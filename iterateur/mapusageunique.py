liste = ["A", "B", "C", "D"]

gen = map(lambda x :x.lower(), liste)
liste = list(gen)

for i in gen:
    print(i)

for i in gen:
    print(i)
