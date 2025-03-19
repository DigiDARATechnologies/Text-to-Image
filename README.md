# 🎨 Text-to-Image Generation Project

Welcome to the **Text-to-Image Generation Project**! 🚀 This repository contains a cutting-edge implementation of a deep learning-based text-to-image synthesis system using **Stable Diffusion 2.1**. Built as part of a college project, this application allows users to generate stunning images from text prompts (e.g., "a man on mars, anime") using a React.js front-end and a Flask back-end running on a CPU. 🌌


## ✨ Project Overview

This project leverages **Stable Diffusion 2.1**, a state-of-the-art latent diffusion model, to transform textual descriptions into high-quality images. It’s designed to be accessible, educational, and extensible, making it an ideal showcase for deep learning enthusiasts and students.

- **Front-End:** A sleek React.js interface hosted at `http://localhost:3000` for user interaction.
- **Back-End:** A Flask server at `http://localhost:5000` handling image generation with Stable Diffusion.
- **Dataset Inspiration:** Utilizes concepts similar to COCO datasets for training inspiration (web:8).
- **Performance:** Generates images in ~17-20 minutes on CPU with 20 inference steps (web:9).

## 🚀 Features
- Generate images from any text prompt (e.g., "a futuristic city at night, realistic").
- Real-time loading feedback for the lengthy generation process.
- Download generated images directly from the interface.
- Attractive, modern UI with responsive design.
- Optimized for CPU usage with attention slicing (web:11).

## 📋 Setup Instructions

Follow these steps to set up and run the project on your local machine:

### Prerequisites
- **Python 3.8+**: [Download Python](https://www.python.org/)
- **Node.js 14.x+**: [Download Node.js](https://nodejs.org/)
- **Git**: [Download Git](https://git-scm.com/)
- **Git LFS**: [Install Git LFS](https://git-lfs.github.com/) for large model files
- **Stable Internet Connection**: Required for initial model download

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/DigiDARATechnologies/Text-to-Image.git
   cd Text-to-Image
   ```
2. **Set Up the Python Back-End**
   - Create a virtual environment:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - Install required Python packages:
     ```bash
     pip install diffusers torch transformers accelerate flask flask-cors gevent
     ```
   - Download the Stable Diffusion 2.1 model manually (due to GitHub file size limits):
       - Visit https://huggingface.co/stabilityai/stable-diffusion-2-1/tree/main.
       - Download all files (e.g., model_index.json, pytorch_model.fp16.bin, etc.) and place them in models/stable-diffusion-2-1/.
   - Run the back-end:
     ```bash
     python app.py
     ```
 3. **Set Up the React Front-End**
    - Navigate to the frontend directory:
      ```bash
      cd frontend
      ```
    - Install Node.js dependencies:
      ```bash
      npm install
      ```
    - Start the front-end:
      ```bash
      npm start
      ```
    - Open http://localhost:3000 in your browser to use the application.
 4. **Generate an Image**
      - Enter a prompt (e.g., "a man on mars, anime") in the input field.
      - Click "Generate Image" and wait ~17-20 minutes for the image to appear.
      - Download the generated image using the "Download Image" button.

## Notes
  - The models/ directory is managed with Git LFS due to its large size (14 GB). Ensure Git LFS is installed to access these files.
  - The venv and AttnGAN folders are excluded from this repository (see .gitignore).

## 🛠️ Project Structure
  ```bash
Text-to-Image/
├── frontend/          # React.js front-end code
├── models/            # Stable Diffusion 2.1 model files (via Git LFS)
├── output/            # Generated image output
├── app.py             # Flask back-end server
├── generate_image.py  # Image generation logic
├── main.py            # Main execution script
├── DEEP LEARNING FOR ... # Project documentation
├── .gitignore         # Excludes venv and AttnGAN
└── README.md          # This file
```

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository, submit pull requests, or open issues for bugs and feature requests. Please adhere to the following guidelines:

  - Follow the existing code style.
  - Add tests for new features.
  - Update the README with any significant changes.

## 📜 License
  This project is licensed under the MIT License. See the LICENSE file for details (add a LICENSE file if desired).

## 🙏 Acknowledgments
  - **Stability AI**: For providing the Stable Diffusion 2.1 model.
  - **Hugging Face**: For hosting the model files.
  - **xAI Community**: For inspiration and support.

## 📈 Future Improvements
  - Optimize generation speed with GPU support.
  - Add support for multiple image styles.
  - Enhance UI with real-time progress bars.


## Happy generating! 🎉 Let’s create some amazing images together! 🌟
