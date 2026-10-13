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
label.pack(anchor="center")
button = Button(window, text="red", font=("arial", 55), command=red)
button.pack(anchor="center",)
button2 = Button(window, text="yellow", font=("arial", 55), command=yellow)
button2.pack(anchor="center")
button3 = Button(window, text="green", font=("arial", 55), command=green)
button3.pack(anchor="center")

window.mainloop()