import speech_recognition as sr
import pyttsx3
from wires import wires
#from button import button 

# TODO: Add delay for speech processing

# Changing voices in pyttsx3 must be SAPI 5 compatible
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)
print("Cooper here. What are we solving?") # TODO: Add random speech
engine.say("Cooper here. What are we solving?")
engine.runAndWait()
# Begin game loop
while True:

   # Obtain audio from the microphone
   r = sr.Recognizer()
   with sr.Microphone() as source:
      audio = r.listen(source)
      answer = r.recognize_google(audio)
      print("You said:", answer)
   try:
      if "done" in answer:
         print("Nice! Let's keep it up.")
         engine.say("Nice! Let's keep it up.") # TODO: Add random speech
         engine.runAndWait()

      # If I say module name, grab variables and call module logic
      if "wires" in answer:
         solution = wires(engine)
         print(solution)
         engine.say(solution)
         engine.runAndWait()

      if "button" in answer:
         solution = button(engine)
         print(solution)
         engine.say(solution)
         engine.runAndWait()

      # Maria easter egg
      if "I love you" in answer:
         print("I love you more")
         engine.say("I love you more")
         engine.runAndWait()

      # Greg easter egg
      if "broke" in answer:
         print("If server working do nothing else fix server")
         engine.say("If server working do nothing else fix server")
         engine.runAndWait()
      
      if "exit" in answer or "shutdown" in answer:
         print("Shutting down. Goodbye!")
         engine.say("Shutting down. Goodbye!")
         engine.runAndWait()
         exit()
      
      engine.runAndWait()
   except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
   except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

