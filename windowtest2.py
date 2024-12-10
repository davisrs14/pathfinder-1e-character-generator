import tkinter as tk
from tkinter import * 
import random

def button_clicked():
    root.destroy()
    root2 = tk.Tk()
    dicetotal = []
    abilityScores = ["Strength     : ", "Dexterity    : ","Wisdom       : ", "Intellegence : " , "Constitution : ", "Charisma     : "]
    #abilityScoresFinal = []
    for i in range(0,6):
        randomNumbers = [random.randrange(1,6),random.randrange(1,6),random.randrange(1,6),random.randrange(1,6)] #generates the dice rolls
        randomNumbers.sort() #sorts the rolls least to greatest
        sumofdice = randomNumbers[1]+randomNumbers[2]+randomNumbers[3] #adds the 3 highest rolls to generate an ability score
        dicetotal.append(sumofdice) #adds the scores to a list for allocation
    root2.title("Scores")
    root2.configure(background="blue")
    root2.minsize(300, 300)  # width, height
    root2.maxsize(500, 500)
    root2.geometry("300x300+50+50")  # width x height + x + y
    text = Label(root2, font= "arial" , text="Choose the Ability and the Score to go with it.")
    
    text.pack()
   # text2 = Label(root2, font = "arial", text=dicetotal)
    #text2.pack()
    
    clicked = IntVar()
    clicked.set(dicetotal[0])
    menuTest = OptionMenu(root2, clicked, *dicetotal)
    menuTest.pack(side="left")
    abilities = StringVar()
    abilities.set(abilityScores[0])
    abilityTest = OptionMenu(root2, abilities,*abilityScores)
    abilityTest.pack(side="right")
    '''canvas = Canvas(root2, width=1000, height=750)
    canvas.create_text(300, 50, text=abilityScores, fill="black", font=('Helvectia 15 bold'))
    canvas.pack(side="left")
    #print("Your scores are: " , dicetotal)'''
    


root = tk.Tk()

# Creating a button with specified options
button = tk.Button(root, 
                   text="Click to generate scores", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

root.mainloop()