def fct2():
    x = 10
    def fct1():
        nonlocal x
        print(x)
    fct1()
    print(x)

fct2()