import numpy as np #numpy_arrays are faster in execution and need less space than lists
import random
from datetime import datetime

def fibonacci(fibonacciSequenzPosition, fibonacciSequenz):
    
    if (type(fibonacciSequenzPosition) != int):
        return "Invalid input, pls use positive integer numbers only \n"
    if (fibonacciSequenzPosition < 0):
        return "Invalid input, pls use positive integer numbers only \n"
    
    if (fibonacciSequenzPosition == 0):
        return "Fibonacci Number for 0 is: 0 \n"
    if (fibonacciSequenzPosition == 1 or fibonacciSequenzPosition == 2):
        return "Fibonacci Number for"+str(fibonacciSequenzPosition)+" is: 1 \n"
    
    fibonacciSequenzLastIndex = fibonacciSequenz.size-1
    if (fibonacciSequenzPosition > fibonacciSequenzLastIndex):
        fibonacciSequenz = fibonacciSequenzExtender(fibonacciSequenzPosition, fibonacciSequenzLastIndex ,fibonacciSequenz)
    
    return "Fibonacci Number for "+str(fibonacciSequenzPosition)+" is: "+str(fibonacciSequenz[fibonacciSequenzPosition])+"\n" 


def fibonacciSequenzExtender(fibonacciSequenzPosition, fibonacciSequenzLastIndex ,fibonacciSequenz):
    
    while(fibonacciSequenzPosition > fibonacciSequenzLastIndex):
        fibonacciSequenzLastNumber = fibonacciSequenz[fibonacciSequenzLastIndex]
        fibonacciSequenzSecondLastNumber = fibonacciSequenz[fibonacciSequenzLastIndex-1]
        fibonacciSequenzNewNumber = fibonacciSequenzLastNumber + fibonacciSequenzSecondLastNumber
        fibonacciSequenz = np.append(fibonacciSequenz, [fibonacciSequenzNewNumber])
        fibonacciSequenzLastIndex = fibonacciSequenz.size-1
        
    return fibonacciSequenz
        

#--------------------Main -----------------------#

startTime = datetime.now()
fibonacciSequenz = np.ulonglong([0, 1, 1])

#One by One manually
#fibonacciInput = input("What position of the Fibonacci sequenz is interesting to you? \n")
#print(fibonacci(int(fibonacciInput), fibonacciSequenz))

#With random number generator
loopStart = 0
loopEnd = 523
fibonacciFirstPosition = 0 
fibonacciMaxPosition = 93 #93 Last Position before overflow

for randomNumber in range(loopStart, loopEnd):
    fibonacciSequenzPosition = random.randint(fibonacciFirstPosition, fibonacciMaxPosition)
    print(fibonacci(fibonacciSequenzPosition, fibonacciSequenz)) 

print("Execution time: " +str(datetime.now()-startTime))
