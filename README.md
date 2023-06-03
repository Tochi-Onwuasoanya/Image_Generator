# Image_Generator
This is a web application that provides an API for generating images using the StableDiffusion model from the Hugging Face library. It is built using the FastAPI framework.

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

4. Stopping the applicationL
Press Ctrl + C to stop the running application.
