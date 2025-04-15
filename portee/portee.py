liste  = [1, 2, 3, 4]

def function_outer():
    x = 99
    def function():
        nonlocal x
        x = 8
        print("function", x)
    function()
    print("function_outer", x)

x = 5
function_outer()
print("global", x)