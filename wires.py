import speech_recognition as sr
import pyttsx3

# wires logic function called from main with parameters, begin logic
def wires(engine):
    print("Initiating wires.")
    engine.say("Initiating wires.")
    engine.runAndWait()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        response = r.recognize_google(audio)
        print(response)
    
    engine.say("Calculating...")
    engine.runAndWait()
    
    try: 
        if len(response.split()) == 3:
            return "Three wires."
        elif len(response.split()) == 4:
            return "Four wires."
        else: 
            return "Error, restart."
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    