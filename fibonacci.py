'''
Authour:Indraja M S
Date:6-12-2024
Description:Program to define a module to find Fibonacci Numbers and import the module to another program.
'''

def Fibonacci_number (num):
    list=[]
    num1=0
    num2=1
    for i in range(num):
        list.append(num1)
        num1,num2=num2,num1+num2
    return(list)