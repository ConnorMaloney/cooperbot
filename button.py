import speech_recognition as sr
import pyttsx3
import bomb
from random import randint
from time import sleep


# On the Subject of The Button

# You might think that a button telling you to press it is pretty straightforward.
# That's the kind of thinking that gets people exploded.
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

        # Cooper may interpret response as numerical value or literal value (e.g. three or 3), hence conversion
        response = str(bomb.sanitize(response))[2:-2] # Remove brackets and apostraphes
        bomb.numBatteries = int(response)
        print(bomb.numBatteries)
        bomb.batteriesStated = True 

    # TODO: These can be more efficient
    if bomb.litCARstated == False:
        print("Is there a lit indicator with label CAR?")
        engine.say("Is there a lit indicator with label CAR?")
        engine.runAndWait()

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            response = r.recognize_google(audio)

        if "yes" in response:
            bomb.litCAR = True
            bomb.litCARstated = True
        elif "no" in response:
            bomb.litCARstated = True

    if bomb.litFRKstated == False:
        print("Is there a lit indicator with label FRK?")
        engine.say("Is there a lit indicator with label FRK?")
        engine.runAndWait()

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            response = r.recognize_google(audio)

        if "yes" in response:
            bomb.litFRK = True
            bomb.litFRKstated = True
        elif "no" in response:
            bomb.litFRKstated = True

    
    
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

    # Follow these rules in the order they are listed. Perform the first action that applies:
    try: 
        # 1. If the button is blue and the button says "Abort", hold the button and refer to "Releasing a Held Button".
        if "blue" in colourText and "abort" in colourText: 
            timer = pressAndHold(engine)
            return timer

        # 2. If there is more than 1 battery on the bomb and the button says "Detonate", press and immediately release the button.
        if bomb.numBatteries > 1 and "detonate" in colourText:
            return "Press and immediately release the button."

        # 3. If the button is white and there is a lit indicator with label CAR, hold the button and refer to "Releasing a Held Button". 
        if "white" in colourText and bomb.litCAR == True:
            timer = pressAndHold(engine)
            return timer

        # 4. If there are more than 2 batteries on the bomb and there is a lit indicator with label FRK, press and immediately release the button. 
        if bomb.numBatteries > 2 and bomb.litFRK == True:
            return "Press and immediately release the button."

        # 5. If the button is yellow, hold the button and refer to "Releasing a Held Button."
        if "yellow" in colourText:
            timer = pressAndHold(engine)
            return timer

        # 6. If the button is red and the button says "Hold", press and immediately release the button.
        if "red" in colourText and "hold" in colourText:
            return "Press and immediately release the button."
        
        # 7. If none of the above apply, hold the button and refer to "Releasing a Held Button".
        else:
            timer = pressAndHold(engine)
            return timer
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Releasing a Held Button

# If you start holding the button down, a colored strip will light up on the right side of the module.
# Based on its color, you must release the button at a specific point in time:
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

    # Blue strip: release when the countdown timer has a 4 in any position.
    if "blue" in response:
        return "Release when the countdown timer has a 4 in any position."

    # White strip: release when the countdown timer has a 1 in any position.
    if "white" in response:
        return "Release when the countdown timer has a 1 in any position."

    # Yellow strip: release when the countdown timer has a 5 in any position.
    if "yellow" in response:
        return "Release when the countdown timer has a 5 in any position."

    # Any other color strip: release when the countdown timer has a 1 in any position.
    else:
        return "Release when the countdown timer has a 1 in any position."
        
