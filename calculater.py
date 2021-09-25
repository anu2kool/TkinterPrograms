from tkinter import *
import tkinter.font as font
root=Tk()
global firstnum
global secondnum
e=Entry(root, width=50)
def click(text):
    index=len(e.get())
    e.insert(index,text)
def clear_screen():
    e.delete(0,END)
def operation(o):
    global firstnum
    global operator
    operator=o
    firstnum=float(e.get())
    print("firstnum:",firstnum)
    e.delete(0,END)
def equal():
    secondnum=float(e.get())
    print("secondnum:",secondnum)
    e.delete(0,END)
    if operator=="+":
        result=firstnum+secondnum
    elif operator=="-":
        result=firstnum-secondnum
    elif operator=="*":
        result=firstnum*secondnum
    elif operator=="/":
        result=firstnum/secondnum
    print("result:",result)
    e.insert(1,str(result))
e.grid(column=0, row=0, columnspan=3, padx=5, pady=5, ipady=5)
b7=Button(root, text="7", width=7, height=4, command=lambda: click("7"), font=font.Font(size=15))
b8=Button(root, text="8", width=7, height=4, command=lambda: click("8"), font=font.Font(size=15))
b9=Button(root, text="9", width=7, height=4, command=lambda: click("9"), font=font.Font(size=15))
b4=Button(root, text="4", width=7, height=4, command=lambda: click("4"), font=font.Font(size=15))
b5=Button(root, text="5", width=7, height=4, command=lambda: click("5"), font=font.Font(size=15))
b6=Button(root, text="6", width=7, height=4, command=lambda: click("6"), font=font.Font(size=15))
b1=Button(root, text="1", width=7, height=4, command=lambda: click("1"), font=font.Font(size=15))
b2=Button(root, text="2", width=7, height=4, command=lambda: click("2"), font=font.Font(size=15))
b3=Button(root, text="3", width=7, height=4, command=lambda: click("3"), font=font.Font(size=15))
b_add=Button(root, text="+", width=7, height=4, command=lambda: operation("+"), font=font.Font(size=15))
b_multiply=Button(root, text="*", width=7, height=4, command=lambda: operation("*"), font=font.Font(size=15))
b_subtract=Button(root, text="-", width=7, height=4, command=lambda: operation("-"), font=font.Font(size=15))
b_division=Button(root, text="/", width=7, height=4, command=lambda: operation("/"), font=font.Font(size=15))
b_equal=Button(root, text="=", width=7, height=4, command=equal, font=font.Font(size=15))
b_clear=Button(root, text="clear", width=7, height=4, command=clear_screen, font=font.Font(size=15))
b7.grid(row=1, column=0, padx=3)
b8.grid(row=1, column=1, padx=3)
b9.grid(row=1, column=2, padx=3)
b4.grid(row=2, column=0, padx=3)
b5.grid(row=2, column=1, padx=3)
b6.grid(row=2, column=2, padx=3)
b1.grid(row=3, column=0, padx=3)
b2.grid(row=3, column=1, padx=3)
b3.grid(row=3, column=2, padx=3)
b_add.grid(row=4, column=0, padx=3)
b_equal.grid(row=4, column=1, columnspan=2, padx=3, ipadx=60)
b_multiply.grid(row=5, column=0, padx=3, ipadx=8)
b_subtract.grid(row=5, column=1, padx=3, ipadx=8)
b_division.grid(row=5, column=2, padx=3, ipadx=8, ipady=0)
b_clear.grid(row=6, column=0, columnspan=3, ipadx=120, ipady=0)
root.mainloop()