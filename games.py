import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import random
import sqlite3

global name1, name2
global points, cnts, toss_pressed
toss_pressed=0
points=30
cnts=0

def Play_Game(player_no, no):
    if toss_pressed==1:
        global points, name1, name2
        points-=no
        no_of_piles.config(text=str(points))
        if points==0:
            if player_no==1:
                conn=sqlite3.connect('games.db')
                c=conn.cursor()
                c.execute('SELECT * FROM stats')
                conn.commit()
                list1=c.fetchall()
                flag=0
                wins=0
                loses=0
                for i in list1:
                    if i[0]==name1:
                        flag=1
                        wins=i[1]
                        loses=i[2]
                        break
                if flag==0:
                    c.execute('INSERT INTO stats VALUES (?,?,?)', (name1,1,0))
                    conn.commit()
                else:
                    c.execute('UPDATE stats SET wins=? WHERE name=?', (wins+1, name1))
                    conn.commit()
                loses2=0
                flag=0
                for i in list1:
                    if i[0]==name2:
                        loses2=i[2]
                        flag=1
                        break
                if flag==1:
                    c.execute('UPDATE stats SET loses=? WHERE name=?', (loses2+1, name2))
                    conn.commit()
                else:
                    c.execute('INSERT INTO stats VALUES (?,?,?)', (name2,0,1))
                    conn.commit()
                result.config(text=name1+" wins")
            if player_no==2:
                conn=sqlite3.connect('games.db')
                c=conn.cursor()
                c.execute('SELECT * FROM stats')
                conn.commit()
                list1=c.fetchall()
                flag=0
                wins=0
                loses=0
                for i in list1:
                    if i[0]==name2:
                        flag=1
                        wins=i[1]
                        loses=i[2]
                        break
                if flag==0:
                    c.execute('INSERT INTO stats VALUES (?,?,?)', (name2,1,0))
                    conn.commit()
                else:
                    c.execute('UPDATE stats SET wins=? WHERE name=?', (wins+1, name2))
                    conn.commit()
                loses2=0
                flag=0
                for i in list1:
                    if i[0]==name1:
                        loses2=i[2]
                        flag=1
                        break
                if flag==1:
                    c.execute('UPDATE stats SET loses=? WHERE name=?', (loses2+1, name1))
                    conn.commit()
                else:
                    c.execute('INSERT INTO stats VALUES (?,?,?)', (name1,0,1))
                    conn.commit()
                result.config(text=name2+" wins")
    else:
        tk.messagebox.showinfo("INFO", "Toss Please")

def Toss():
    global toss_pressed
    toss_pressed=1
    s.configure('m13.TLabel', font='Times 15 bold italic')
    toss_button.destroy()
    num=random.randint(0,2)
    toss_label=ttk.Label(master=toss_frame, text="", style='m13.TLabel')
    toss_label.grid(row=0, column=0)
    if num==0:
        toss_label.config(text=name1+"'s turn")
    else:
        toss_label.config(text=name2+"'s turn")
        
def submit_name(num):
    if num==1:
        global name1
        name1=name1_entry.get()
        if len(name1)>0:
            name1_entry.destroy()
            button1.destroy()
            s.configure('m4.TLabel', font='Arial 16 bold')
            player_name1=ttk.Label(master=frame_names, text=name1, style='m4.TLabel')
            player_name1.grid(row=1, column=0, padx=(20,0))
        else:
            tk.messagebox.showinfo("INFO", "Enter name!")
    if num==2:
        global name2
        name2=name2_entry.get()
        if len(name2)>0:
            name2_entry.destroy()
            button2.destroy()
            s.configure('m4.TLabel', font='Arial 16 bold')
            player_name2=ttk.Label(master=frame_names, text=name2, style='m4.TLabel')
            player_name2.grid(row=1, column=1, padx=(0,100))
        else:
            tk.messagebox.showinfo("INFO", "Enter name!")

