from flask import Flask, request, send_file
from flask_cors import CORS
from diffusers import StableDiffusionPipeline
import torch
import os
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()  # Patch for asynchronous I/O

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the model locally
model_dir = os.path.join(os.getcwd(), "models", "stable-diffusion-2-1")
pipe = StableDiffusionPipeline.from_pretrained(
    model_dir,
    torch_dtype=torch.float32,
    local_files_only=True,
    variant="fp16"
)
pipe = pipe.to("cpu")
pipe.enable_attention_slicing()

@app.route('/generate', methods=['POST'])
def generate_image():
    prompt = request.json['prompt']
    if not prompt:
        return {"error": "Prompt is required"}, 400

    try:
        image = pipe(prompt, num_inference_steps=20).images[0]
        if not os.path.exists("output"):
            os.makedirs("output")
        image.save("output/generated_image.png")
        return send_file("output/generated_image.png", mimetype='image/png')
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    # Use gevent WSGI server without timeout (gevent handles long-running tasks natively)
    http_server = WSGIServer(('0.0.0.0', 5000), app, log=None)
    http_server.serve_forever()