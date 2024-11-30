def sum(numbers):
    total=0
    for i in numbers:
      total+=i
    print("the sum of the numbers is ",total)
numbers=[]
num=int(input("enter the number of elements:"))
for i in range(num):
    n=int(input("Enter the number:"))
    numbers.append(n)
sum(numbers)


