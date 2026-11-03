from tkinter import *
window = Tk()
window.geometry("800x800")
window.title("Colours")
window.configure(bg="white")

def red():
    label.configure(text="STOP", bg="red")
    window.configure(bg="red")
def yellow():
    label.configure(text="GO SLOW", bg="yellow")
    window.configure(bg="yellow")
def green():
    label.configure(text="GO", bg="green")
    window.configure(bg="green")
    

label = Label(window, text="Colours", bg="white", fg="black", font=("bold", 50))
label.place(x= 300, y= 0)
button = Button(window, text="red", font=("arial", 55), command=red)
button.place(x=0, y=375)
button2 = Button(window, text="yellow", font=("arial", 55), command=yellow)
button2.place(x= 250, y= 375)
button3 = Button(window, text="green", font=("arial", 55), command=green)
button3.place(x= 600, y= 375)

window.mainloop()