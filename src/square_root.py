import math 

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of -ve numbers")
    return math.sqrt(x)