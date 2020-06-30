import speech_recognition as sr
import pyttsx3
from wires import wires

# Changing voices in pyttsx3 must be SAPI 5 compatible
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)
while True:

   print("Listening...")
   engine.say("Listening...")
   engine.runAndWait()
   # obtain audio from the microphone
   r = sr.Recognizer()
   with sr.Microphone() as source:
      audio = r.listen(source)
      answer = r.recognize_google(audio)
      print(answer)
   try:
      #if I say wires, grab variables and call wires logic
      if "wires" in answer:
         answer = wires(engine)
         print(answer)
         engine.say(answer)

      elif "I love you" in answer:
         print("I love you more")
         engine.say("I love you more")

      elif "exit" or "quit" or "shutdown" in answer:
         print("Shutting down. Goodbye!")
         engine.say("Shutting down. Goodbye!")
         engine.runAndWait()
         exit()

      else:
         engine.say("Error. Retry.")
      engine.runAndWait()
   except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
   except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

