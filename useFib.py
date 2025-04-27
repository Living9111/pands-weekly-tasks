import logging
import myfunctions

#logging.basicConfig(level=logging.DEBUG)

nTimes = int(input('how many:'))
print(myfunctions.fibonacci(nTimes))

def fibonacci(number):
    if number == 0:
     return []
    if number < 0:
     raise ValueError('number must be > 0')

    a = 0
    b = 1
    fibonacciSequence = [0]
    
    # Generate the Fibonacci sequence
    for i in range(1, number):
        fibonacciSequence.append(b)

        a, b = b, a + b
    
    logging.debug("%d: %s", number, fibonacciSequence)

    

