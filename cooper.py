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
   # obtain audio from the microphone
   r = sr.Recognizer()
   with sr.Microphone() as source:
      audio = r.listen(source)
   try:
      #if I say wires, grab variables and call wires logic
      if "wires" in r.recognize_google(audio):
         answer = wires(engine)
         print(answer)
         engine.say(answer)

      elif "I love you" in r.recognize_google(audio):
         print("I love you more")
         engine.say("I love you more")

      else:
         engine.say("Error. Retry.")
      engine.runAndWait()
   except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
   except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

