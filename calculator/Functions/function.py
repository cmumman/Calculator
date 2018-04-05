def pizza():
    """this functions refers ingrediants of pizza"""
    recip = ['bread','onion']
    print recip
    return recip

recip = ['tamoto','garlic']
pizza()
print recip
print "%s"%pizza.__doc__
print dir(pizza)

def add_1(x,y):
    for para in (x,y):
        if (type(para) != type(1)):
            raise TypeError, "enter a integer"
    a = x + y
    return (a)

sum_1 = add_1(3, "a")

print sum_1
