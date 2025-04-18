class RequestBadType(Exception):
    pass
class RequestBadServer(Exception):
    pass


try:
    raise FloatingPointError("")
except ZeroDivisionError as e:
    print(f"{e}")
except ArithmeticError as e:
    print(f"{e}")
except Exception as e:
    print(f"{e}")