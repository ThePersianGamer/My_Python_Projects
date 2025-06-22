from tkinter import *
def bAaction():
    print("Thank you!")
def bBaction():
    print("Ouch! That hurt!")
window = Tk()
buttonA = Button(window, text="Press me!", command=bAaction)
buttonB = Button(window, text="Don't press!", command=bBaction)
buttonA.pack()
buttonB.pack()
mainloop()