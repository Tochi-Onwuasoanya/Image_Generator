# Image_Generator
This is a web application that provides an API for generating images using the StableDiffusion model from the Hugging Face library. It is built using the FastAPI framework.

## Languages, Tools, and Technologies
- Python: The programming language used for the development of the application 

### Tools and Technologies
- FastAPI: A modern web framework used for building APIs with Python. FastAPI provides high-performance capabilities and easy-to-use features for creating web applications.

- PyTorch: A deep learning framework used for creating and training neural networks. In this project, PyTorch is used for working with the StableDiffusion model and performing image generation.

- Hugging Face: A popular platform for accessing and using pre-trained models. The code uses the Hugging Face library to load the StableDiffusion model and generate images based on prompts.

- diffusers: A library that provides implementations of diffusion models for image generation. The StableDiffusionPipeline from the diffusers library is used in the code to perform image generation.

- PIL (Python Imaging Library): A library used for opening, manipulating, and saving images. The code uses the PIL.Image module for working with images, such as saving the generated images.

- io: A module in Python's standard library used for working with streams. The io module is used to create an in-memory stream for streaming the generated images in the `/generate-memory` endpoint.

- FastAPI's FileResponse and StreamingResponse: FastAPI provides these response classes for handling file responses and streaming responses. They are used in the code to return the generated images as file responses or streaming responses.

Altogether everything above is combined to create a web application that exposes endpoints for generating images using the StableDiffusion model. FastAPI handles the HTTP requests and responses, PyTorch and Hugging Face are used for the image generation process, and PIL is used for image manipulation and saving.

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/image-generator.git
   cd image-generator
   
2. Install the required dependencies 
    pip install -r requirements.txt

3. Set up the authentication token:
   Obtain your authentication token at https://huggingface.co/settings/tokens.
   Create a file named token.txt in the root directory of the project.
   Paste your token into the token.txt file
   
# Usage 
1. Start the application
uvicorn main:app --reload

2. API Endpoints:

- GET / - Returns a simple JSON response indicating the server is running.
- GET /items/{item_id} - Returns a JSON response containing the provided item_id.
- POST /items/ - Accepts a JSON payload to create an item.
- GET /generate - Generates an image based on the provided prompt. The generated image is saved as "image.png" and returned as a file response.
- GET /generate-memory - Generates an image based on the provided prompt and streams it directly as a response in the PNG format.

3. Example API Request:
To generate an image using the /generate endpoint, you can make a GET request to the following URL:
http://localhost:8000/generate?prompt=your-prompt

Replace your-prompt with the desired prompt for generating the image.
You can also provide additional query parameters to customize the image generation process, such as seed, num_inference_steps, and guidance_scale.

4. Stopping the application:
Press Ctrl + C to stop the running application.
