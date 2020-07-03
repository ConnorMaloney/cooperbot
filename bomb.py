global serialOdd, serialStated, numBatteries, batteriesStated
serialOdd = False
serialStated = False
numBatteries = 0
batteriesStated = False 
litCAR = False
litCARstated = False
litFRK = False
litFRKstated = False

def sanitize(words):
    words = [word.replace('read','red') for word in words]
    words = [word.replace('fore','four') for word in words]
    return words
