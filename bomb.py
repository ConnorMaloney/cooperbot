global serialOdd, serialStated, numBatteries, batteriesStated
serialOdd = False
serialStated = False
numBatteries = 0
batteriesStated = False 

def sanitize(words):
    words = [word.replace('read','red') for word in words]
    return words
