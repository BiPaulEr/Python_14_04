def minimum(arg1, arg2, *args):
    minimum_result = arg1
    if arg2 < arg1:
        minimum_result = arg2 
    if not args:
        return minimum_result
    for element in args:
        if element < minimum_result:
            minimum_result = element
    return minimum_result

tuple_test = (1, 2, 3, 4, 5, 6, -13)
print(minimum(*tuple_test))
print(minimum(1, 2, 3, 4, 5, 6, -13))

def fct(arg1 = "OK", **kwargs):
    print(arg1, kwargs) 

dictionnaire = {"arg1" : "QUOI0", "arg2" : "QUOI2", "arg3" : "QUOI3", "arg4" : "QUOI4"}
fct(dictionnaire)

fct(arg1 = "QUOI0", arg2 = "QUOI2", arg3 = "QUOI3", arg4 = "QUOI4")
fct(**dictionnaire)



