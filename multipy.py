def multiply(numbers):
    total=1
    for i in numbers:
        total*=i
    print("the multiplication of numbers",total)
numbers=[]
num=int(input("enter the number of elements:"))
for i in range(num):
    n=int(input("enter the number"))
    numbers.append(n)
multiply(numbers)


