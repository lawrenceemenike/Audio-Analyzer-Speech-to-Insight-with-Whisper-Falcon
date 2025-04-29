# 🎙️ Audio Analyzer: Speech-to-Insight with Whisper + Falcon

This is one of many practical projects being developed as part of my IBM Generative AI Engineering certification journey.

In this app, I integrated open-source speech-to-text and text generation models to build a simple audio analysis tool. The pipeline takes any uploaded audio file, transcribes the content using OpenAI’s Whisper model (running locally via Hugging Face), and then summarizes the key points using Falcon-7B-Instruct — a powerful LLM optimized for instruction-following.

---

## ✅ What It Does

- Accepts uploaded audio (MP3, WAV, etc.)
- Converts speech to text using **Whisper**
- Summarizes the transcribed text using **Falcon** or any Hugging Face-supported LLM
- Presents both transcription and summary in a clean Gradio interface

---

## 🛠️ Technologies Used

- Python 🐍
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Whisper ASR (openai/whisper-tiny.en)](https://huggingface.co/openai/whisper-tiny.en)
- [Falcon-7B-Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct) (can be replaced with lighter models if needed)
- Gradio for UI


## Final Note
This project is deliberately designed to be simple and reusable. It’s not just about model usage — it’s about integrating capabilities into an actual usable product. The goal here is functional fluency.

More projects to come.
