import io

from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel

from ml import obtain_image

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Endpoint to read item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Item model for creating items
class Item(BaseModel):
    name: str
    price: float
    tags: list[str] = []

# Endpoint to create an item
@app.post("/items/")
def create_item(item: Item):
    return item

# Endpoint to generate an image
@app.get("/generate")
def generate_image(
    prompt: str,
    *,
    seed: int | None = None,
    num_inference_steps: int = 50,
    guidance_scale: float = 7.5
):
    # Obtain the image based on the provided prompt
    image = obtain_image(
        prompt,
        num_inference_steps=num_inference_steps,
        seed=seed,
        guidance_scale=guidance_scale,
    )
    # Save the generated image as "image.png"
    image.save("image.png")
    # Return the generated image as a file response
    return FileResponse("image.png")

# Endpoint to generate an image and stream it in memory
@app.get("/generate-memory")
def generate_image_memory(
    prompt: str,
    *,
    seed: int | None = None,
    num_inference_steps: int = 50,
    guidance_scale: float = 7.5
):
    # Obtain the image based on the provided prompt
    image = obtain_image(
        prompt,
        num_inference_steps=num_inference_steps,
        seed=seed,
        guidance_scale=guidance_scale,
    )
    # Create an in-memory stream
    memory_stream = io.BytesIO()
    # Save the generated image to the in-memory stream in PNG format
    image.save(memory_stream, format="PNG")
    memory_stream.seek(0)
    # Return the in-memory stream as a streaming response with media type "image/png"
    return StreamingResponse(memory_stream, media_type="image/png")
