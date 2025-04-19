import whisper
from google.cloud import speech
from langgraph.graph import StateGraph, MessagesState
from langgraph.graph import START, END

# Function to transcribe audio using Google Speech-to-Text
def transcribe_audio(state):
#     """Transcribe audio using Google Cloud Speech-to-Text API"""
#     # Get audio data from state
    audio_file_path = state.get("messages")[0].content
    
    model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_file_path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    print(result.text)
    # Initialize the client
    # client = speech.SpeechClient()
    
    # # Read the audio file
    # with open(audio_file_path, "rb") as audio_file:
    #     content = audio_file.read()
    
    # # Configure the recognition settings
    # config = speech.RecognitionConfig(
    #     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    #     sample_rate_hertz=16000,
    #     language_code="en-US",
    #     enable_automatic_punctuation=True,
    #     audio_channel_count=2
    # )
    
    # # Create the audio object
    # audio = speech.RecognitionAudio(content=content)
    
    # # Perform the transcription
    # response = client.recognize(config=config, audio=audio)
    
    # # Process and return the response
    # transcription = ""
    # for result in response.results:
    #     transcription += result.alternatives[0].transcript
    
    # Extract the 
    # Update state with transcription
    state["messages"].append({"role": "user", "content": result.text})

    return state

# Define your graph
graph = StateGraph(MessagesState)

# Add nodes for audio processing and other tasks
graph.add_node("transcribe_audio", transcribe_audio)

# Add more edges as needed for your application flow
graph.add_edge(START, "transcribe_audio")
graph.add_edge("transcribe_audio", END)

# Compile the graph
compiled_graph = graph.compile()

result = compiled_graph.invoke({"messages": "C:\\Dev\\HackAI\\backend\\test.wav"})

print(result)


