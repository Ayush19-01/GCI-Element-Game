#Made for the sole purpose of GCI 2019
import periodictable as p
import random
from tkinter import *
from tkinter import messagebox
score=0
dict={}
dict1={}
lives=5
l=[]
a=1
for i in p.elements:
    if a==1:
        a+=1
        continue
    else:
        tmp1=i.number
        dict1[tmp1]=i
        dict[tmp1]=str(i)
        l.append(str(i))
def howto(event):
    messagebox.showinfo("How to play","Rules:\n1.The atomic number of a random element from periodic table would be shown\n2. You have to guess it, the answers are case sensitive\n3.You only have 5 lives, if answered incorrectly five times you will lose.\n4. Each correct answer gives you 3 points.")

def hint(event):
    global ele
    x=dict1[ele]
    y=x.mass
    messagebox.showinfo("Hint","It's Atomic Mass is: "+str(y)+" u")
def get(event):
    global lives
    global label4
    if lives==1:
        messagebox.showinfo("Error", "Cannot get the answer or you will lose.")
    else:
        z=dict1[ele]
        x=z.name
        messagebox.showinfo("Answer","The correct answer is "+str(x)+" and it's symbol is "+str(z))
        lives-=1
        label4.place_forget()
        label4 = Label(root2, text="Lives: " + str(lives), font=("roboto", 15), bg="#220047",
                       fg="#CE9141")
        label4.place(x=500, y=180)


def check(event):
    global lives
    global label4
    global score
    global l
    y=answer.get()
    if y not in l:
        messagebox.showinfo("Error","The answer you entered does not exist in the periodic table! Please try a valid element! ")
    if y in l:
        if y == dict[ele]:
            messagebox.showinfo("Correct",Username.get()+", your answer was correct, Good Job!")
            labelm.place_forget()
            label1.place_forget()
            label3.place_forget()
            button2.place_forget()
            button3.place_forget()
            entry2.place_forget()
            score+=3
            gamegui()

        else:
            lives-=1
            if lives<=0:
                messagebox.showinfo("Incorrect", "Your Answer was incorrect, You lost all your lives, game over\nYour final score was : "+str(score))
                exit()
            else:
                messagebox.showinfo("Incorrect","Your Answer was incorrect, As a penalty you loose one life!")
                label4.place_forget()
                label4 = Label(root2, text="Lives: " + str(lives), font=("roboto", 15), bg="#220047",
                               fg="#CE9141")
                label4.place(x=500, y=180)

def main1():
    global root1
    global Username
    root1=Tk()
    root1.resizable(0,0)
    Username = StringVar()
    root1.geometry("500x220")
    root1.config(bg="#220047")
    root1.title("Game")
    label_1 = Label(root1,text="Element Guessing Game",font=("roboto",30),bg="#220047",fg="#CE9141")
    label_1.place(x=30,y=10)
    label_2 = Label(root1,text="Enter the your name:",font=("roboto",19),bg="#220047",fg="#CE9141")
    label_2.place(x=30,y=90)
    entry1= Entry(root1,textvar=Username,width=30)
    entry1.place(x=270,y=100)
    button1 = Button(root1,text=" Play ",font=("roboto",20),bg="#CE9141",fg="#220047",activeforeground="#CE9141",activebackground="#220047")
    button1.bind("<Button-1>",startgame)
    button1.place(x=120,y=150)
    button2 = Button(root1, text="How to play", font=("roboto", 20), bg="#CE9141", fg="#220047", activeforeground="#CE9141",
                     activebackground="#220047")
    button2.bind("<Button-1>", howto)
    button2.place(x=240, y=150)
    root1.mainloop()
def startgame(event):
    global root2
    root1.destroy()
    root2 = Tk()
    root2.title("Game")
    root2.resizable(0, 0)
    root2.geometry("600x300")
    gamegui()
def generate(event):
    labelm.place_forget()
    label1.place_forget()
    label3.place_forget()
    button2.place_forget()
    button3.place_forget()
    entry2.place_forget()
    gamegui()

def close(event):
    quit()
def gamegui():
    global ele
    global answer
    global label1
    global label2
    global label3
    global label4
    global button2
    global button3
    global entry2
    global labelm
    global button4
    global button5
    global button6
    ele = random.randint(1, 118)
    answer = StringVar()
    root2.config(bg="#220047")
    labelm= Label(root2, text="Atomic Number is\n"+str(ele), font=("roboto", 40), bg="#220047", fg="#CE9141")
    labelm.place(x=80, y=60)
    label1 = Label(root2, text="Guess the element from its atomic number", font=("roboto", 22), bg="#220047", fg="#CE9141")
    label1.place(x=20, y=10)
    button2 = Button(root2, text="   Hint   ", font=("roboto", 15), bg="#CE9141", fg="#220047", activeforeground="#CE9141",
                     activebackground="#220047")
    button2.bind("<Button-1>", hint)
    button2.place(x=10, y=140)
    label3 = Label(root2, text="Enter your answer here:", font=("roboto", 15), bg="#220047",
                   fg="#CE9141")
    label3.place(x=120, y=212)
    label4=Label(root2, text="Lives: "+str(lives), font=("roboto", 15), bg="#220047",
          fg="#CE9141")
    label4.place(x=500, y=180)
    label5 = Label(root2, text="Score: " + str(score), font=("roboto", 15), bg="#220047",
                   fg="#CE9141")
    label5.place(x=10, y=180)
    entry2 = Entry(root2, textvar=answer, width=20)
    entry2.place(x=347, y=219)
    button3 = Button(root2, text="    Submit    ", font=("roboto", 15), bg="#CE9141", fg="#220047", activeforeground="#CE9141",
                     activebackground="#220047")
    button3.bind("<Button-1>", check)
    button3.place(x=210, y=250)

    button4 = Button(root2, text="   Quit   ", font=("roboto", 15), bg="#CE9141", fg="#220047", activeforeground="#CE9141",
                     activebackground="#220047")
    button4.bind("<Button-1>", close)
    button4.place(x=500, y=140)

    button5 = Button(root2, text="Get Answer", font=("roboto", 15), bg="#CE9141", fg="#220047", activeforeground="#CE9141",
                     activebackground="#220047")
    button5.bind("<Button-1>", get)
    button5.place(x=80, y=250)

    button6 = Button(root2, text="Generate Another", font=("roboto", 15), bg="#CE9141", fg="#220047",
                     activeforeground="#CE9141",
                     activebackground="#220047")
    button6.bind("<Button-1>", generate)
    button6.place(x=350, y=250)
    root2.mainloop()

main1()
