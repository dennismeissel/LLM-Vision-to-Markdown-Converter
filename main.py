import os
import base64
import requests
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain.llms.base import LLM
from typing import Optional, List

load_dotenv()

class CustomLLM(LLM, BaseModel):
    """
    A custom LLM that sends a prompt and an image to a specified endpoint.
    """
    invoke_url: str
    api_key: str
    model_name: str
    temperature: float
    top_p: float
    max_tokens: int

    @property
    def _llm_type(self) -> str:
        return "custom_llm"

    def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }

        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "stream": False,
        }

        response = requests.post(self.invoke_url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            return "No response found."

def main():
    base_url = os.getenv("LLM_BASE_URL")
    model = os.getenv("LLM_MODEL_NAME")
    api_key = os.getenv("LLM_API_KEY")

    if not all([base_url, model, api_key]):
        print("Please set the environment variables LLM_BASE_URL, LLM_MODEL_NAME, and LLM_API_KEY.")
        return

    print("Custom LLM with Image Example")

    user_prompt = "What is on this picture?"

    image_folder = "images"
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg'))]

    if not image_files:
        print("No .jpg or .jpeg files found in the 'images' folder.")
        return

    # Loop through each image, print filename, and wait for user to press Enter before processing
    for image_file in image_files:
        print("File path:", image_file)
        input("Press Enter to send this image to the LLM...")

        image_path = os.path.join(image_folder, image_file)

        if not os.path.isfile(image_path):
            print("Image file not found. Please check the path and try again.")
            continue

        with open(image_path, "rb") as f:
            image_b64 = base64.b64encode(f.read()).decode()

        full_prompt = f'{user_prompt} <img src="data:image/jpg;base64,{image_b64}" />'

        custom_llm = CustomLLM(
            invoke_url=base_url,
            model_name=model,
            api_key=api_key,
            temperature=0.7,
            top_p=0.9,
            max_tokens=1024,
        )
        print("User Prompt: " + user_prompt)
        response = custom_llm.invoke(full_prompt)
        print("Model Response:")
        print(response)
        print("-" * 50)  # Separator line between responses

if __name__ == "__main__":
    main()