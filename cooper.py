import speech_recognition as sr
import pyttsx3
from wires import wires

# TODO: Add delay for speech processing

# Changing voices in pyttsx3 must be SAPI 5 compatible
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)
print("Cooper here.")
engine.say("Cooper here.")
engine.runAndWait()
# Begin game loop
while True:
   print("What are we solving?") # TODO: Add random speech
   engine.say("What are we solving?")
   engine.runAndWait()
   # obtain audio from the microphone
   r = sr.Recognizer()
   with sr.Microphone() as source:
      audio = r.listen(source)
      answer = r.recognize_google(audio)
      print("You said:", answer)
   try:
      #if I say wires, grab variables and call wires logic
      if "wires" in answer:
         answer = wires(engine)
         print(answer)
         engine.say(answer)

      elif "I love you" in answer:
         print("I love you more")
         engine.say("I love you more")

      elif "broke" in answer:
         print("If server working do nothing else fix server")
         engine.say("If server working do nothing else fix server")
      
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

