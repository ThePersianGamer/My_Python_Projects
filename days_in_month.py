m0nth = int(input("Enter a month (1-12): "))
if m0nth == 2:
    print("28 or 29 days")
elif m0nth in (4, 6, 9, 11):
    print("30 days")
elif m0nth in (1, 3, 5, 7, 8, 10, 12):
    print("31 days")
