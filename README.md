# LLM Vision-to-Markdown Converter

This repository provides a script that uses a custom Large Language Model (LLM) endpoint to analyze images and convert their visual content into Markdown format. The script takes `.jpg` or `.jpeg` images from the `images` directory, sends them to the LLM along with a prompt, and receives a fully Markdown-formatted description of the image.

## Features

- **LLM Integration**: Easily configure the script to use custom LLM endpoints such as Llama 3.2 Vision models.
- **Image-to-Markdown Conversion**: The response is returned solely in Markdown format for easy integration into documentation, reports, or websites.
- **Customizable Output**: Optionally save LLM responses to `.md` files within the `output` directory.

## Getting Started

### Prerequisites

- Python 3.9+ recommended
- A compatible LLM API endpoint, model name, and API key
- `pip` for installing dependencies

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/llm-vision-to-markdown.git
   cd llm-vision-to-markdown
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Copy the `.env.example` file to `.env` and fill in your LLM configuration:

```plaintext
LLM_BASE_URL=<your-llm-endpoint>
LLM_MODEL_NAME=<your-llm-model-name>
LLM_API_KEY=<your-llm-api-key>
SAVE_RESPONSE_TO_FILE=true  # or false
```

- `LLM_BASE_URL`: The base URL of the LLM inference endpoint.
- `LLM_MODEL_NAME`: The model name (e.g., "llama3.2-vision").
- `LLM_API_KEY`: Your API key for authentication.
- `SAVE_RESPONSE_TO_FILE`: If `true`, Markdown responses are saved to the `output` folder.

### Usage

1. Place one or more `.jpg` or `.jpeg` images in the `images` directory.

2. Run the script:
   ```bash
   python main.py
   ```

3. The script will process each image, send it to the LLM, and print the Markdown response. If `SAVE_RESPONSE_TO_FILE` is `true`, a corresponding `.md` file will be created in the `output` folder.

### Example

If you place `sample.jpg` in the `images` folder and run the script, you might see output like:

```plaintext
File: sample.jpg
User Prompt: 
[...prompt...]
Model Response:
# A Beautiful Landscape

- **Mountains**: Tall, snow-capped peaks in the background
- **Lake**: A calm, reflective surface at the center
- **Trees**: Lush green foliage on both sides of the view
--------------------------------------------------
```

This response would be saved in `output/sample.jpg.md`.

### Troubleshooting

- If the script prints "No .jpg or .jpeg files in the images folder.", ensure that you have placed images in the correct directory.
- If you encounter authentication or network issues, verify your `.env` settings and ensure you have a stable internet connection.

### Contributing

Feel free to open issues or create pull requests for bug fixes, feature requests, or other improvements.

### License

This project is licensed under the [MIT License](LICENSE).