count = 0
number = input("Enter a number: ")
digit = input("Enter a digit: ")
for i in number:
    if digit == i:
        count += 1
print(count)
