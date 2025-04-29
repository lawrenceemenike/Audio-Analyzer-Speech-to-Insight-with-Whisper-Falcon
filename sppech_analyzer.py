import torch
from transformers import pipeline
import gradio as gr

# Load Whisper for speech-to-text
asr_pipeline = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=30
)

# Load Falcon or another HF text generation model
text_pipeline = pipeline(
    "text-generation",
    model="tiiuae/falcon-7b-instruct",  # You can swap this with 'gpt2', 'bloom', etc.
    max_new_tokens=256,
    temperature=0.7
)

# Processing function for Gradio
def analyze_audio(audio_path):
    # Step 1: Transcribe the audio
    transcript = asr_pipeline(audio_path)["text"]

    # Step 2: Summarize key points using LLM
    prompt = f"List the key points with details from the context:\n\n{transcript}"
    summary = text_pipeline(prompt)[0]["generated_text"]

    return transcript, summary

# Gradio UI
iface = gr.Interface(
    fn=analyze_audio,
    inputs=gr.Audio(type="filepath", label="Upload Audio"),
    outputs=[
        gr.Textbox(label="Transcribed Text"),
        gr.Textbox(label="Key Points Summary")
    ],
    title="🎤 Audio Analyzer",
    description="Upload an audio file. Whisper transcribes it, Falcon generates key points summary."
)

iface.launch(server_name="0.0.0.0", server_port=7860)
#iface.launch()