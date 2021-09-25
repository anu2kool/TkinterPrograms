import tkinter as tk
from PIL import Image, ImageTk
root=tk.Tk()
global flag
global count
global images
count=1
flag=0
def forward():
    global count
    global flag
    flag=1
    count+=1
    if count==6:
        count=1
    label=tk.Label(image=images[count-1])
    label.grid(row=1, column=0, columnspan=5)
def backward():
    global count
    global flag
    flag=1
    count-=1
    if count==0:
        count=5
    label=tk.Label(image=images[count-1])
    label.grid(row=1, column=0, columnspan=5)
img1=ImageTk.PhotoImage(Image.open('bullet.png').resize((400,400)))
img2=ImageTk.PhotoImage(Image.open('enemy.png').resize((400,400)))
img3=ImageTk.PhotoImage(Image.open('space.png').resize((400,400)))
img4=ImageTk.PhotoImage(Image.open('bullet1.jpg').resize((400,400)))
img5=ImageTk.PhotoImage(Image.open('player.png').resize((400,400)))
images=[img1,img2,img3,img4,img5]
label=tk.Label(root, text="Image Viewer", font=('Arial',40))
label.grid(row=0, column=0, columnspan=5)
if flag==0:
    label=tk.Label(image=img1)
    label.grid(row=1, column=0, columnspan=5)
b_forward=tk.Button(root, text=">>", command=forward)
b_backward=tk.Button(root, text="<<", command=backward)
b_forward.grid(row=2, column=4)
b_backward.grid(row=2, column=0)
root.mainloop()