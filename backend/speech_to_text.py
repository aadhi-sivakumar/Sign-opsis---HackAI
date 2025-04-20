import json
import whisper
from langgraph.graph import StateGraph, MessagesState
from langgraph.graph import START, END

import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

COORDINATE_DATA = "backend/coordinates.json"

def transcribe_audio(state):
    audio_file_path = state.get("messages")[-1].content
    
    model = whisper.load_model("base")
    transcription = model.transcribe(audio_file_path)
    state["messages"].append({"role": "user", "content": transcription["text"]})

    return state

def english_to_asl_structure(state):
    text = state.get("messages")[-1].content
    doc = nlp(text)
    
    time_markers = []
    topics = []
    verbs = []
    objects = []
    others = []
    
    negation = False
    
    for token in doc:
        if token.dep_ == "neg":
            negation = True
            continue
            
        if token.ent_type_ == "DATE" or token.ent_type_ == "TIME" or token.text.lower() in ["today", "tomorrow", "yesterday", "now", "later"]:
            time_markers.append(token.text.upper())
        
        elif token.pos_ == "DET" or (token.lemma_ == "be" and token.pos_ == "AUX"):
            continue
            
        elif token.dep_ in ["nsubj", "nsubjpass"]:
            topics.append(token.text.upper())
            
        elif token.pos_ == "VERB":
            verbs.append(token.text.upper())
            
        elif token.dep_ in ["dobj", "pobj"]:
            objects.append(token.text.upper())
            
        elif token.pos_ not in ["PUNCT", "ADP", "PART"]:
            others.append(token.text.upper())
    
    asl_components = time_markers + topics + objects + verbs
    
    if negation:
        asl_components.append("NOT")
        
    asl_structure = " ".join(asl_components)
    state["messages"].append({"role": "user", "content": asl_structure})

    return state

def get_asl_coordinates(state):
    text = state.get("messages")[-1].content
    words = text.split(' ')
    with open(COORDINATE_DATA, 'r') as file:
        coordinates = json.load(file)
    word_cords = []
    for word in words:
        cord = coordinates.get(word)
        if cord != None:
            for c in cord:
                word_cords.append((c["Left Hand Coordinates"], c["Right Hand Coordinates"]))
        else:
            for let in word:
                word_cords.append(coordinates[let])
    state["messages"].append({"role": "user", "content": word_cords})

    return state

graph = StateGraph(MessagesState)

# Add nodes for audio processing and other tasks
graph.add_node("transcribe_audio", transcribe_audio)
graph.add_node("asl_structure", english_to_asl_structure)
graph.add_node("get_asl_coordinates", get_asl_coordinates)

# Add more edges as needed for your application flow
graph.add_edge(START, "transcribe_audio")
graph.add_edge("transcribe_audio", "asl_structure")
graph.add_edge("asl_structure", "get_asl_coordinates")
graph.add_edge("get_asl_coordinates", END)

# Compile the graph
compiled_graph = graph.compile()

result = compiled_graph.invoke({"messages": "C:\\Dev\\HackAI\\backend\\test.wav"})
print(result["messages"][-1].content)


