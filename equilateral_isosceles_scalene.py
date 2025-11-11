from traceback import print_tb

side_1 = int(input("Side one: "))
side_2 = int(input("Side two: "))
side_3 = int(input("Side three: "))
if side_1 == side_2 and side_1 == side_3:
    print("Equilateral.")
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("Isosceles.")
else:
    print("Scalene.")
