import socket
apple = ["fuji", "gold"]

print apple

apple_new = ["local", "hybrid"]

print apple != apple_new

print "a" > "A"

print "A" > "1000"
i=1
while i < 10:
    print ("hello i am in loop %d" %i)
    i = i+1


for each in apple:
    print each


#s= socket.socket
print socket.gethostname()
print host