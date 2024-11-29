def check_right_triangle(sides):
    sides.sort()
    if sides[2]**2== sides[0]**2+sides[1]**2:
        return true
    return false
sides=[]
sides.append(int(input("enter the length of the first side:")))
sides.append(int(input("enter the length of the second side:")))
sides.append(int(input("enter the length of the third side:")))
if check_right_triangle(sides):
    print("it is aright triangle")
else:
    print("it is not a right triangle")