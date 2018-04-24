class employee:
    ''' this class is to create employee class'''
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.emp_count += 1

    def emp_size(self):
        print employee.emp_count

    def print_name(self):
        print ("employee name: %s salary: %d" %(self.name,self.salary) )

a = employee("test1",1000)


print employee.emp_count
print a.emp_size()
print a.print_name()

b= employee("test2",2000)

print employee.emp_count
print a.emp_size()
print b.print_name()
print hasattr(a,"name")
print setattr(a,"name","test3")
print getattr(a,"name")
print delattr(a,"name")
#print a.print_name()
print employee.__doc__
