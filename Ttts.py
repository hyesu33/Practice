!pip install gtts

import streamlit as st
from gtts import gTTS

# Function to convert text to speech and save as mp3 file
def text_to_speech_file(text, filename="tts_output.mp3"):
    tts = gTTS(text, lang='en')
    tts.save(filename)

# Predefined text
predefined_text = """
In the small town of Willowby, there stood an old library that was rumored to be enchanted. Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true. As the clock struck twelve, the books began to rustle. To Sarah's amazement, characters stepped out of their pages. She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained. Sarah spent the whole night listening and learning from the characters, promising to keep their secret. As dawn approached, they returned to their pages. Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
"""

# Initialize session state for buttons
if 'play_audio' not in st.session_state:
    st.session_state.play_audio = False
if 'show_text' not in st.session_state:
    st.session_state.show_text = False

# Buttons
if st.button("Play TTS"):
    st.session_state.play_audio = True

if st.button("Show Text"):
    st.session_state.show_text = not st.session_state.show_text  # Toggle text visibility

# Play audio if button pressed
if st.session_state.play_audio:
    mp3_filename = "tts_output.mp3"
    text_to_speech_file(predefined_text, mp3_filename)

    with open(mp3_filename, "rb") as f:
        audio_bytes = f.read()
        st.audio(audio_bytes, format="audio/mp3")

    st.session_state.play_audio = False

# Display text if toggled
if st.session_state.show_text:
    st.write(predefined_text)
