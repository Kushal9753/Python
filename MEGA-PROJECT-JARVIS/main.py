
import speech_recognition as sr

import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "2e35e08934914ed59c5f3fce124a0f67"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtub" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            
            for article in articles:
                speak(article['title'])
                  # Get the title and add to list

            

    

if __name__ == "__main__":
  speak("Initializing jarvis......")

  
  while True:

  
      # Listen for the microphone


      # obtain audio from the microphone

      r = sr.Recognizer()
     

      
      
      # recognize speech using Sphinx
      print("recognizing...")
      try:
            with sr.Microphone() as source:
                
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "hello"):
                speak("ji")
                # Listen for command

                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

                

      except Exception as e:
          print("Error; {0}".format(e))
  
  

