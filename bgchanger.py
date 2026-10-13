from tkinter import *
window = Tk()
window.geometry("200x200")
window.title("my first app")
window.configure(bg="blue")

def change_text():
    label1.configure(text="Hello")
    window.configure(bg="skyblue")
    label1.configure(bg="darkgreen")

label1 = Label(window, text="Welcome", bg="blue", fg="red", font=("arial", 20))
label1.pack(anchor="center")
button = Button(window, text="change text", bg="red", relief="flat", bd=0, command=change_text)
button.pack(side="bottom")





window.mainloop()