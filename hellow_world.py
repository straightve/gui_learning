import tkinter

root = tkinter.Tk()

root.title("First app!!")
root.geometry("800x600")

my_label = tkinter.Label(root)
my_label.config(text="Hello!", fg="green")
my_label.grid()

my_label2 = tkinter.Label(root)
my_label2.config(text="hey there!", fg="blue")
my_label2.grid()

my_label3 = tkinter.Label(root)
my_label3.config(text="hey you", fg="purple")
my_label3.grid()

root.mainloop()
