from diffusers import StableDiffusionPipeline
from uuid import uuid4 as uuid
import torch

def generate(prompt, save_path):
    EXT = ".jpg"
    rng = str(uuid())

    model_id = "dreamlike-art/dreamlike-photoreal-2.0"

    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")

    image = pipe(prompt).images[0]

    image.save(f'{save_path}.{EXT}')
    
    return save_path + f".{EXT}"