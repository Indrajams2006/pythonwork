'''
Author:indraja m s
Date:25-10-2024
Description: Python program to convert temperature values back and forth
between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c5=f−329
'''
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if(num1>num2 and num1>num3):
    print(num1,"is the greater than the other two")
elif (num2>num3 and num2>num1):
    print(num2,"is the greater than the other two")
else:
    print(num3,"is greater than the other two")