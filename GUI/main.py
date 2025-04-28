import tkinter as tk
import random 


root = tk.Tk()
root.title("D20 Roller")
root.geometry("300x200")

result_label = tk.Label(root, text="", font=("Helvetica", 48), width=2, borderwidth=2, relief="solid")

def roll_dice():
    roll = random.randint(0,20)
    result_label.config(text=str(roll))
    if roll == 10 or roll == 16 or roll == 12 or roll == 11 or roll == 4:
        root.config(bg="#E395FF")
    else:
        root.config(bg="white")




result_label.pack(pady=20)

roll_button = tk.Button(root, text=" roll the dice", command=roll_dice)
roll_button.pack()

root.mainloop()





