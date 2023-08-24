
from tkinter import END , NORMAL , DISABLED , messagebox , Tk as t , Text , Label
from nltk.corpus import words

from playsound import playsound
import threading
#new_string = re.sub(r'[0-9]', '', )
custom_font = ("Comic Sans MS", 40, "bold")
entry_font = ("Comic Sans MS", 14, "bold")
list_typed = []
def checkAnswer(showans,ans,text,score):
    answer = ans.get()
    print(showans.get("1.0","end-1c").split())
    print([*answer])
    ans_copy = answer
    text_copy = text.copy()
    for i in ans_copy:
        if i in text_copy:
            print(i)
            text_copy.remove(i)
        elif i not in text_copy:
            if i == " ":
                messagebox.showinfo("InvalidCharacterExtension" , "Sory , but dont use space")
                return
            else:
                messagebox.showerror("LetterNotFoundError", i+" not found or can't use this much time")
                ans.set("")
                return

    if answer in list_typed:
        messagebox.showerror("Invalid!!","Word already there!!!")       
    elif (answer.lower() in words.words()):
        showans.config(state=NORMAL)
        print(showans.get("1.0","end-1c").split("\n"))
        idx = len(showans.get("1.0","end-1c").split("\n"))
        sound_thread = threading.Thread(target=lambda:playsound('ok.mp3'))
        sound_thread.start()
        showans.insert(END,str(idx)+"."+answer+"\n")
        list_typed.append(answer)
        print(list_typed)
        score.set(score.get()+1)
        showans.config(state=DISABLED)
    else:
        messagebox.showinfo("Sorry" , "Sorry, but i cant understand the word!!!")
        
    ans.set("")

def toCaps(v):
    v.set(v.get().upper())
def finish(answer,showans,score,tk):
    # answer.set("")
    # showans.config(state=NORMAL)
    # showans.delete("1.0","end")
    # showans.config(state=DISABLED)
    # score.set(0)
    
    sw = t()
    print()
    sw.geometry('200x400')
    Label(sw,text="Your Score is : "+str(score.get())).grid(row=1,column=1)
    sw.mainloop()

