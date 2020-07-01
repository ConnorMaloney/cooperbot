import speech_recognition as sr
import pyttsx3
from random import randint
from time import sleep

# TODO: Sanitize input to grab only colour words

# wires logic function called from main with parameters, begin logic
def wires(engine):
    print("Initiating wires.")
    engine.say("Initiating wires.")
    print("What are the colours?")
    engine.say("What are the colours?")
    engine.runAndWait()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        response = r.recognize_google(audio)
    
    colours = response.split()
    print("You said:", colours)
    engine.say("Calculating...")
    engine.runAndWait()
    sleep(randint(1,4)) # Have Cooper "calculate" for a random amount of time
    
    # Number of wires determined by how many wire colours are said
    try: 
        # 3 wires:
        if len(colours) == 3: 
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
                
        # 4 wires:
        elif len(colours) == 4:
            # If there is more than one red wire...
            if colours.count("red") > 1:
                print("Is the last digit of the serial number odd?")
                engine.say("Is the last digit of the serial number odd?")
                engine.runAndWait()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    response = r.recognize_google(audio)
                # ...and the last digit of the serial number is odd, cut the last red wire.
                if "yes" in response: 
                    return "Cut the last red wire."
                # ...and the last digit of the serial number is even, cut the second wire.
                elif "no" in response:
                    return "Cut the second wire."
            # Otherwise, if the last wire is yellow and there are no red wires, cut the first wire.
            elif "yellow" in colours[3] and "red" not in colours:
                return "Cut the first wire."
            # Otherwise, if there is exactly one blue wire, cut the first wire.
            elif colours.count("blue") == 1:
                return "Cut the first wire."
            # Otherwise, if there is more than one yellow wire, cut the last wire.
            elif colours.count("yellow") > 1:
                return "Cut the last wire."
            # Otherwise, cut the second wire.
            else:
                return "Cut the second wire."

        # 5 wires:
        elif len(colours) == 5:
            # If the last wire is black...
            if "black" in colours[4]:
                print("Is the last digit of the serial number odd?")
                engine.say("Is the last digit of the serial number odd?")
                engine.runAndWait()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    response = r.recognize_google(audio)
                # ...and the last digit of the serial number is odd, cut the fourth wire.
                if "yes" in response: 
                    return "Cut the fourth wire."
                # ...and the last digit of the serial number is even, cut the first wire.
                elif "no" in response:
                    return "Cut the first wire."
            # Otherwise, if there is exactly one red wire and there is more than one yellow wire, cut the first wire.
            elif colours.count("red") == 1 and colours.count("yellow") > 1:
                return "Cut the first wire."
            # Otherwise, if there are no black wires, cut the second wire.
            elif colours.count("black") == 0:
                return "Cut the second wire."
            # Otherwise, cut the first wire.
            else:
                return "Cut the first wire."

        # 6 wires:
        elif len(colours) == 6:
            # If there are no yellow wires...
            if colours.count("yellow") == 0:
                print("Is the last digit of the serial number odd?")
                engine.say("Is the last digit of the serial number odd?")
                engine.runAndWait()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    response = r.recognize_google(audio)
                # ...and the last digit of the serial number is odd, cut the third wire.
                if "yes" in response: 
                    return "Cut the third wire."
                # ...and the last digit of the serial number is even...
                elif "no" in response:
                    # ...and if there are no red wires, cut the last wire.
                    if colours.count("red") == 0:
                        return "Cut the last wire".
                    # ...cut the fourth wire.
                    else:
                        return "Cut the fourth wire."
            # Otherwise, if there is exactly one yellow wire and there is more than one white wire, cut the fourth wire.
            elif colours.count("yellow") == 1 and colours.count("white") > 1:
                return "Cut the fourth wire."
            # Otherwise, if there are no red wires, cut the last wire.
            elif colours.count("red") == 0:
                return "Cut the last wire."
            # Otherwise, cut the fourth wire.
            else:
                return "Cut the fourth wire."
            
        # Bad input
        else: 
            return "Error, restart."
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    