def status(player_no):
    global name1, name2
    conn=sqlite3.connect('games.db')
    c=conn.cursor()
    if player_no==1:
        c.execute('SELECT * FROM stats')
        conn.commit()
        list1=c.fetchall()
        flag=0
        wins1=0
        loses1=0
        for i in list1:
            if i[0]==name1:
                flag=1
                wins1=i[1]
                loses1=i[2]
                break
        if flag==0:
            c.execute('INSERT INTO stats VALUES (?,?,?)', (name1,0,0))
            conn.commit()
        new_window=tk.Tk()
        new_window.geometry('400x400')
        new_window.config(background="black")
        s=ThemedStyle(new_window)
        s.set_theme('black')
        s.configure('m16.TLabel', font='Arial 18 bold', background='black')
        p_name1=ttk.Label(master=new_window, text=name1, style='m16.TLabel')
        p_name1.grid(row=0, column=0, padx=(170,0))
        p1_wins_l=ttk.Label(master=new_window, text="Wins: ", style='m16.TLabel')
        p1_wins_l.grid(row=1, column=0, padx=(140,0))
        p1_loses_l=ttk.Label(master=new_window, text="Loses: ", style='m16.TLabel')
        p1_loses_l.grid(row=2, column=0, padx=(140,0))
        p1_wins=ttk.Label(master=new_window, text=str(wins1), style='m16.TLabel')
        p1_wins.grid(row=1, column=1)
        p1_loses=ttk.Label(master=new_window, text=str(loses1), style='m16.TLabel')
        p1_loses.grid(row=2, column=1)
        new_window.mainloop()
    elif player_no==2:
        c.execute('SELECT * FROM stats')
        conn.commit()
        list1=c.fetchall()
        flag=0
        wins2=0
        loses2=0
        for i in list1:
            if i[0]==name2:
                flag=1
                wins2=i[1]
                loses2=i[2]
                break
        if flag==0:
            c.execute('INSERT INTO stats VALUES (?,?,?)', (name2,0,0))
            conn.commit()
        new_window=tk.Tk()
        new_window.geometry('400x400')
        new_window.config(background="black")
        s=ThemedStyle(new_window)
        s.set_theme('black')
        s.configure('m16.TLabel', font='Arial 18 bold', background='black')
        p_name1=ttk.Label(master=new_window, text=name2, style='m16.TLabel')
        p_name1.grid(row=0, column=0, padx=(170,0))
        p2_wins_l=ttk.Label(master=new_window, text="Wins: ", style='m16.TLabel')
        p2_wins_l.grid(row=1, column=0, padx=(140,0))
        p2_loses_l=ttk.Label(master=new_window, text="Loses: ", style='m16.TLabel')
        p2_loses_l.grid(row=2, column=0, padx=(140,0))
        p2_wins=ttk.Label(master=new_window, text=str(wins2), style='m16.TLabel')
        p2_wins.grid(row=1, column=1)
        p2_loses=ttk.Label(master=new_window, text=str(loses2), style='m16.TLabel')
        p2_loses.grid(row=2, column=1)
        new_window.mainloop()
    conn.close()    
    
def Reset():
    global points, cnts, toss_pressed
    toss_pressed=0
    points=30
    cnts=0
    no_of_piles.config(text="30")
    toss_button=ttk.Button(master=toss_frame, text="TOSS", command=Toss, style='m12.TButton')
    toss_button.grid(row=0, column=0, padx=(0,0))
    result.config(text="")

def Exit():
    root.destroy()

root=tk.Tk()
root.title("MY GAME")
root.config(background="black")
root.geometry('800x700')

s=ThemedStyle(root)
s.set_theme('black')
s.configure('m1.TLabel', font='verdana 28 bold', relief=tk.RAISED)

frame_head=ttk.Frame(master=root)
frame_head.grid(row=0, column=0)
heading_label=ttk.Label(master=frame_head, text="My Game", style='m1.TLabel')
heading_label.grid(row=0, column=0, rowspan=2, padx=(300,500))

frame_names=ttk.Frame(master=root)
frame_names.grid(row=1, column=0, padx=(0,180))
s.configure('m2.TLabel', font='Arial 20 bold')
name1=ttk.Label(master=frame_names, text="Player 1", style='m2.TLabel')
name1.grid(row=0, column=0, padx=(80,48))
name1_entry=ttk.Entry(master=frame_names, width=20, font='Arial 18 bold')
name1_entry.grid(row=1, column=0, padx=(80,50))
name2=ttk.Label(master=frame_names, text="Player 2", style='m2.TLabel')
name2.grid(row=0, column=1, padx=(0,100))
name2_entry=ttk.Entry(master=frame_names, width=20, font='Arial 18 bold')
name2_entry.grid(row=1, column=1, padx=(0,100))
s.configure('m3.TButton', foreground="white", background="black")
button1=ttk.Button(master=frame_names, text="Submit", style="m3.TButton", command=lambda: submit_name(1))
button1.grid(row=2, column=0, pady=(5,5))
button2=ttk.Button(master=frame_names, text="Submit", style="m3.TButton", command=lambda: submit_name(2))
button2.grid(row=2, column=1, padx=(0,100), pady=(5,5))

