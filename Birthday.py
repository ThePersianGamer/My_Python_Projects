from datetime import date

Today = date.today()

birthday = date(2025, 7, 2)

def HAVE_FUN():
    print("Have an amazing day, Artin! 🎉")

def GO_STUDY():
    print("Time to study and stay focused. 📚")

if Today == birthday:
    print("Happy Birthday Artin!")
    HAVE_FUN()

else:
    GO_STUDY()
