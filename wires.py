import speech_recognition as sr
import pyttsx3

# wires logic function called from main with parameters, begin logic
def wires(engine):
    engine.say("Initiating wires.")
    engine.say("How many?")
    engine.runAndWait()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Getting number of wires...")
        numWires = r.listen(source)
    try: 
        if "3" in r.recognize_google(numWires):
            return "Cut the red wire."
        elif "4" in r.recognize_google(numWires):
            return "Cut the last wire."
        else: 
            return "Error, restart."
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    