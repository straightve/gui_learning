import tkinter
root = tkinter.Tk()

button1 = tkinter.Button(root)
button1.config(text="cake",
               font=("Wingdings", "50"),
               command=print("the cake is a lie"))
button1.grid()

root.mainloop()
