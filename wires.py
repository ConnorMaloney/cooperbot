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
    
    colours = response.split()
    print("You said:", colours)
    engine.say("Calculating...")
    engine.runAndWait()
    
    # Number of wires determined by how many wire colours are said
    try: 
        # 3 Wires:
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
        elif len(colours) == 4:
            return "Four wires."
        elif len(colours) == 5: 
            return "Five wires."
        elif len(colours) == 6:
            return "Six wires."
        else: 
            return "Error, restart."
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    