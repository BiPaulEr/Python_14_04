
def f1():
    #1 / 0
    #raise ZeroDivisionError("division by zero")
    a = 9

try:
    f1()
except Exception as e:
    print("Mince")
else:
    print("DANS LE ELSE")
finally:
    print("DANS LE finally")

print("ok")
