def mobile_number():
   n=input("Enter  a mobile number :")
   if len(n)==10 and n[0] in "7,8,9":
     print("The mobile number is valid")
   else:
     print("The mobile number is not valid")
mobile_number()
