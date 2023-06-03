from pathlib import Path

import torch
from diffusers import StableDiffusionPipeline
from PIL.Image import Image

# Path to the token file
token_path = Path("token.txt")
# Read the token from the file and remove leading/trailing whitespaces
token = token_path.read_text().strip()

# Create a StableDiffusionPipeline instance using the pre-trained model
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    revision="fp16",
    torch_dtype=torch.float16,
    use_auth_token=token,
)

# Move the pipeline to CUDA device for GPU acceleration
pipe.to("cuda")

# Function to obtain an image based on the provided prompt
def obtain_image(
    prompt: str,
    *,
    seed: int | None = None,
    num_inference_steps: int = 50,
    guidance_scale: float = 7.5,
) -> Image:
    # Create a generator for random number generation with a specified seed
    # If seed is None, no seed is set
    generator = None if seed is None else torch.Generator("cuda").manual_seed(seed)
    # Print the device being used for image generation
    print(f"Using device: {pipe.device}")
    # Generate the image based on the prompt using the StableDiffusionPipeline
    image: Image = pipe(
        prompt,
        guidance_scale=guidance_scale,
        num_inference_steps=num_inference_steps,
        generator=generator,
    ).images[0]
    # Return the generated image
    return image

# Example usage of the obtain_image function
# Uncomment the following line and provide the necessary values to generate an image
# image = obtain_image(prompt, num_inference_steps=5, seed=1024)
