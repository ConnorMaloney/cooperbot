import speech_recognition as sr
import pyttsx3
from wires import wires
from button import button 
from keypads import keypads

def testMode(engine):
   print("Initiating test mode.")
   engine.say("Initiating test mode. Go ahead and state utterance, I'll repeat.")
   engine.runAndWait()

   # Initiate mimic loop to test what Cooper interprets
   while True:
      r = sr.Recognizer()
      with sr.Microphone() as source:
         audio = r.listen(source)
         answer = r.recognize_google(audio)

      if "exit" in answer or "shutdown" in answer or "shut down" in answer:
         print("Exiting test mode. Returning to main.")
         engine.say("Exiting test mode. Returning to main.")
         engine.runAndWait()
         break
      else:
         print(answer)
         engine.say(answer)
         engine.runAndWait()
# TODO: Add delay for speech processing

# TODO: Initiate "Bomb Check" module that initializes all globals

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

   try:
   # Obtain audio from the microphone
      r = sr.Recognizer()
      with sr.Microphone() as source:
         audio = r.listen(source)
         answer = r.recognize_google(audio)
         print("You said:", answer)
   
      if "done" in answer:
         print("Nice! Let's keep it up.")
         engine.say("Nice! Let's keep it up.") # TODO: Add random speech
         engine.runAndWait()

      # Begin wires module logic
      if "wire" in answer or "tire" in answer:
         solution = wires(engine)
         print(solution)
         engine.say(solution)
         engine.runAndWait()

      # Begin button module logic
      if "button" in answer:
         solution = button(engine)
         print(solution)
         engine.say(solution)
         engine.runAndWait()

      # Begin keypad module logic
      if "keypad" in answer or "knee" in answer or "pee" in answer or "pad" in answer or "symbol" in answer:
         solution = keypads(engine)
         print(solution)
         engine.say(solution)
         engine.runAndWait()

      # Victory speech
      if "did it" in answer or "victory" in answer or "congrat" in answer:
         print("Another job well done. Mission accomplished, sir.")
         engine.say("Another job well done. Mission accomplished, sir.")
         engine.runAndWait()
         exit()

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

      # Test mode
      if "test" in answer or "testing" in answer or "test mode" in answer:
         testMode(engine)
      
      # Gracefully shutdown Cooper
      if "exit" in answer or "shutdown" in answer or "shut down" in answer:
         print("Shutting down. Goodbye!")
         engine.say("Shutting down. Goodbye!")
         engine.runAndWait()
         exit()

   except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
      engine.say("Sorry, could not understand you. Please repeat.")
      engine.runAndWait()
   except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))
      engine.say("Sorry, lost connection to Google.")
      engine.runAndWait()


