'''
Author:indraja m s
Date:25-10-2024
Description:
Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c5=f−32/9
'''
temperature=int(input("enter the temperature"))
scale=input("is this in(c)celsius or (F)ahrenheit?")
if scale=="C":
    temp1=(9/5*temperature)+32
    print(temperature,"celsius is",temp1,"fahrenheit")
else:
    temp2=5/9*(temperature-32)
    print(temperature,"fahrenheit is",temp2,"celsius" )
