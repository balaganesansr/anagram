from tkinter import *
import random
import string
import time
from components import custom_font , entry_font , checkAnswer , toCaps , finish
import numpy as np
score=0

text = [random.choice(string.ascii_uppercase) for x in range(16)]
textgrid = np.array(text).reshape(4,4)
print(textgrid)
tk = Tk()
tk.iconbitmap("unnamed.ico")
tk.resizable(0,0)
answer = StringVar()
scr=IntVar()

tk.title("Anagram")
tk.geometry('750x500')

scoreboard = Label(tk,text="Score : "+str(scr.get()),textvariable=scr)
scoreboard.grid(row=0,column=3)
for i in range(4):
    for j in range(4):
       l =  Label(tk,text=" "+textgrid[i][j]+" ")
       l.configure(font=custom_font)
       l.grid(row=i+1,column=j,)
       print(i+1,j+1)
showans = Text(tk,width=20,)
showans.grid(row=1,column=5,rowspan=5)
showans.config(state=DISABLED)
ent = Entry(tk,textvariable=answer,width=40,font=entry_font)
ent.grid(row=5,column=0,columnspan=3,)
ent.focus()
Button(tk,text="Finish The Game",command=lambda :finish(answer,showans,scr,tk)).grid(row=6,column=5,)

Button(tk,text="Sumbit",command=lambda :checkAnswer(showans,answer,text,scr)).grid(row=5,column=3)


ent.bind("<KeyRelease>", lambda event:toCaps(answer))
tk.bind('<Return>',lambda event: checkAnswer(showans,answer,text,scr))
tk.mainloop()