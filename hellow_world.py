import tkinter

root = tkinter.Tk()

root.title("First app!!")
root.geometry("800x600")

my_label = tkinter.Label(root)
my_label.config(text="Hello!", fg="green")
my_label.grid()

root.mainloop()
