import tkinter as tk

root = tk.Tk()
root.title("grid")
root.geometry("300x300")

# for i in range(9)
#     button_name="btn_" + i
#     button_name = tk.Button(root, text="btn"+i)
#     button_name.grid(row=i+, column = 0 )

for i in range(9):
    btn = tk.Button(
        root,
        text=f"Button {i+1}",
        # bg=colors[i],
        fg='black',
        width=15,
        height=2,
        
    )

    btn.grid(row=i//3, column= ((i%3)), padx=10, pady=5, sticky="nsew")

# btn = tk.Button(root, text="btn 00", bg="#E395FF")
# btn.grid(row=0, column=0, sticky="nsew", columnspan=3)

root.mainloop()