from tkinter import *
def callback(r,c):
    global player
    if player=='X'and states [r][c]==0 and stop_game== False:
        b[r][c].configure(text='X' ,fg='blue',bg='white')
        states[r][c]='X'
        player='o'
    if player=='o'and states [r][c]==0 and stop_game== False:
        b[r][c].configure(text='o' ,fg='orange',bg='black')
        states[r][c]='X'
        player='X'
root=Tk()
root.title("Tic TAC Toe")
b=[[0,0,0],
   [0,0,0],
   [0,0,0]]

states=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j]=Button(font=("Arial",60),width=4,bg='powder blue',command= lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row=i,column=j)
        player="X"
        stop_game = False
mainloop()
