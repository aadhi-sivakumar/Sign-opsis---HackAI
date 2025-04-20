import json
import whisper
from langgraph.graph import StateGraph, MessagesState
from langgraph.graph import START, END

import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

COORDINATE_DATA = "coordinates.json"

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

def get_asl_coordinates(text):
    words = text.split(' ')
    with open(COORDINATE_DATA, 'r') as file:
        coordinates = json.load(file)
    word_cords = []
    for word in words:
        cord = coordinates.get(word)
        if cord != None:
            word_cords.append(cord)
        else:
            spell_coord =[]
            for let in word:
                spell_coord.append(coordinates[let])
            word_cords.append(spell_coord)

    return word_cords

graph = StateGraph(MessagesState)

# Add nodes for audio processing and other tasks
graph.add_node("transcribe_audio", transcribe_audio)
graph.add_node("asl_structure", english_to_asl_structure)
graph.add_node("get_asl_coordinates", get_asl_coordinates)

# Add more edges as needed for your application flow
graph.add_edge(START, "transcribe_audio")
graph.add_edge("transcribe_audio", "asl_structure")
graph.add_edge("asl_structure", END)

# Compile the graph
compiled_graph = graph.compile()

import cv2
import numpy as np

image_width = 800
image_height = 750

def draw_hand(image, coordinates):
    color = (0, 0, 0)
    if len(coordinates) == 0:
        return
    cv2.line(image, (int(image_width*coordinates['0'][0]), int(image_height*coordinates['0'][1])), (int(image_width*coordinates['1'][0]), int(image_height*coordinates['1'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['1'][0]), int(image_height*coordinates['1'][1])), (int(image_width*coordinates['2'][0]), int(image_height*coordinates['2'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['2'][0]), int(image_height*coordinates['2'][1])), (int(image_width*coordinates['3'][0]), int(image_height*coordinates['3'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['3'][0]), int(image_height*coordinates['3'][1])), (int(image_width*coordinates['4'][0]), int(image_height*coordinates['4'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['0'][0]), int(image_height*coordinates['0'][1])), (int(image_width*coordinates['5'][0]), int(image_height*coordinates['5'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['0'][0]), int(image_height*coordinates['0'][1])), (int(image_width*coordinates['17'][0]), int(image_height*coordinates['17'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['5'][0]), int(image_height*coordinates['5'][1])), (int(image_width*coordinates['9'][0]), int(image_height*coordinates['9'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['9'][0]), int(image_height*coordinates['9'][1])), (int(image_width*coordinates['13'][0]), int(image_height*coordinates['13'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['13'][0]), int(image_height*coordinates['13'][1])), (int(image_width*coordinates['17'][0]), int(image_height*coordinates['17'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['5'][0]), int(image_height*coordinates['5'][1])), (int(image_width*coordinates['6'][0]), int(image_height*coordinates['6'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['6'][0]), int(image_height*coordinates['6'][1])), (int(image_width*coordinates['7'][0]), int(image_height*coordinates['7'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['7'][0]), int(image_height*coordinates['7'][1])), (int(image_width*coordinates['8'][0]), int(image_height*coordinates['8'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['9'][0]), int(image_height*coordinates['9'][1])), (int(image_width*coordinates['10'][0]), int(image_height*coordinates['10'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['10'][0]), int(image_height*coordinates['10'][1])), (int(image_width*coordinates['11'][0]), int(image_height*coordinates['11'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['11'][0]), int(image_height*coordinates['11'][1])), (int(image_width*coordinates['12'][0]), int(image_height*coordinates['12'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['13'][0]), int(image_height*coordinates['13'][1])), (int(image_width*coordinates['14'][0]), int(image_height*coordinates['14'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['14'][0]), int(image_height*coordinates['14'][1])), (int(image_width*coordinates['15'][0]), int(image_height*coordinates['15'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['15'][0]), int(image_height*coordinates['15'][1])), (int(image_width*coordinates['16'][0]), int(image_height*coordinates['16'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['17'][0]), int(image_height*coordinates['17'][1])), (int(image_width*coordinates['18'][0]), int(image_height*coordinates['18'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['18'][0]), int(image_height*coordinates['18'][1])), (int(image_width*coordinates['19'][0]), int(image_height*coordinates['19'][1])), color, 5)
    cv2.line(image, (int(image_width*coordinates['19'][0]), int(image_height*coordinates['19'][1])), (int(image_width*coordinates['20'][0]), int(image_height*coordinates['20'][1])), color, 5)


def audio_to_asl(file_path):
    result = compiled_graph.invoke({"messages": file_path})
    coordinates = get_asl_coordinates(result["messages"][-1].content)
    out = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 20, (image_height, image_width))

    for word_cord in coordinates:
        if word_cord[0].get('Left Hand Coordinates') != None:
            for cord in word_cord:
                    image = np.ones((image_width, image_height, 3), dtype=np.uint8)*255
                    coord1 = cord["Left Hand Coordinates"]
                    unnorm_coord1 = [(image_width*c[0], image_height*c[1]) for c in list(coord1.values())]
                    coord2 = cord["Right Hand Coordinates"]
                    unnorm_coord2 = [(image_width*c[0], image_height*c[1]) for c in list(coord2.values())]
                    for c in unnorm_coord1:
                        cv2.circle(image, (int(c[0]), int(c[1])), 10, (0, 0, 0), -1)
                    draw_hand(image, coord1)
                    for c in unnorm_coord2:
                        cv2.circle(image, (int(c[0]), int(c[1])), 10, (0, 0, 0), -1)
                    draw_hand(image, coord2)
                    out.write(image)
                    #cv2.imshow("img", image)
                    key = cv2.waitKey(50)
        else:
            for let_cord in word_cord:
                image = np.ones((image_width, image_height, 3), dtype=np.uint8)*255
                unnorm_coord = [(image_width*c[0], image_height*c[1]) for c in list(let_cord.values())]
                for c in unnorm_coord:
                    cv2.circle(image, (int(c[0]), int(c[1])), 10, (0, 0, 0), -1)
                draw_hand(image, let_cord)
                out.write(image)
                #cv2.imshow("img", image)
                key = cv2.waitKey(300)
            key = cv2.waitKey(50)

    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    audio_to_asl("C:\\Dev\\HackAI\\backend\\test.wav")
