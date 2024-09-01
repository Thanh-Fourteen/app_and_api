"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

# genai.configure(api_key=os.environ["GEMINI_API_KEY"])
genai.configure(api_key="Your_API")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)


def getPrompt(text, type):
    prompt = ""
    if (type == "E2V"):
        prompt = f"Hãy giúp tôi chuyển văn bản sau sang tiếng Việt: {text}. Yêu cầu in chỉ in ra bản dịch không cần in thêm gì cả."
    elif (type == "V2E"):
        prompt = f"Hãy giúp tôi chuyển văn bản sau sang tiếng Anh: {text}. Yêu cầu in chỉ in ra bản dịch không cần in thêm gì cả."
    return prompt

def getRes(text, type):
    prompt = getPrompt(text, type)
    response = model.generate_content(prompt)
    return response.text