from tkinter import *
import random

root = Tk()

root.title("RANDOM WORD GENERATOR")
root.geometry("500x500")

show_random_words = Label(root)

def randomAlpha():
    alpha_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z"]
    
    random_no1 = random.sample(range(1,26),1)
    random_no2 = random.sample(range(1,26),1)
    random_no3 = random.sample(range(1,26),1)
    random_no4 = random.sample(range(1,26),1)
    random_no5 = random.sample(range(1,26),1)

    random_alpha1 = alpha_list[random_no1]
    random_alpha2 = alpha_list[random_no2]
    random_alpha3 = alpha_list[random_no3]
    random_alpha4 = alpha_list[random_no4]
    random_alpha5 = alpha_list[random_no5]
    show_random_words["text"] = random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5 
    


btn = Button(root)
btn = Button(root, text="Who is your lucky friend?", command=randomAlpha)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

show_random_words.pack()
root.mainloop()