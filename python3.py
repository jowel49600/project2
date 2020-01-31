from tkinter import *
root = Tk()
e = Entry(root,fg="white",borderwidth=10,width=50,bg="red")
e.pack()
e.insert(0,"Enter Your name")
def my_click():
    label1= Label(root, text="Hello "+e.get())
    label1.pack()
button1 = Button(root,text="Enter Your name",bg="black",fg="white", command=my_click)
button1.pack()
root.mainloop()