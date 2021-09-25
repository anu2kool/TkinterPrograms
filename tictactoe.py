import tkinter as tk
root=tk.Tk()
root.iconbitmap('tic.ico')
frame1=tk.Frame(root)
frame2=tk.Frame(root)
l1=tk.Label(frame1, text="First Player:")
l1.grid(row=0, column=0)
l2=tk.Label(frame1, text="Second Player:")
l2.grid(row=1, column=0)
e1=tk.Entry(frame1, width=30)
e2=tk.Entry(frame1, width=30)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
frame1.grid(row=0, column=0)    
global count
count=0
states=[]
for i in range(3):
    states.append([-1,-1,-1])
def reset():
    global b
    global count
    global states
    count=0
    for i in range(3):
        for j in range(3):
            b[i][j].config(text="", bg='black',command=lambda r=i , c=j : onclick(r,c))
    for i in range(3):
        for j in range(3):
            states[i][j]=-1
    global label
    label.config(text="")
def onclick(i, j):
    indices=[]
    global count
    global b
    count+=1
    if count%2==1:
        b[i][j]=tk.Button(frame2, text="X",font=('Arial',60), width=4,bg='SystemButtonFace',fg='black')
        b[i][j].grid(row=i, column=j)
        states[i][j]=1
    else:
        b[i][j]=tk.Button(frame2, text="O",font=('Arial',60), width=4, bg='SystemButtonFace', fg='black')
        b[i][j].grid(row=i, column=j)
        states[i][j]=0
    flag=0
    text=""
    for i in range(3):
        if states[i][0]==states[i][1] and states[i][1]==states[i][2]:
            if states[i][0]==1:
                flag=1
                text="X"
                indices.append([i,0])
                indices.append([i,1])
                indices.append([i,2])
            elif states[i][0]==0:
                flag=1
                text="O"
                indices.append([i,0])
                indices.append([i,1])
                indices.append([i,2])
        if flag:
            break
        if states[0][i]==states[1][i] and states[1][i]==states[2][i]:
            if states[0][i]==1:
                text="X"
                flag=1
                indices.append([0,i])
                indices.append([1,i])
                indices.append([2,i])
            elif states[0][i]==0:
                flag=1
                text="O"
                indices.append([0,i])
                indices.append([1,i])
                indices.append([2,i])
        if flag:
            break
    if flag==0:
        if states[0][0]==states[1][1] and states[1][1]==states[2][2]:
            if states[0][0]==1:
                text="X"
                flag=1
                indices.append([0,0])
                indices.append([1,1])
                indices.append([2,2])
            elif states[0][0]==0:
                flag=1
                text="O"
                indices.append([0,0])
                indices.append([1,1])
                indices.append([2,2])
        if states[0][2]==states[1][1] and states[1][1]==states[2][0]:
            if states[0][2]==1:
                text="X"
                flag=1
                indices.append([0,2])
                indices.append([1,1])
                indices.append([2,0])
            elif states[0][2]==0:
                flag=1
                text="O"
                indices.append([0,2])
                indices.append([1,1])
                indices.append([2,0])
    global label
    if flag:
        for i in indices:
            b[i[0]][i[1]].config(bg='yellow')
        if text=="X":
            label=tk.Label(frame2, text=e1.get()+" wins",font=('Halvetica',30))
            label.grid(row=3, column=1)
            tk.messagebox.showinfo('information',e1.get()+' wins')
        elif text=="O":
            label=tk.Label(frame2, text=e2.get()+" wins",font=('Halvetica',30))
            label.grid(row=3, column=1)
            tk.messagebox.showinfo('information',e2.get()+' wins')
        
        b_reset=tk.Button(frame2, text="Reset", command=reset, font=('Arial',20))
        b_reset.grid(row=3, column=2)
    if flag==0 and count==9:
        label=tk.Label(frame2, text="DRAW", font=('Halvetica',30))
        label.grid(row=3,column=1)
        b_reset=tk.Button(frame2, text="Reset", command=reset, font=('Arial',20))
        b_reset.grid(row=3, column=2)
        for i in range(3):
            for j in range(3):
                b[i][j].config(bg='red')
def close():
    root.destroy()
b=[]
for i in range(3):
    b.append([0,0,0])
for i in range(3):
    for j in range(3):
        b[i][j]=tk.Button(frame2, text="",command=lambda r=i , c=j : onclick(r,c), font=('Arial',60), width=4, bg='black')
        b[i][j].grid(row=i, column=j)
e_button=tk.Button(frame2,text="exit",command=close)
e_button.grid(row=4, column=2)
frame2.grid(row=1, column=0)
root.mainloop()

