import speech_recognition as sr
import pyttsx3

# Changing voices in pyttsx3 must be SAP 5 compatible

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

memeText = "soi soi soi soi soi soi soi. e brbrbrbbrbrbr. ped ped ped ped ped ped ped 0000 0000 ha ha ha ha hahahhahhahaahhaha tce tce tce tce tce tce tce tce tce mmmmmmmmmm ttttttttt m m m m mm m mm mmm m tt t tt t t"
testText = 'Red. red. blue. yellow. red. Two. Five. Nine. Three. Mike. soi soi soi soi soi soi soi soi soi soi soi Im gonna make an earthquake e brbrbrbrbrbrbrbrbrbrbr'
engine.say(memeText)
engine.setProperty('voice', voices[1].id)
engine.say(memeText)
engine.setProperty('voice', voices[0].id)
engine.say(memeText)
engine.runAndWait()


# while True:

#     # obtain audio from the microphone
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)

#     # recognize speech using Google Speech Recognition
#     try:
#         # for testing purposes, we're just using the default API key
#         # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#         # instead of `r.recognize_google(audio)`
#         voices = engine.getProperty('voices')
#         engine.setProperty('voice', voices[0].id)
#         engine.say(r.recognize_google(audio))
#         engine.runAndWait()
#         engine.setProperty('voice', voices[1].id)
#         engine.say(r.recognize_google(audio))
#         engine.runAndWait()
#         engine.setProperty('voice', voices[2].id)
#         engine.say(r.recognize_google(audio))
#         engine.runAndWait()
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))
