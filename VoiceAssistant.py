import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

def recognize():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
  try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    print("You said: ",text)
    return text.lower()
  except sr.UnknownValueError:
    speak("Sorry, i didn't catch that. Could you repeat?")
  except sr.RequestError:
    speak("Sorry, but their is some problemes. Could you try again")  

def main():
  speak("Hello how can i assist you today?")
  while True:
    command = recognize()
    if command:
      if "hello" in command or "hi" in command:
        speak("Hello how can i assist you today?")
      elif "how are you" in command:
        speak("I am just a robot")   
      elif "exit" in command or "stop" in command:
        speak("Goodbey")
        break  
      else:
        speak("Somthing went wrong.")   

if __name__ == "__main__":
  main()        