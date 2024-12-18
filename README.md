# LLM Picture Sender

This repository provides a simple script that uses a custom LLM to process images. The script loads environment variables for the LLM endpoint, model name, and API key. It then searches an images folder for .jpg and .jpeg files and sends each image with a prompt to the LLM.

## Installing dependencies
```bash
pip install -r requirements.txt
```

## Usage

1. Place your .jpg or .jpeg images in the images folder.
2. Set the environment variables LLM_BASE_URL, LLM_MODEL_NAME, and LLM_API_KEY in your .env file.
3. Run the script. For each image, press Enter to send it to the model and receive a response.