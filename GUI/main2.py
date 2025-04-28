import tkinter as tk

root = tk.Tk()
root.title("grid")
root.geometry("300x300")


# btn_00.pack()

#row 0
btn_00 = tk.Button(root, text="btn 00", bg="#E395FF")
btn_00.grid(row=0, column=0, sticky="nsew", columnspan=3)
# btn_01 = tk.Button(root, text="btn 01")
# btn_01.grid(row = 0, column = 1, sticky="nsew")
# btn_02 = tk.Button(root, text="btn 02")
# btn_02.grid(row = 0, column = 2, sticky="nsew")
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# row 1
btn_10 = tk.Button(root, text="(1,0)")
btn_10.grid(row=1, column=0, sticky="nsew")

btn_11 = tk.Button(root, text="(1,1)")
btn_11.grid(row=1, column=1, sticky="nsew")

btn_12 = tk.Button(root, text="(1,2)")
btn_12.grid(row=1, column=2, sticky="nsew")

# row 2
btn_20 = tk.Button(root, text="(2,0)")
btn_20.grid(row=2, column=0, sticky="nsew")

btn_21 = tk.Button(root, text="(2,1)")
btn_21.grid(row=2, column=1, sticky="nsew")

btn_22 = tk.Button(root, text="(2,2)")
btn_22.grid(row=2, column=2, sticky="nsew")




root.mainloop()