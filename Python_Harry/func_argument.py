# default arguments

def add(a,b,plus=0):
    x = a + b + plus
    return x

c = add(3,5,2)
# print(c)


# //keywords arguments

c1 = add(b=5,a=3)
print(c1)