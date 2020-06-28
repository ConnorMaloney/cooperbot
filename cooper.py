import speech_recognition as sr
import pyttsx3

# Changing voices in pyttsx3 must be SAPI 5 compatible
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)

engine.say("Greetings, Cooper here. Go ahead and talk.")
engine.runAndWait()

while True:

   # obtain audio from the microphone
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening...")
      audio = r.listen(source)

   # recognize speech using Google Speech Recognition
   try:
      # for testing purposes, we're just using the default API key
      # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
      # instead of `r.recognize_google(audio)`
      if "hello" in r.recognize_google(audio):
         engine.say("your sentence had hello")

      else:
         engine.say("i didnt hear you say hello")
      engine.runAndWait()
   except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
   except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))
