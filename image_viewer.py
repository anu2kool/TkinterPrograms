from tkinter import *
from PIL import ImageTk, Image
import pygame
root=Tk()
root.title("Images")
root.iconbitmap('imageico.ico')
img=ImageTk.PhotoImage(Image.open('bullet.png'))
label=Label(image=img)
label.pack()
root.mainloop()