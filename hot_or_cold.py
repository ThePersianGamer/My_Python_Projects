temp = int(input("What is the temperature (celsius)? "))
if temp <= 0:
    print("Freezing!")
elif temp >= 0 and temp <= 30:
    print("Normal.")
else:
    print("Hot!")
