
a = ( 1,"hello",2,3,"bye")
print a[1]
print a[2]
print a[3]
print a[4]
print a[0]
print a[-1]
print a[-2]
print ("length of tupule", len(a))
print a[len(a)-1]

b = (a,"added")
print b
print b[0]
print b[0][0]
print b[0][2]

test = ("hello test")
test1 = ("hello test1",)

print test[0]
print test1[0]

print len(test)

if len(test) > 1 :
    print len(test)
