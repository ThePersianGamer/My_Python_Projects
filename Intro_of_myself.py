age = input("How old are you? ")
heightcm = input("How tall are you(in cm)? ")
name = input("What is your name? ")
print(f"Hello {name}.")
age = int(age)
heightcm = float(heightcm)
heightm = heightcm / 100
print(f"You are {heightm} meters tall!")
print(f"Hello {name}! I heard you are {age} years old and also you are {heightm} meters tall which is same with {heightcm} centimetre.")