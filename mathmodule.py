'''
Author:indraja m s
Date:18-10-2024
Description:a Python program that uses functions from the math module to perform the following operations on a number provided by the user:
'''
import math
number=int(input("Enter a number:"))
square_root=math.sqrt(number)
print("square root of ",number,":",square_root)
factorial=math.factorial(number)
print("factorial of",number,":",factorial)
number2=int(input("Enter a number:"))
power=math.pow(number,number2)
print(number,"raised to power 3",":",power)
