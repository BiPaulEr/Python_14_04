import time
from random import randint

def cache(function):
    dictionnaire = {}
    def wrapper(*args):
        if args in dictionnaire:
            print("Cached")
            return dictionnaire[args]          
        result = function(*args)
        dictionnaire[args]  = result
        print(dictionnaire)
        return result    
    return wrapper

@cache
def function_lente(a, b):
    sleep = randint(1, 5)
    print(f"function_lente sleep for {sleep}")
    time.sleep(sleep)
    return a + b

@cache
def function_lente2(a):
    sleep = randint(1, 5)
    print(f"function_lente sleep for {sleep}")
    time.sleep(sleep)
    return a

print(function_lente(3, 6))

print(function_lente(-89, 6))

print(function_lente(3, 6))

print(function_lente(-89, 6))

print(function_lente2("A"))

print(function_lente2("B"))

print(function_lente2("A"))

print(function_lente2("B"))