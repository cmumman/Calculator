test_list = [ 1,2,"hi"]

print test_list[1]

test_list[1] = "hi"

print test_list

test_list.append("hello")

print test_list

test_list.extend(["vardhan", "reddy"])

#test_list.insert("rename")

print test_list

test_list1 = ["one", "two"]

test_list1.append(test_list)

test_list1.append("three")

print test_list1

print test_list1[2][2][1]
test_list3 = []

test_list3.extend(test_list)

print test_list3

dairy_section = ["milk","Ghee","Curd","Yogart"]
print dairy_section
print dairy_section[0] +  dairy_section[3]

month = 12
date = 10
year = 2005
milk_exipiration  = (month,date,year)

print  milk_exipiration[1]
print ("milk carton will expires on %d/%d/%d" %(milk_exipiration[0], milk_exipiration[1], milk_exipiration[2]))

milk_carton = {"expiration_date":milk_exipiration , "fl_oz": 1, "cost": 2 ,"brand_name": "test"}

print milk_carton["expiration_date"]

cost = 6*milk_carton["cost"]

print  ("six cartopn of milk cost is %d" %cost)
cheese = ["cotton","light","freeze"]
dairy_section.append(cheese)
print dairy_section
dairy_section.remove(cheese)
print dairy_section
dairy_section.extend(cheese)
print dairy_section
dairy_section.remove(cheese)
print dairy_section