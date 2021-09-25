import tkinter as tk
play=tk.Tk()
def on_click(grade_num):
    new_win=tk.Tk()
    new_win.title('Topics')
    new_win.geometry('800x600')
    text="Learn and Study "
    l=tk.Label(master=new_win, text="Learn and Study ", font='arial 20 bold')
    l.grid(row=0, column=0)
    if grade_num==1:
        l.config(text=text)
        head_l=tk.Label(master=new_win, text="EVS for Grade: 1", font='Times 18 bold italic')
        head_l.grid(row=1, column=0)
    if grade_num==2:
        l.config(text=text)
        head_l=tk.Label(master=new_win, text="EVS for Grade: 2", font='Times 18 bold italic')
        head_l.grid(row=1, column=0)
    if grade_num==3:
        l.config(text=text)
        head_l=tk.Label(master=new_win, text="Science for Grade: 3", font='Times 18 bold italic')
        head_l.grid(row=1, column=0)
    if grade_num==4:
        l.config(text=text)
        head_l=tk.Label(master=new_win, text="Science for Grade: 4", font='Times 18 bold italic')
        head_l.grid(row=1, column=0)
    new_win.mainloop()
play.geometry('800x600')
play.title('kittu')
heading=tk.Label(master=play, text="Universal Science", font='Arial 28 bold italic underline', fg="black", bg="blue")
heading.grid(row=0, column=0, padx=(150,130))
line1=tk.Label(master=play, text="Science is a practical subject", font='verdana 15 bold')
line1.grid(row=1, column=0, padx=(180,130))
line2=tk.Label(master=play, text="Where we learn about the EARTH,", font='verdana 15 bold')
line2.grid(row=2, column=0, padx=(180,130))
line3=tk.Label(master=play, text=" about the nature, ", font='verdana 15 bold')
line3.grid(row=3, column=0, padx=(180,130))
line4=tk.Label(master=play, text=" about the animals and humans, ", font='verdana 15 bold')
line4.grid(row=4, column=0, padx=(180,130))
line5=tk.Label(master=play, text=" about the UNIVERSE. ", font='verdana 15 bold')
line5.grid(row=5, column=0, padx=(180,130))
line6=tk.Label(master=play, text=" what is your grade? ", font='verdana 20 bold')
line6.grid(row=6, column=0, padx=(100,380), pady=(30,0))
button1=tk.Button(master=play, text="Grade 1", command=lambda: on_click(1), font='verdana 20 bold italic', relief=tk.RAISED, bg='brown', fg='white')
button1.grid(row=7, column=0, padx=(0,420))
button2=tk.Button(master=play, text="Grade 2", command=lambda: on_click(2), font='verdana 20 bold italic', relief=tk.RAISED, bg='green', fg='yellow')
button2.grid(row=8, column=0, padx=(0,420))
button3=tk.Button(master=play, text="Grade 3", command=lambda: on_click(3), font='verdana 20 bold italic', relief=tk.RAISED, bg='lightblue', fg='black')
button3.grid(row=9, column=0, padx=(0,420))
button4=tk.Button(master=play, text="Grade 4", command=lambda: on_click(4), font='verdana 20 bold italic', relief=tk.RAISED, bg='yellow', fg="green")
button4.grid(row=10, column=0, padx=(0,420))
play.mainloop()