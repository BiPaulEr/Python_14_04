def gen():
    i = 2
    while True:
        yield i 
        i = i**2
        

for test in gen():
    print(test)

print("end")