import os
import base64
import asyncio
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
 
# Load API key from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
 
if not api_key:
    st.error("GROQ_API_KEY not found in environment variables.")
    st.stop()
 
client = Groq(api_key=api_key)
 
# Helper to encode image file to base64
def encode_uploaded_file_to_base64(upload_file) -> str:
    file_bytes = upload_file.read()
    encoded = base64.b64encode(file_bytes).decode("utf-8")
    ext = upload_file.name.split(".")[-1].lower()
    mime_type = "jpeg" if ext in ["jpg", "jpeg"] else "png"
    return f"data:image/{mime_type};base64,{encoded}"
 
# Call Groq API
def call_groq(model, messages):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_completion_tokens=1024,
        top_p=1,
        stream=False
    )
    return response.choices[0].message.content
 
# Streamlit UI
st.title("🏗️ Construction Progress Estimator")
 
st.write("Upload 2 images:")
plan_image = st.file_uploader("1️⃣ Upload 2D Rendered Architectural Design", type=["jpg", "jpeg", "png"])
site_image = st.file_uploader("2️⃣ Upload Real Construction Site Photo", type=["jpg", "jpeg", "png"])
 
if plan_image and site_image:
    if st.button("Analyze Progress 🚀"):
        with st.spinner("Analyzing..."):
 
            IMAGE_1_BASE64 = encode_uploaded_file_to_base64(plan_image)
            IMAGE_2_BASE64 = encode_uploaded_file_to_base64(site_image)
 
            messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """
You are a highly experienced civil engineer and construction progress auditor.
 
TASK:
- Compare these two images:
    1️⃣ First is a 2D rendered architectural design.
    2️⃣ Second is a real construction site photo.
   
- Your main goal is to provide:
    - Estimated percentage of work completed.
    - Keep percentage in one short line at the top.
    - Then briefly explain completed vs pending work.
 
RESPONSE FORMAT STRICTLY:
Progress Completed: __%
 
Completed Work:
- (list of completed work, 2-3 bullets)
 
Pending Work:
- (list of pending work, 2-3 bullets)
 
Avoid extra paragraphs. Stay to the point.
"""
                        },
                        {"type": "image_url", "image_url": {"url": IMAGE_1_BASE64}},
                        {"type": "image_url", "image_url": {"url": IMAGE_2_BASE64}}
                    ]
                }
            ]
 
            result = call_groq("meta-llama/llama-4-maverick-17b-128e-instruct", messages)
            st.success("✅ Analysis Completed")
            st.write(result)