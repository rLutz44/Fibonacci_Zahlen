import numpy as np #numpy_arrays are faster in execution and need less space than lists



def fibonacci(fibonacci_sequenz_position: int, 
              fibonacci_sequenz: int) -> str:
   
    """
    | Prints Fibonacci Number
    
    """
    
    if (fibonacci_sequenz_position == 0):
        return ("Fibonacci Number for 0 is: 0 \n")
    
    if (fibonacci_sequenz_position == 1 or 
        fibonacci_sequenz_position == 2):
        return ("Fibonacci Number for" 
                + str(fibonacci_sequenz_position) 
                + " is: 1 \n")
    
    
    fibonacci_sequenz_last_index: int = (fibonacci_sequenz.size - 1)
    
    if (fibonacci_sequenz_position > 
        fibonacci_sequenz_last_index):
        
        fibonacci_sequenz = fibonacci_sequenz_extender(fibonacci_sequenz_position, 
                                                       fibonacci_sequenz_last_index, 
                                                       fibonacci_sequenz)
    
    return ("Fibonacci Number for " 
            + str(fibonacci_sequenz_position) 
            + " is: " 
            + str(fibonacci_sequenz[fibonacci_sequenz_position]) 
            + "\n") 


def fibonacci_sequenz_extender(fibonacci_sequenz_position: int, 
                               fibonacci_sequenz_last_index: int, 
                               fibonacci_sequenz: int) -> np:
    
    """
    | Extends the sequenz to the current needed Position, if Position > 3
    
    """
    
    while(fibonacci_sequenz_position  > 
          fibonacci_sequenz_last_index):
        
        fibonacci_sequenz_last_number: int = fibonacci_sequenz[fibonacci_sequenz_last_index]
        fibonacci_sequenz_second_last_number: int = fibonacci_sequenz[fibonacci_sequenz_last_index-1]
        fibonacci_sequenz_new_number: int = (fibonacci_sequenz_last_number 
                                             + fibonacci_sequenz_second_last_number) #f(n) = f(n-1) + f(n-2)
        
        fibonacci_sequenz = np.append(fibonacci_sequenz,
                                      [fibonacci_sequenz_new_number])
        fibonacci_sequenz_last_index = (fibonacci_sequenz.size-1)
        
    return fibonacci_sequenz