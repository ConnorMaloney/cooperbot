import speech_recognition as sr
import pyttsx3
import bomb
from random import randint
from time import sleep

# TODO: This needs to be fixed, Cooper is not understanding  

# Define literal definitions for symbols
c1 = ["lollipop", "mountain", "nowton", "lambda", "z", "zulu", "triangle", "h", "hotel", "crescent"]
c2 = ["e", "echo", "eyes", "ice", "lollipop", "crescent", "cursive", "star", "h", "hotel", "question"]
c3 = ["copyright", "copy right", "boobs", "cleavage", "cursive", "mirror", "three", "3", "lambda", "star"]
c4 = ["g", "golf", "gulf", "music", "down", "triangle", "mirror", "question", "smile", "philly", "smiley", "miley", "tongue"]
c5 = ["trident", "smile", "philly", "smiley", "miley", "tongue", "down", "crescent", "music", "dragon", "star"]
c6 = ["g", "golf", "gulf", "e", "echo", "eyes", "ice", "road", "cross", "joined", "a", "alpha", "trident", "psy", "halo", "n", "november", "omega"]
columns = [c1, c2, c3, c4, c5, c6]
numColumns = 6

def keypads(engine):
    print("Initiating keypads.")
    engine.say("Initiating key pads.")
    engine.runAndWait()

    try:
        print("What are the symbols from left to right?")
        engine.say("What are the symbols from left to right?")
        engine.runAndWait()

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            response = r.recognize_google(audio)

        # Abort
        if "cancel" in response:
            return "Exiting, returning to main."
        
        symbols = response.split()
        symbols = [x.lower() for x in symbols] # Convert every symbol to lowercase for easy comparison to column data
        correctColumn = 0 
        orderedSymbols = {}

        for i in range(numColumns):
            validWords = 0
            for j in range(len(columns[i])):
                if columns[i][j] in symbols:
                    validWords+=1
            if validWords >= 4:
                correctColumn = i

        for i in range(len(symbols)): # Iterate over symbols
            valueCounter = 0
            for j in range(len(columns[correctColumn])): # Iterate over correct column
                if symbols[i] == columns[correctColumn][j]: # If words match
                    orderedSymbols[symbols[i]] = valueCounter # Append to dictionary
                else:
                    valueCounter+=1

        orderedSymbols = {k: v for k, v in sorted(orderedSymbols.items(), key=lambda item: item[1])} # Sort symbol dictionary by values 
        return str(orderedSymbols.keys())[11:-2]

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        

    