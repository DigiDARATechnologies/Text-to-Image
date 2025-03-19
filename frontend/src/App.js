import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [image, setImage] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateImage = async () => {
    if (!prompt.trim()) {
      setError("Prompt is required");
      return;
    }

    setLoading(true);
    setError(null);
    setImage(null);

    try {
      // Increase timeout for long-running requests (25 minutes)
      const response = await axios.post('http://localhost:5000/generate', { prompt }, {
        timeout: 1500000,  // 25 minutes in milliseconds
        responseType: 'blob',  // Ensure response is treated as a blob for image download
      });
      const imageBlob = response.data;
      setImage(URL.createObjectURL(imageBlob));
    } catch (error) {
      setError(error.response?.data?.error || 'Error generating image');
    } finally {
      setLoading(false);
    }
  };

  const downloadImage = () => {
    if (image) {
      const link = document.createElement('a');
      link.href = image;
      link.download = 'generated_image.png';  // Default filename for download
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Text-to-Image Generator</h1>
      </header>
      <div className="container">
        <div className="input-section">
          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Enter text prompt (e.g., 'a man on mars, anime')"
            className="prompt-input"
          />
          <button onClick={generateImage} disabled={loading} className="generate-button">
            {loading ? 'Generating...' : 'Generate Image'}
          </button>
        </div>
        {error && <p className="error">{error}</p>}
        {loading && <p className="loading">Generating image (this may take ~17-20 minutes on CPU)...</p>}
        {image && (
          <div className="image-section">
            <img src={image} alt="Generated" className="generated-image" />
            <button onClick={downloadImage} className="download-button">
              Download Image
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;