import numpy as np #numpy_arrays are faster in execution and need less space than lists
import random
from datetime import datetime

def fibonacci(fibonacci_sequenz_position: int, fibonacci_sequenz: int) -> str:
    """
    | Prints Fibonacci Number
    
    """
    if (type(fibonacci_sequenz_position) != int):
        return "Invalid input, pls use positive integer numbers only \n"
    
    if (fibonacci_sequenz_position < 0):
        return "Invalid input, pls use positive integer numbers only \n"
    
    if (fibonacci_sequenz_position == 0):
        return "Fibonacci Number for 0 is: 0 \n"
    
    if (fibonacci_sequenz_position == 1 or fibonacci_sequenz_position == 2):
        return "Fibonacci Number for"+str(fibonacci_sequenz_position)+" is: 1 \n"
    
    fibonacci_sequenz_last_index: int = fibonacci_sequenz.size-1
    if (fibonacci_sequenz_position > fibonacci_sequenz_last_index):
        fibonacci_sequenz = fibonacci_sequenz_extender(fibonacci_sequenz_position, fibonacci_sequenz_last_index, fibonacci_sequenz)
    
    return "Fibonacci Number for "+str(fibonacci_sequenz_position)+" is: "+str(fibonacci_sequenz[fibonacci_sequenz_position])+"\n" 


def fibonacci_sequenz_extender(fibonacci_sequenz_position: int, fibonacci_sequenz_last_index: int, fibonacci_sequenz: int) -> np:
    """
    | Extends the sequenz to the current needed Position, if Position > 3
    
    """
    while(fibonacci_sequenz_position > fibonacci_sequenz_last_index):
        fibonacci_sequenzLastNumber: int         = fibonacci_sequenz[fibonacci_sequenz_last_index]
        fibonacci_sequenzSecondLastNumber: int   = fibonacci_sequenz[fibonacci_sequenz_last_index-1]
        fibonacci_sequenzNewNumber: int          = fibonacci_sequenzLastNumber + fibonacci_sequenzSecondLastNumber
        fibonacci_sequenz                        = np.append(fibonacci_sequenz, [fibonacci_sequenzNewNumber])
        fibonacci_sequenz_last_index             = fibonacci_sequenz.size-1
        
    return fibonacci_sequenz
        

#--------------------Main -----------------------#

if (__name__ == "__main__"):
    
    start_time                      = datetime.now()
    fibonacci_sequenz               = np.ulonglong([0, 1, 1])
    
    #With random number generator
    loop_start: int                 = 0
    loop_end: int                   = 523
    fibonacci_first_position: int   = 0 
    fibonacci_max_position: int     = 93 #93 Last Position before overflow
    
    for random_number in range(loop_start, loop_end):
        fibonacci_sequenz_position: int = random.randint(fibonacci_first_position, fibonacci_max_position)
        print(fibonacci(fibonacci_sequenz_position, fibonacci_sequenz)) 
    
    print("Execution time: " +str(datetime.now()-start_time))
