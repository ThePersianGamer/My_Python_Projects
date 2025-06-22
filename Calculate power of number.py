num = int(input("Enter a number: "))
pwr = int(input("Enter a power: "))

powerOfNumber = 1
for i in range(pwr):
    powerOfNumber = num * powerOfNumber
print(powerOfNumber)