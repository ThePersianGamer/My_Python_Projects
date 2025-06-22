side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

side12 = side1 + side2
side23 = side2 + side3
side13 = side1 + side3

if side12 > side3 or side13 > side2 or side23 > side1:
    print("The sides form a triangle.")
else:
    print("The sides do not form a triangle.")
