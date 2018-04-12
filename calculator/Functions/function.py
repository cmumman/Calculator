'''def pizza():
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

print sum_1 '''

def fab():
    a,b = 1,1
    while 1:
        yield a
        print a,b
        a , b = b,a+b

cnt = 0
for n in fab():
    print n
    cnt += 1
    if cnt == 10:
        break

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []

for n in numbers:
    if n > 0:
     newlist.append(n)
print(newlist)
