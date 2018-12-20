#made_by_sameer_kaushik
from tkinter import *
import pyglet
from pygame import mixer

def main():    
    root=Tk()
    root.title(" ==>  P O N G     G A M E  <== ")     #title changed
    root.resizable(0,0)     #window can not be resized
    root.wm_attributes("-topmost",1)    #window will be on the topmost layer

    import time
    import random
    from pynput.keyboard import Key,Controller
    kb=Controller()

    c=Canvas(width=500, height=500 ,bg="palegreen")    #canvas created
    c.pack()

    ball=c.create_oval(220,120,240,140,fill="blue")  #ball created
    pad=c.create_rectangle(280,400,420,410, fill="red") #paddle created
    p=3
    q=2
    sc=0
    c.create_text(250,15, text="S C O R E",font=("Arial",15,"bold"), fill="red")

    while 1:
        bpos=c.coords(ball)
        c.move(ball,p,q)       #ball starts to move
        root.update()
        time.sleep(0.01)        #time lag bw 2 frames

        cheight=c.winfo_height()        #height of canvas
        cwidth=c.winfo_width()      #width of canvas



        if bpos[0]<=0:       #if ball toches the upper boundary
            p=3

        if bpos[1]<=30:       #if ball toches the left boundary
            q=2
            
        if bpos[2]>=cwidth:      #if ball toches the lower boundary
            p=-3
            
        if bpos[3]>=cheight:     #if ball toches the right boundary
            q=-2

        ppos=c.coords(pad)      #coordinates of paddle
        
        root.update()   #frames updated

        def pad_left(event):    #pad moved left
            c.move(pad,-10,0)
        
        def pad_right(event):   #pad moves right
            c.move(pad,10,0)
           
        c.bind_all("<KeyPress-Left>",pad_left)  #left key linked with pad
        c.bind_all("<KeyPress-Right>",pad_right)    #right key linked with pad

        pr=ppos[0]
        pl=ppos[2]
        pt=ppos[1]
        end=ppos[3]

        if bpos[3]==pt and bpos[0]>=pr and bpos[2]<=pl:
            q=-2
            mixer.init()
            mixer.music.load("./ring.wav")
            mixer.music.play()
            c.create_text(250,35, text=str(int(sc)), font=("Arial",15,"bold"), fill="palegreen")
            sc=sc+0.5
            c.create_text(250,35, text=str(int(sc)), font=("Arial",15,"bold"), fill="forestgreen")
            root.update()

        if bpos[1]==end:
            def pl():
                root.destroy()
                main()
            def ex():
                root.destroy()
            p=0
            q=0
            abc=str(int(sc))
            mixer.init()
            mixer.music.load("./gameover.wav")
            mixer.music.play()
            a=c.create_text(250,250,text="GAME OVER",font=("none",30,"bold"),fill="red")   #Display game over when ball crosses the paddle
            b=c.create_text(250,300,text="Score : "+abc,font=("none",20,"bold"),fill="blue")   #Show the score which is equal to the time taken
            Button(text="Play again",command=pl,fg="blue",width=20).pack()  #play_again
            Button(text="Exit",command=ex, fg="red",width=20).pack()   #exit
    mainloop()

main()
#made_by_sameer_kaushik
