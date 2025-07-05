# Rotify

Rotify is a Chrome extension + Flask backend that transforms any webpage into a Gen-Z-style brainrot TikTok. It scrapes webpage content, summarizes it using GPT, generates synced TTS using ElevenLabs, overlays the audio and word-by-word subtitles on Subway Surfers footage, and displays it inside the popup.

## Features

- One-click summarization of the active tab
- GPT-based summarization
- ElevenLabs TTS voiceover
- Subway Surfers gameplay as visual background
- Auto-generated, synced subtitles (JSON)
- Real-time caption overlay in popup

## Tech Stack

- Frontend: HTML, CSS, JavaScript (Chrome Extension)
- Backend: Flask (Python)
- AI: OpenAI GPT, ElevenLabs TTS
- Media Processing: FFmpeg
- Subtitle Format: JSON word-timed


### 1. Clone & Setup

```bash
git clone https://github.com/yourname/rotify.git
cd rotify
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Create `.env`

```
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

### 3. Run Flask Server

```bash
python app.py
```

Make sure `ffmpeg` is installed and the path is set correctly in `render.py`.

### 4. Load Chrome Extension

Go to `chrome://extensions`  
Turn on **Developer Mode**  
Click **Load Unpacked** and select the `extension` folder

