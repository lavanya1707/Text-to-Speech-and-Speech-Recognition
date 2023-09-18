import streamlit as st
from gtts import gTTS
import os
import speech_recognition as sr

# Streamlit app title
st.title('Text to Speech and Speech to Text')

# Text input area for text-to-speech conversion
text_to_speech_input = st.text_area('Enter the text for Text-to-Speech:', '')

# Button to trigger text-to-speech conversion
if st.button('Convert to Speech'):
    if text_to_speech_input:
        # Convert text to speech
        tts = gTTS(text_to_speech_input)
        tts.save("output.mp3")

        # Play the audio file using a system command
        os.system("output.mp3")
    else:
        st.warning('Please enter text for Text-to-Speech conversion.')

# Display a separator between the two functionalities
st.markdown('---')

# Speech recognition
st.subheader('Speech Recognition')

# Button to initiate audio recording
start_recording = st.button('Start Recording')

# Initialize recognizer outside of the loop to maintain state
recognizer = sr.Recognizer()

# Placeholder for recognized text
recognized_text = ""

# If the "Start Recording" button is clicked
if start_recording:
    with sr.Microphone() as source:
        st.write("Recording...")
        audio = recognizer.listen(source)
        st.write("Finished recording.")
    
    try:
        recognized_text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        st.warning("Sorry, could not understand audio.")
    except sr.RequestError as e:
        st.warning("Could not request results from Google Web Speech API; {0}".format(e))

# Display recognized text
st.write("Recognized Text:", recognized_text)
