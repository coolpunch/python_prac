from tkinter import *

"""
this will create a new GUI window with a hello to display
root = Tk()
thelabel = Label(root, text="hello")
thelabel.pack()
root.mainloop()
"""
"""
root = Tk()

topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

b1 = Button(topframe,text="click me",fg="red")
b2 = Button(topframe,text="click me",fg="blue")
b1.pack(side= LEFT)
b2.pack()
root.mainloop() 
"""

"""
root = Tk()

one = Label(root,text="hello",bg="red",fg="black")
one.pack(side=LEFT,fill=Y)


root.mainloop()

"""
"""
root = Tk()

lbl1 = Label(root,text="name")
lbl2  = Label(root , text="password")
entr1 = Entry(root)
entr2 = Entry(root)

lbl2.grid(row=3)
entr1.grid(row=1,column=1)
entr2.grid(row=3,column=1)
lbl1.grid(row =1,sticky=E)
c= Checkbutton(root,text = "signed in ")
c.grid(columnspan = 1)



root.mainloop()
"""
"""
root = Tk()

def print_name(event):
    print("this is the first GUI that iam making")

b1 = Button(root ,text="print a random text")
b1.bind('<Button-1>',print_name)
b1.pack()
root.mainloop()
"""
root = Tk()
def left_click(event):
    print("i just pressed the left click")
def middle_click(event):
    print("i just clicked the middle button")
def right_click(event):
    print("i just clicked the right click")

frame =  Frame(root,width=300,height=300)
frame.bind('<Button-1>',left_click)
frame.bind('<Button-2>',middle_click)
frame.bind('<Button-3>',right_click)
frame.pack()
root.mainloop()

