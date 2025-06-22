s1 = int(input("Enter the first score between 0-100: "))
s2 = int(input("Enter the first score between 0-100: "))

if s1 > -1 and s1 < 101 and s2 > -1 and s2 < 101:
    addition = s1 + s2
    avg = addition / 2
    if avg > 89:
        print("Your average is A.")
    if avg > 79 and avg < 90:
        print("Your average is B.")
    if avg > 69 and avg < 80:
        print("Your average is C.")
    if avg > 59 and avg < 70:
        print("Your average is D.")
    if avg < 60:
        print("Your average is F.")
else:
    print("Invalid scores.")
