from tkinter import *
window = Tk()
window.title("temperature converter")
window.geometry("800x800")
window.configure(bg= "skyblue")

def c_to_f():
    c = int(entry.get())
    calc = c * 1.8 + 32
    label2.configure(text= calc)

label = Label(window, text= "Temperature Converter", bg= "skyblue", fg= "black", font= ("bold", 40))
label.place(x= 200, y= 0)
label1 = Label(window, text= "Temperature in degree Celsius.", bg= "skyblue", fg= "black", font= ("bold", 16))
label1.place(x= 150, y= 300)
entry = Entry(window, width= 10)
entry.place(x= 275, y= 325)
label2 = Label(window, text= "Degree Farenheit", bg= "skyblue", fg= "black", font= ("bold", 16))
label2.place(x= 450, y= 325)
button = Button(window, text= "convert", font= ("boldd", 16), command= c_to_f)
button.place(x= 350, y= 375)

window.mainloop()