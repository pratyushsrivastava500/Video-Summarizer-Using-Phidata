
# Video Summarizer Agent 📽️

A modular Streamlit application that uses Google's Gemini AI to analyze and provide insights from uploaded videos. The app leverages the phidata framework for AI agent capabilities and includes web research functionality through DuckDuckGo.

---

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Features
- 🎥 Video upload support (MP4, MOV, AVI)
- 🤖 AI-powered video analysis using Gemini
- 🔍 Contextual web research integration
- 💬 Interactive query interface
- 📊 Detailed analysis results
- 🧩 Modular code structure for easy maintenance

---

## Project Structure
```
├── main.py                # Streamlit app entry point
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not committed)
├── src/
│   ├── __init__.py
│   ├── agent_utils.py     # Agent and Gemini configuration
│   └── video_utils.py     # Video processing utilities
└── README.md
```

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/video-summarizer-phidata.git
cd video-summarizer-phidata
```

2. **Create and activate a Conda environment:**
```bash
conda create -n agentdemo python=3.11 -y
conda activate agentdemo
```

3. **Install the required dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create a `.env` file in the project root and add your Google API key:**
```
GOOGLE_API_KEY=your_api_key_here
```

---

## Usage

1. **Start the Streamlit app:**
```bash
streamlit run main.py
```

2. **Open your web browser and navigate to the provided local URL (typically http://localhost:8501)**

3. **Upload a video file using the file uploader**

4. **Enter your query about the video content**

5. **Click "Analyze Video" to get AI-generated insights**

---

## Dependencies
- phidata
- python-dotenv
- duckduckgo-search
- streamlit
- google-generativeai

---

## Environment Variables
- `GOOGLE_API_KEY`: Your Google API key for accessing Gemini AI services

---

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## Acknowledgments
- Google Gemini AI
- Phidata Framework
- Streamlit Team

---

## 📧 Contact

For questions, suggestions, or support:

**Project Maintainer**: Pratyush Srivastava  
**Email**: pratyushsrivastava500@gmail.com  
**GitHub**: [@pratyushsrivastava500](https://github.com/pratyushsrivastava500)

---

<div align="center">
  <strong>Made with ❤️ and Python | © 2025 Pratyush Srivastava</strong>
</div>
