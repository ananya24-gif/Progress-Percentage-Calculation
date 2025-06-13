from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from PIL import Image
import base64

# Load ChatOllama with local LLaVA 7B model
llm = ChatOllama(model="llava:7b")

# Utility to encode image to base64 string
def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Function to call Ollama with vision input
def analyze_progress_with_ollama(arch_path, site_path):
    arch_img_b64 = encode_image(arch_path)
    site_img_b64 = encode_image(site_path)

    prompt = (
        "You are a construction progress analysis expert. "
        "Compare the following two images:\n"
        "1. Architectural Rendering (future building appearance).\n"
        "2. Construction Site (current real-world image).\n"
        "Estimate the construction progress percentage completed. "
        "Provide detailed reasoning and list completed and pending components."
    )

    # Prepare LangChain-compatible message
    messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{arch_img_b64}"}},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{site_img_b64}"}}
            ]
        }
    ]

    # Run LLaVA 7B via Ollama
    response = llm.invoke(messages)
    return response.content

# Example usage
architectural_img_path = "image1.jpg"
site_img_path = "image2.jpg"

result = analyze_progress_with_ollama(architectural_img_path, site_img_path)
print("🔍 Analysis Result:\n", result)
