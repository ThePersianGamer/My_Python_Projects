n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
if n1 > n2:
    if n1 > n3:
        print(f"{n1} is the biggest number.")
else:
    if n2 > n3:
        print(f"{n2} is the biggest number.")
    if n3 > n2 and n3 > n1:
        print(f"{n3} is the biggest number.")
    if n3 == n2:
        print(f"{n3} and {n2} are equal.")
    if n3 == n1:
        print(f"{n3} and {n1} are equal.")
    if n1 == n2:
        print(f"{n1} and {n2} are equal.")
