import speech_recognition as sr
import pyttsx3
from random import randint
from time import sleep

def button(engine):
    print("Initiating button.")
    engine.say("Initiating button.")
    print("What is the colour and text?")
    engine.say("What is the colour and text?")
    engine.runAndWait()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        response = r.recognize_google(audio)

    colourText = response.split()
    print("You said:", colourText)
    engine.say("Calculating...")
    engine.runAndWait()
    sleep(randint(1,3)) # Have Cooper "calculate" for a random amount of time

    # Follow rules in order
    try: 
        # If the button is blue and the button says "Abort", hold the button and refer to "Releasing a Held Button":
        if "blue" in colourText and "abort" in colourText: 
            timer = pressAndHold()
            # If there are no red wires, cut the second wire.
            if "red" not in colours:
                return "Cut the second wire."
            # Otherwise, if the last wire is white, cut the last wire.
            elif "white" in colours[2]:
                return "Cut the last wire."
            # Otherwise, if there is more than one blue wire, cut the last blue wire.
            elif colours.count("blue") > 1:
                return "Cut the last blue wire."
            # Otherwise, cut the last wire.
            else:
                return "Cut the last wire."
        
        # Bad input
        else: 
            return "Error, restart."
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Determine when to release based on strip colour
def pressAndHold():
