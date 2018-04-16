# lambda, reduce,  map usage
import sys
filter_me = [1,2,3,4,5,6,7,8,12,15,18]

result = filter(lambda x : (x%2 == 0 and x%3 == 0) , filter_me)

print result

reduce_me = [1,2,3,4]
result =  reduce(lambda x,y: x+y, reduce_me)
print result


map_me = [1,1,2,3,4,5,6]
result = map(lambda x: x/2, map_me)
result_1 = map(lambda x: x+5,map_me)
print result
print result_1

map_me_again = [[1,2,3],[4,5,6],[7,8,9]]

result = map(lambda a : (a[2],a[1],a[0]),map_me_again)

print result

print [x for x in map_me if x%2]

x = xrange(1,10)
y = range(1,10)
print x,y

print x[1]