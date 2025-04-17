class Simplest():
    attribut = "Choucroute"

print(Simplest) #<class '__main__.Simplest'>
print(Simplest.attribut)

simple1 = Simplest()
print(simple1) #<__main__.Simplest object at 0x0000017273B4A2D0>
print(simple1.attribut)
simple1.attribut = "Saucisse"
print(simple1.attribut)

simple2 = Simplest()
print(simple2) #<__main__.Simplest object at 0x0000017273B4A270>
print(simple2.attribut)



