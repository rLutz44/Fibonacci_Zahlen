import numpy as np #numpy_arrays are faster in execution and need less space than lists

import random

from datetime import datetime

from fibonacci_calculator import fibonacci



if (__name__ == "__main__"):
    
    start_time = datetime.now()
    fibonacci_sequenz = np.ulonglong([0, 1, 1]) #ulonglong = 64 bit int array in numpy
    
    loop_start: int = 0
    loop_end: int = 523
    fibonacci_first_position: int = 0 
    fibonacci_max_position: int = 93         #93 Last Position before overflow
    
    for random_number in range(loop_start, loop_end):
        fibonacci_random_sequenz_position: int = random.randint(fibonacci_first_position,
                                                                fibonacci_max_position)
        print(fibonacci(fibonacci_random_sequenz_position, 
                        fibonacci_sequenz)) 
    
    print("Execution time: " +str(datetime.now()-start_time))
