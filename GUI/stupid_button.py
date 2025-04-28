import tkinter as tk
import random

root = tk.Tk()
root.title("click me if you can")
root.geometry("400x300")

button = tk.Button(root, text="click mee", font=("Helvetica", 16))
button.place(x=150, y=120)

def move_button(event):
    print("hover!")
    button.place(x=random.randint(0,300), y=random.randint(0,200))



button.bind("<Enter>", move_button)

root.mainloop()