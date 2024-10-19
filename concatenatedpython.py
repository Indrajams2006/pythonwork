'''
Author:indraja m s
Date:19-10-24
Description:Python program that performs Create, concatenate, and print a string and access a sub-string from a given string.
'''
first_name=input("enter your first name")
last_name=input("enter your last name")
name=first_name+" "+last_name
print(name)
first_name_length=len(first_name)
last_name_length=len(first_name)
print(first_name_length)
extracted_first_name=name[:first_name_length]
print(extracted_first_name)

