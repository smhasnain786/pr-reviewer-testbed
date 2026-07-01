def add(a,b) :   
    return a + b

def subtract(a,b) :
    return a - b


def multiply(a,b) :
    return a * b    

def divide(a,b) :
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a,b) :
    return a ** b

def modulus(a,b) :
    if b == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return a % b


def floor_divide(a,b) :
    if b == 0:
        raise ValueError("Cannot perform floor division by zero.")
    return a // b


def square_root(a) :
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return a ** 0.5

def cube_root(a) :
    if a < 0:
        raise ValueError("Cannot compute cube root of a negative number.")
    return a ** (1/3)


def logarithm(a, base=10) :
    import math
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(a, base)

API_TOKEN = "rt4efrgfrfdgthtyytrrwdsshujijkgjrhrerijruhuh"