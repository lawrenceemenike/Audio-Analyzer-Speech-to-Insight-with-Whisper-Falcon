import streamlit as st
from transformers import pipeline
import torch
import tempfile

# Title and description
st.title("🎙️ Audio Transcription App")
st.write("Upload an audio file and get the transcription using OpenAI Whisper.")

# File uploader
uploaded_audio = st.file_uploader("Choose an audio file", type=["mp3", "wav", "m4a"])

if uploaded_audio is not None:
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_audio.read())
        tmp_path = tmp.name

    # Load Whisper model
    with st.spinner("Transcribing..."):
        pipe = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-tiny.en",
            chunk_length_s=30,
        )
        result = pipe(tmp_path, batch_size=8)["text"]

    # Display the result
    st.subheader("📝 Transcribed Text:")
    st.write(result)
