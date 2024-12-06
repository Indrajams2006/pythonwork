'''
Authour:Indraja M S
Date:6-12-2024
Description:Program to define a module to find Fibonacci Numbers and import the module to another program.
'''

import fibonacci
from fibonacci import Fibonacci_number
num=int(input("Enter a number:"))
print(Fibonacci_number(num))