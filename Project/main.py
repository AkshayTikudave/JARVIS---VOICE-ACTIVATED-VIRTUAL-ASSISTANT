import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import cv2
import subprocess






recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "ae7df6fe4d16493a870b6ba63fc5df77"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 
    
def aiProcess(command):
    client = OpenAI(
        api_key = "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"
        )


    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content
    
    
def processCommand(c):
    
    # Open websites
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://twitter.com")
        
    # Play Songs
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
        
    # Open applications
    elif "open notepad" in command:
        subprocess.Popen("notepad.exe")  # For Windows
    elif "open calculator" in command:
        subprocess.Popen("calc.exe")     # For Windows
    elif "open command prompt" in command or "open cmd" in command:
        subprocess.Popen("cmd.exe")      # For Windows
    elif "open camera" in command:
        cap = cv2.VideoCapture(0)  # Open the default camera (0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Camera', frame)
            
            # Press 'q' to close the camera window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
    # Open News   
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
                
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)
    
        


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "jarvis"
        r = sr.Recognizer()
             
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2,phrase_time_limit=1)    
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                        
        except Exception as e:
            print("Error; {0}".format(e))
        




