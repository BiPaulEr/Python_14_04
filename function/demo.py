def function(name1):
    print(name1)
    name1.append("Dupont")
    print(name1)
    return "OKOKOK", "Deuxieme object"

print(function)
name1 = []
variable1, variable2 = function("OK", "OK")  
print(name1)

print("end")