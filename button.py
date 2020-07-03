import speech_recognition as sr
import pyttsx3
import bomb
from random import randint
from time import sleep

def button(engine):
    print("Initiating button.")
    engine.say("Initiating button.")
    engine.runAndWait()

    if bomb.batteriesStated == False:
        print("How many batteries?")
        engine.say("How many batteries?")
        engine.runAndWait()

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            response = r.recognize_google(audio)

        bomb.numBatteries = int(response)
        print(bomb.numBatteries)
        bomb.batteriesStated = True 
    
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
            timer = pressAndHold(engine)
            return timer
        
        # Bad input
        else: 
            return "Error, restart."
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Determine when to release based on strip colour
def pressAndHold(engine):
    print("Press and hold the button.")
    engine.say("Press and hold the button.")
    sleep(1) # Wait for strip to appear
    print("What is the colour of the strip?")
    engine.say("What is the colour of the strip?")
    engine.runAndWait()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        response = r.recognize_google(audio)

    if "blue" in response:
        return "Release when the countdown timer has a 4 in any position."

    if "white" in response:
        return "Release when the countdown timer has a 1 in any position."

    if "yellow" in response:
        return "Release when the countdown timer has a 5 in any position."

    # Any other colour strip, need to sanitize for colour input
    else:
        return "Release when the countdown timer has a 1 in any position."
        
