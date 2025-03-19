import os
from diffusers import StableDiffusionPipeline
import torch

# Load the model locally (manually downloaded, using .fp16.bin for CPU efficiency)
model_dir = os.path.join(os.getcwd(), "models", "stable-diffusion-2-1")
pipe = StableDiffusionPipeline.from_pretrained(
    model_dir,
    torch_dtype=torch.float32,
    local_files_only=True,  # Use only local files, no network access
    variant="fp16"  # Explicitly specify fp16 variant to match .fp16.bin files
)
pipe = pipe.to("cpu")  # Use CPU for your setup

# Optimize for low memory on CPU
pipe.enable_attention_slicing()  # Reduce memory usage on CPU (recommended for low-resource setups)

# Generate image from text with reduced steps for faster generation
prompt = "a man viewing towards sun, realistic, outdoor scene"
try:
    image = pipe(prompt, num_inference_steps=20).images[0]  # Reduced to 20 steps for faster generation
    if not os.path.exists("output"):
        os.makedirs("output")
    image.save("output/generated_image.png")
    print(f"Image saved to: output/generated_image.png")
except Exception as e:
    print(f"Error generating image: {e}")