import whisper
from google.cloud import speech
from langgraph.graph import StateGraph, MessagesState
from langgraph.graph import START, END

import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

def english_to_asl_structure(text):
    doc = nlp(text)
    
    # Extract components
    time_markers = []
    topics = []
    verbs = []
    objects = []
    others = []
    
    # Identify negation
    negation = False
    
    for token in doc:
        # Check for negation
        if token.dep_ == "neg":
            negation = True
            continue
            
        # Time expressions (simplified)
        if token.ent_type_ == "DATE" or token.ent_type_ == "TIME" or token.text.lower() in ["today", "tomorrow", "yesterday", "now", "later"]:
            time_markers.append(token.text.upper())
        
        # Skip articles and "to be" verbs
        elif token.pos_ == "DET" or (token.lemma_ == "be" and token.pos_ == "AUX"):
            continue
            
        # Identify subjects/topics
        elif token.dep_ in ["nsubj", "nsubjpass"]:
            topics.append(token.text.upper())
            
        # Identify main verbs
        elif token.pos_ == "VERB":
            verbs.append(token.text.upper())
            
        # Identify objects
        elif token.dep_ in ["dobj", "pobj"]:
            objects.append(token.text.upper())
            
        # Other elements
        elif token.pos_ not in ["PUNCT", "ADP", "PART"]:
            others.append(token.text.upper())
    
    # Construct ASL structure: TIME + TOPIC + OBJECT + VERB + NOT (if negation)
    asl_components = time_markers + topics + objects + verbs
    
    if negation:
        asl_components.append("NOT")
        
    return " ".join(asl_components)



def transcribe_audio(state):
    audio_file_path = state.get("messages")[0].content
    
    model = whisper.load_model("base")
    transcription = model.transcribe(audio_file_path)
    asl_structure = english_to_asl_structure(transcription["text"])
    state["messages"].append({"role": "user", "content": asl_structure})

    return state

graph = StateGraph(MessagesState)

# Add nodes for audio processing and other tasks
graph.add_node("transcribe_audio", transcribe_audio)

# Add more edges as needed for your application flow
graph.add_edge(START, "transcribe_audio")
graph.add_edge("transcribe_audio", END)

# Compile the graph
compiled_graph = graph.compile()

result = compiled_graph.invoke({"messages": "C:\\Dev\\HackAI\\backend\\test.wav"})

print(result["messages"][1].content)


