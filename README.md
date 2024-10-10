# JARVIS - VOICE-ACTIVATED VIRTUAL ASSISTANT

1. Developed a Voice-Activated Assistant: Built a Python-based virtual assistant using speech_recognition, pyttsx3, and gTTS for speech recognition, speech synthesis, and text-to-speech functionalities.

2. Integrated OpenAI API for Dynamic Responses: Implemented OpenAI's GPT-3 model to process user queries and provide intelligent responses, enhancing the assistant's conversational capabilities.

3. Automated Web Browsing and Music Playback: Created functions to automate web browsing (opening sites like Google, YouTube, etc.) and music playback by linking commands to web-based music libraries.

4. Implemented Real-Time News Fetching: Integrated the NewsAPI to fetch and read aloud the latest news headlines using speech synthesis, ensuring real-time updates for users.

## FEATURES

• Voice Recognition

• Utilizes the speech_recognition library to listen for and recognize voice commands.

• Activates upon detecting the wake word "Jarvis."

• Text-to-Speech

• Converts text to speech using pyttsx3 for local conversion.

• Uses gTTS (Google Text-to-Speech) and pygame for playback.

• Web Browsing.

• Opens websites like Google, Facebook, YouTube, and LinkedIn based on voice commands.

• Music Playback

• Interfaces with a musicLibrary module to play songs via web links.

• News Fetching

• Fetches and reads the latest news headlines using NewsAPI.

• OpenAI Integration

• Handles complex queries and generates responses using OpenAI's GPT-3.5-turbo.

• Acts as a general virtual assistant similar to Alexa or Google Assistant.

• Activates upon detecting the wake word "Jarvis."

• Text-to-Speech


## WORKFLOW

1. Initialization
2. Greets the user with "Initializing Jarvis...."
3. Wake Word Detection
4. Listens for the wake word "Jarvis."
5. Acknowledges activation by saying "Ya."
6. Command Processing.
7. Processes commands to determine actions such as opening a website, playing 
music, fetching news, or generating a response via OpenAI.
8. Speech Output.
9. Provides responses using speak function with either pyttsx3 or gTTS.
10. Greets the user with "Initializing Jarvis...."
11. Wake Word Detection
12. Acknowledges activation by saying "Ya."
58
13. Processes commands to determine actions such as opening a website, playing 
music, fetching news, or generating a response via OpenAI.

## LIBRARIES USED

• speech_recognition

• webbrowser

• pyttsx3

• musicLibrary

• requests

• openai

• gTTS

• pygame

• os

