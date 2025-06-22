n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
if n1 > n2 and n1 > n3:
    print(f"{n1} is the biggest number.")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is the biggest number.")
elif n3 > n1 and n3 > n2:
    print(f"{n3} is the biggest number.")
elif n3 == n1:
    print(f"{n3} and {n1} are the same.")
elif n3 == n2:
    print(f"{n3} and {n2} are the same.")
elif n2 == n1:
    print(f"{n2} and {n1} are the same.")
else:
    print(f"{n1}, {n2} and {n3} are the same.")
