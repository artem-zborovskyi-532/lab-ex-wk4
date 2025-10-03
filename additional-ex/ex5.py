# Exercise 5: Vectors
    # A vector of dimension 𝑛 can be represented by a list in Python. For example, a
    # vector of dimension 3 could represent a point in space, and a vector of dimension
    # 4 could represent a point in space and time (the fourth dimension being the time).
    # In mathematical notation, a vector of dimension 3 is represented as follow:
    # [a, b, c]
    # The vector could be stored in a Python list [a, b, c]. There are two simple
    # operations that can be done on vector, and the result of the two operation is also
    # a vector. The two operations are:
    # Scalar product: 
    # l x [a, b, c] = [l * a, l * b, l * c]
    # Addition: 
    # [a, b, c] + [d, e, f] = [a + d, b + e, c + f]
    # Implement two functions:
    # 1. scalar_product(scalar, vector) where scalar is a float and vector is
    # a list of float. The function returns the scalar product of the two
    # parameters.
    # 2. vector_addition(vector1, vector2) where vector1 and vector2
    # are lists of float. The function returns the vector addition of the two
    # parameters. If vector1 and vector2 don’t have the same dimension, you
    # should print an error message and return None.

def scalar_product(scalar:float, vector:list[float]) -> list[float]:
    res = []
    for i in vector:
        res.append(scalar * i)
    return res

def same_direction(a, b):
    return a % b == 0 or b % a == 0

def vector_addition(vector1:list[float], vector2:list[float]) -> list[float]:
    if len(vector1) != len(vector2):
        print("Wrong input!")
        return
    
    res = []

    for i in range(len(vector1)):
        if same_direction(vector1[i], vector2[i]):
            res.append(vector1[i] + vector2[i])
        else:
            print("Vectors have different directions.")
            return None
        
    return res