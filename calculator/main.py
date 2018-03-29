# this is main code for calculator

#enter two inputs

from calculator.Functions import *

#import calculator.Functions.Sub as f1

def main():

 input1 = input("Enter first number:")

 input2 = input("Enter second number:")

 #input3 = raw_input("enter ADDI/SUB/MUX/DIVI:")

 output1 = Add.add(input1,input2)

 output2 = Sub.sub(input1,input2)

 var1 = "sum of"
 var2 = "and"
 var3 = "is"
 var4 = "sub of"
 print (var1, input1, var2, input2, var3, output1)
 print (var4, input1, var2, input2, var3, output2)

main()
