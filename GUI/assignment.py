import tkinter as tk



def on_resize(event):
 
 #setting size
    current_width = root.winfo_width()
    current_height = root.winfo_height()
    
    # setting how much to re-size
    width_change = current_width - previous_size[0]
    height_change = current_height - previous_size[1]
    
    # invertng resize
    new_width = current_width - width_change * 2
    new_height = current_height - height_change * 2
    
    # applying sizing
    new_width = max(new_width, 200)  # Prevent window from disappearing
    new_height = max(new_height, 200)
    root.geometry(f"{new_width}x{new_height}")
    
    # Update previous size for next event
    previous_size[0] = new_width
    previous_size[1] = new_height

root = tk.Tk()
root.title("Inverse Resize Window")
root.geometry("400x400")

# Track previous size
previous_size = [400, 400]

# Bind the resize event
root.bind("<Configure>", on_resize)

main_label = tk.Label(root, text="try to re-size box dimensions")
main_label.pack(pady=20)

main_button = tk.Button(root, text="Confirm!", font=("Helvetica", 14))
main_button.pack(pady=10)

root.mainloop()