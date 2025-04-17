def pair(max, pair = True):
    depart = 0 if pair else 1
    for i in range(depart, max+1, 2):
        yield i

for i in pair(10, pair=False):
    print(i)

gen_pair = (i for i in range(0, 11, 2))
for i in gen_pair:
    print(i)