s.configure('m11.TFrame', background='black')
s.configure('m12.TButton', font='Arial 15 bold', relief=tk.RAISED)
toss_frame=ttk.Frame(master=root, style='m11.TFrame')
toss_frame.grid(row=2, column=0, padx=(0,180), pady=(10,10))
toss_button=ttk.Button(master=toss_frame, text="TOSS", command=Toss, style='m12.TButton')
toss_button.grid(row=0, column=0, padx=(0,0))

game_frame=ttk.Frame(master=root)
game_frame.grid(row=3, column=0, pady=(5,5), padx=(50,250))
s.configure('m5.TLabel', font='Arial 20 bold')
no_of_piles_label=ttk.Label(master=game_frame, text="Number of stones:", style='m5.TLabel')
no_of_piles_label.grid(row=0, column=0)
s.configure('m6.TLabel', font='Arial 20 bold', relief=tk.RIDGE)
no_of_piles=ttk.Label(master=game_frame, text="30", style='m6.TLabel')
no_of_piles.grid(row=0, column=1, padx=(60,0))

s.configure('m7.TButton', font='Times 17 bold', relief=tk.RAISED)

s.configure('m8.TFrame', background='black')
player_area=ttk.Frame(master=root, style='m8.TFrame')
player_area.grid(row=4, column=0)
play_button1_1=ttk.Button(master=player_area, text="1", style='m7.TButton', command=lambda: Play_Game(1,1))
play_button1_1.grid(row=0, column=0, padx=(0,300))
play_button1_2=ttk.Button(master=player_area, text="2", style='m7.TButton', command=lambda: Play_Game(1,2))
play_button1_2.grid(row=1, column=0, padx=(0,300))
play_button1_3=ttk.Button(master=player_area, text="3", style='m7.TButton', command=lambda: Play_Game(1,3))
play_button1_3.grid(row=2, column=0, padx=(0,300))
play_button2_1=ttk.Button(master=player_area, text="1", style='m7.TButton', command=lambda: Play_Game(2,1))
play_button2_1.grid(row=0, column=1, padx=(0,200))
play_button2_2=ttk.Button(master=player_area, text="2", style='m7.TButton', command=lambda: Play_Game(2,2))
play_button2_2.grid(row=1, column=1, padx=(0,200))
play_button2_3=ttk.Button(master=player_area, text="3", style='m7.TButton', command=lambda: Play_Game(2,3))
play_button2_3.grid(row=2, column=1, padx=(0,200))
s.configure('m10.TFrame', background="black")
result_frame=ttk.Frame(master=root, style="m10.TFrame")
result_frame.grid(row=5, column=0, padx=(0,170))
s.configure('m9.TLabel', font='Arial 24 bold italic', background="black")
result=ttk.Label(master=result_frame, text="", style="m9.TLabel")
result.grid(row=0, column=0)

s.configure('m14.TFrame', background="black")
stats_frame=ttk.Frame(master=root, style='m14.TFrame')
stats_frame.grid(row=6, column=0)
stats1=ttk.Button(master=stats_frame, text="Stats", command=lambda: status(1))
stats1.grid(row=0, column=0, padx=(0,500))
stats2=ttk.Button(master=stats_frame, text="Stats", command=lambda: status(2))
stats2.grid(row=0, column=1, padx=(0,200))

s.configure('m17.TButton', font='Arial 14 italic')
reset_frame=ttk.Frame(master=root)
reset_frame.grid(row=7, column=0, pady=(200,0), padx=(0,180))
reset_button=ttk.Button(master=reset_frame, text="RESET", style='m17.TButton', command=Reset)
reset_button.grid(row=0, column=0)

exit_frame=ttk.Frame(master=root)
exit_frame.grid(row=8, column=0, padx=(400,0))
exit_button=ttk.Button(master=exit_frame, text="Exit", command=Exit)
exit_button.grid(row=0, column=0)
root.mainloop()



