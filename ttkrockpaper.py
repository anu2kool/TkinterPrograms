import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import random
import pygame
from PIL import Image, ImageTk
import sqlite3
#conn=sqlite3.connect('high_wins.db')
#c=conn.cursor()
#c.execute("CREATE TABLE wins ( name text, score integer )")
#c.execute("DROP TABLE wins")
#nam="computer"
#s=0
#c.execute("INSERT INTO wins (name,score) VALUES (?,?);",(nam,s))
#conn.commit()
#conn.close()
if __name__ == '__main__':
    global state
    root=tk.Tk()
    s=ThemedStyle(root)
    s.set_theme('black')
    root.iconbitmap('tic.ico')
    root.config(background='lightblue')
    state=0
    global flag
    global option_state
    global score_comp, score_player, no_of_points
    global username
    score_comp=0
    score_player=0
    no_of_points=0
    flag=0
    option_state=0
    
    def Update_wins():
        global username, high_wins, high_name 
        conn=sqlite3.connect('high_wins.db')
        c=conn.cursor()
        c.execute("SELECT * FROM wins")
        conn.commit()
        list1=c.fetchall()
        f=0
        for i in list1:
            if username==i[0]:
                f=1
                prev_score=int(i[1])
                prev_score+=1
                c.execute("UPDATE wins SET score=? WHERE name=? ;", (prev_score, username))
                break
        if f==0:
            c.execute("INSERT INTO wins (name, score) VALUES (?, ?) ;", (username, 1))
        c.execute("SELECT * FROM wins")
        conn.commit()
        list2=c.fetchall()
        max_name=""
        ind=-1
        max_score=0
        cnt1=-1
        for i in list2:
            cnt1+=1
            if i[1]>max_score:
                ind=cnt1
                max_score=i[1]
        max_name+=list2[ind][0]
        high_wins.config(text=str(max_score))
        high_name.config(text=max_name)
        conn.close()
        print(list1)
        print(list2)
        print("maxname",max_name)
        print("max_score",max_score)
    def play(n):
        global no_of_points, score_player, score_comp
        global bq1 , bq2 , bq3
        global score1, score2, option_state
        global win, state
        if option_state==0:
            tk.messagebox.showinfo("information", "Enter number of points")
        if state==1:
            option_state=1
            score1=0
            score2=0
            s.configure('m10.TFrame', background='lightblue')
            score_frame=ttk.Frame(root, style='m10.TFrame')
            score_frame.grid(row=2, column=1)
            s.configure('m11.TLabel', font='Arial 25 bold italic')
            name_player=ttk.Label(score_frame,text=username+":", style='m11.TLabel')
            name_comp=ttk.Label(score_frame, text="Computer:", style='m11.TLabel')
            name_player.grid(row=1, column=0)
            name_comp.grid(row=0, column=0)
            s.configure('m12.TLabel', font='Arial 30 bold')
            score1=ttk.Label(score_frame, text=str(score_comp), style='m12.TLabel')
            score2=ttk.Label(score_frame, text=str(score_player), style='m12.TLabel')
            score1.grid(row=0, column=1)
            score2.grid(row=1, column=1)
            state=0
        no_of_points-=1
        if no_of_points==0:
            choices=[0,1,2]
            index=random.choice(choices)
            str1=""
            if index==0:
                str1+="rock"
            if index==1:
                str1+="paper"
            if index==2:
                str1+="scissor"
            str2=""
            if n==0:
                str2+="rock"
            if n==1:
                str2+="paper"
            if n==2:
                str2+="scissor"
            imgcomp=ImageTk.PhotoImage(Image.open(str1+".png").resize((200,200)))
            imgplayer=ImageTk.PhotoImage(Image.open(str2+".png").resize((200,200)))
            bq1.configure(image=imgcomp)
            bq1.photo=imgcomp
            bq3.configure(image=imgplayer)
            bq3.photo=imgplayer
            if str1=="rock":
                if str2=="scissor":
                    score_comp+=1
                elif str2=="paper":
                    score_player+=1
            elif str1=="scissor":
                if str2=="rock":
                    score_player+=1
                elif str2=="paper":
                    score_comp+=1
            elif str1=="paper":
                if str2=="rock":
                    score_comp+=1
                elif str2=="scissor":
                    score_player+=1
            score1.config(text=str(score_comp))
            score2.config(text=str(score_player))
            result=tk.Frame(root)
            result.grid(row=3, column=1)
            win=tk.Label(result, text="", font=("Arial", 20))
            win.grid(row=0, column=0)
            if score_player>score_comp:
                win.config(text=username+" wins", highlightbackground="black", highlightthickness=4)
                result.config(highlightbackground="black", highlightthickness=4, relief=tk.RAISED)
                pygame.init()
                sound_win=pygame.mixer.Sound("winning.wav")
                sound_win.play()
                Update_wins()
            elif score_player<score_comp:
                win.config(text="You Lose", highlightbackground="black", highlightthickness=4)
                result.config(highlightbackground="black", highlightthickness=4,relief=tk.RAISED)
                pygame.init()
                sound_lose=pygame.mixer.Sound("lose.wav")
                sound_lose.play()
            elif score_player==score_comp:
                win.config(text="Draw", highlightbackground="black", highlightthickness=4)
                result.config(highlightbackground="black", highlightthickness=4, relief=tk.RAISED)
                pygame.init()
                sound_draw=pygame.mixer.Sound("draw.wav")
                sound_draw.play()
        elif no_of_points>0:
            choices=[0,1,2]
            index=random.choice(choices)
            str1=""
            if index==0:
                str1+="rock"
            if index==1:
                str1+="paper"
            if index==2:
                str1+="scissor"
            str2=""
            if n==0:
                str2+="rock"
            if n==1:
                str2+="paper"
            if n==2:
                str2+="scissor"
            imgcomp=ImageTk.PhotoImage(Image.open(str1+".png").resize((200,200)))
            imgplayer=ImageTk.PhotoImage(Image.open(str2+".png").resize((200,200)))
            bq1.config(image=imgcomp)
            bq1.photo=imgcomp
            bq3.config(image=imgplayer)
            bq3.photo=imgplayer
            if str1=="rock":
                if str2=="scissor":
                    score_comp+=1
                elif str2=="paper":
                    score_player+=1
            elif str1=="scissor":
                if str2=="rock":
                    score_player+=1
                elif str2=="paper":
                    score_comp+=1
            elif str1=="paper":
                if str2=="rock":
                    score_comp+=1
                elif str2=="scissor":
                    score_player+=1    
            score1.config(text=str(score_comp))
            score2.config(text=str(score_player))
    
    def options(num):
        global no_of_points, option_state
        options_label.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        global label2
        label2=tk.Label(frame_options, text="Number of points: "+str(num), font=('Arial',30))
        label2.grid(row=0, column=0, padx=40)
        no_of_points=num
        option_state=1
        
    def submit():
        global flag, username, frame_name
        global score1, score2, name_comp, name_player
        if len(name.get())==0:
            tk.messagebox.showinfo('info','Enter Name!')
        else:
            flag=1
            username=name.get()
            print(username)
            name_label1=tk.Label(frame_name, text="Hello "+username, font=('Halvetica',30))
            name_label1.grid(row=0, column=0)
            frame_name.config(highlightthickness=5, highlightbackground="black")
            submit_button.destroy()
            name_label.destroy()
            name.destroy()
            name2.config(text=username, font=('castellar',20), relief=tk.RAISED, highlightbackground="black", highlightthickness=2)
            if len(username)>0:
                score_frame=tk.Frame(root)
                score_frame.grid(row=2, column=1)
                name_player=tk.Label(score_frame,text=username+":", font=('Arial',25))
                name_comp=tk.Label(score_frame, text="Computer:", font=('Arial',25))
                name_player.grid(row=1, column=0)
                name_comp.grid(row=0, column=0)
                score1=tk.Label(score_frame, text=str(score_comp), font=("Arial",30))
                score2=tk.Label(score_frame, text=str(score_player), font=('Arial',30))
                score1.grid(row=0, column=1)
                score2.grid(row=1, column=1)
    
    def Exit():
        root.destroy()
        
    def reset():
        global option_state, label2, b1, b2, b3, options_label, bq1, bq3, score1, score2, win, name_comp, name_player, state, score_comp, score_player
        score_comp=0
        score_player=0
        option_state=0
        label2.destroy()
        s.configure('m4.TLabel', font='Arial 25 bold')
        options_label=ttk.Label(frame_options, text="Number of points", style='m4.TLabel')
        options_label.grid(row=0, column=0)
        s.configure('m1.TButton', font='Arial 12 bold', height=1, width=30, background='blue', foreground='black')
        b1=ttk.Button(frame_options, text="5", command=lambda: options(5), style='m1.TButton')
        b2=ttk.Button(frame_options, text="10", command=lambda: options(10), style='m1.TButton')
        b3=ttk.Button(frame_options, text="15", command=lambda: options(15), style='m1.TButton')
        b1.grid(row=1,column=0)
        b2.grid(row=2, column=0)
        b3.grid(row=3, column=0)
        imgcomp=ImageTk.PhotoImage(Image.open("qmark.png").resize((200,200)))
        imgplayer=ImageTk.PhotoImage(Image.open("qmark.png").resize((200,200)))
        bq1.configure(image=imgcomp)
        bq1.photo=imgcomp
        bq3.configure(image=imgplayer)
        bq3.photo=imgplayer
        score1.destroy()
        score2.destroy()
        win.destroy()
        name_comp.destroy()
        name_player.destroy()
        state=1
    root.geometry('1100x700')
    frame_head=tk.Frame(root)
    frame_head.grid(row=0, column=0)
    heading=tk.Label(frame_head, text="Rock Paper Scissor", relief=tk.RAISED, anchor=tk.CENTER,font=('Arial',40))
    heading.pack()
    
    frame_name=tk.Frame(root)
    frame_name.grid(row=1, column=0)
    
    if flag==0:
        name_label=tk.Label(frame_name, text="Enter Name:", font=('Arial',15))
        name_label.grid(row=0, column=0)
        name=tk.Entry(frame_name, width=20, font=('Arial',20))
        name.grid(row=0, column=1)
        submit_button=tk.Button(frame_name, text="Submit", command=submit)
        submit_button.grid(row=1, column=0)
    
    frame_options=ttk.Frame(root)
    frame_options.grid(row=0, column=1, rowspan=2)
    s.configure('m3.TButton', font='Arial 25 bold')
    options_label=ttk.Label(frame_options, text="Number of points", style='m3.TButton')
    options_label.grid(row=0, column=0, padx=(20,0))
    s.configure('m1.TButton', font='Arial 12 bold', height=1, width=30, background='blue', foreground='black')
    b1=ttk.Button(frame_options, text="5", command=lambda: options(5), style='m1.TButton')
    b2=ttk.Button(frame_options, text="10", command=lambda: options(10), style='m1.TButton')
    b3=ttk.Button(frame_options, text="15", command=lambda: options(15), style='m1.TButton')
    b1.grid(row=1,column=0)
    b2.grid(row=2, column=0)
    b3.grid(row=3, column=0)
    
    
    fight_area=tk.Frame(master=root, bd=2, highlightbackground="black", highlightthickness=5)
    fight_area.grid(row=2, column=0, rowspan=3, pady=80, padx=40)
    name1=tk.Label(master=fight_area, text="Computer", font=('castellar',20), relief=tk.RAISED, highlightbackground="black", highlightthickness=2)
    global name2
    name2=tk.Label(master=fight_area, text="")
    name1.grid(row=0, column=0)
    name2.grid(row=0, column=2)
    imgqm=ImageTk.PhotoImage(Image.open('qmark.png').resize((200,200)))
    imgvs=ImageTk.PhotoImage(Image.open('versus.jpg').resize((80,100)))
    global bq1, bq2, bq3
    bq1=tk.Button(master=fight_area, image=imgqm)
    bq2=tk.Button(master=fight_area, image=imgvs)
    bq3=tk.Button(master=fight_area, image=imgqm)
    bq1.grid(row=1, column=0)
    bq2.grid(row=1, column=1)
    bq3.grid(row=1, column=2)
    s.configure('m9.TFrame', background='lightblue')
    game_frame=ttk.Frame(root, style='m9.TFrame')
    game_frame.grid(row=5, column=0, pady=30)
    img1=ImageTk.PhotoImage(Image.open('rock.png').resize((80,80)))
    bi1=tk.Button(image=img1, master=game_frame, command=lambda: play(0))
    bi1.grid(row=0, column=0, padx=30)
    img2=ImageTk.PhotoImage(Image.open('paper.png').resize((80,80)))
    bi2=tk.Button(image=img2, master=game_frame, command=lambda: play(1))
    bi2.grid(row=0, column=1, padx=30)
    img3=ImageTk.PhotoImage(Image.open('scissor.png').resize((80,80)))
    bi3=tk.Button(image=img3, master=game_frame, command=lambda: play(2))
    bi3.grid(row=0, column=2, padx=30)
    
    reset_frame=ttk.Frame(master=root)
    reset_frame.grid(row=5, column=1)
    s.configure('m5.TButton', relief=tk.RAISED, font='Arial 18 bold', width=7, height=1, background='blue')
    reset_button=ttk.Button(master=reset_frame, text="reset", command=reset, style='m5.TButton')
    reset_button.grid(row=0, column=0, padx=150)
    
    exit_frame=ttk.Frame(master=root)
    exit_frame.grid(row=0, column=2)
    s.configure('m2.TButton', font='Arial 18 bold', relief=tk.RAISED, height=1, width=4, background='red')
    exit_button=ttk.Button(master=exit_frame, text="Exit", command=Exit, style='m2.TButton')
    exit_button.grid(row=0, column=0)
    
    s.configure('m6.TFrame', highlightthickness=3, highlightbackground='blue' )
    max_wins=ttk.Frame(master=root, style='m6.TFrame')
    max_wins.grid(row=4, column=1)
    s.configure('m7.TLabel', font='Arial 19')
    m_wins=ttk.Label(master=max_wins, text="Maximum wins", style='m7.TLabel')
    m_wins.grid(row=0, column=0, padx=(0,10))
    m_player=ttk.Label(master=max_wins, text="Player Name", style='m7.TLabel')
    m_player.grid(row=0, column=1)
    s.configure('m8.TLabel', font='Arial 16 bold')
    high_wins=ttk.Label(master=max_wins, text="nil", style='m8.TLabel')
    high_wins.grid(row=1, column=0)
    high_name=ttk.Label(master=max_wins, text="nil", style='m8.TLabel')
    high_name.grid(row=1, column=1)
    
    #Getting the highest wins from database high_wins.db table->wins
    max1=0
    max1_name=""
    cnt2=-1
    ind=-1
    conn=sqlite3.connect('high_wins.db')
    c=conn.cursor()
    c.execute("SELECT * FROM wins")
    conn.commit()
    lst=c.fetchall()
    for i in lst:
        cnt2+=1
        if i[1]>max1:
            max1=i[1]
            ind=cnt2
    max1_name+=lst[ind][0]
    high_wins.config(text=str(max1))
    high_name.config(text=max1_name)
    
    root.mainloop()