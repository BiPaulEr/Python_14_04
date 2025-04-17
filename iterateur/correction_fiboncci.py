def fibo(max):
    a, b = 0, 1
    for _ in range(0, max):
        yield a
        a, b = b, a+b

gen = fibo(10)
print(list(gen))