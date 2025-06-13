from dotenv import load_dotenv
import os
import base64
from groq import Groq

# Load API key from .env or ask
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    api_key = input("Please enter your Groq API key: ")
    os.environ["GROQ_API_KEY"] = api_key

client = Groq(api_key=api_key)

# Function to encode local image file to base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")
    return f"data:image/jpeg;base64,{encoded}"

# Replace these with your actual local file paths
image_1_path = "C:/Users/admin/Downloads/ShriVaasa_2D.png"
image_2_path = "C:/Users/admin/Downloads/ShriVaasa_010425.jpeg"

IMAGE_1_BASE64 = encode_image_to_base64(image_1_path)
IMAGE_2_BASE64 = encode_image_to_base64(image_2_path)

# Build messages
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
            {
                "type": "image_url",
                "image_url": {"url": IMAGE_1_BASE64}
            },
            {
                "type": "image_url",
                "image_url": {"url": IMAGE_2_BASE64}
            }
        ]
    }
]

# Send request to Groq
completion = client.chat.completions.create(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    messages=messages,
    temperature=0.7,
    max_completion_tokens=1024,
    top_p=1,
    stream=True
)

# Print streamed output
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
