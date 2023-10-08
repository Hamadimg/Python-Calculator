# importing the module
import tkinter as tk 

# creating main tkinter window/toplevel 
root = tk.Tk()


main_window = tk.Frame(root)
main_window.pack(fill="both", expand=True)
#create display screen
Screen = tk.Label(main_window, text ="This is a Label")
Screen.pack()

grid_section = tk.Frame(main_window)
grid_section.pack(fill="both", expand=True)

# Creating 3x3 grid layout
for i in range(3):
   for j in range(3):
    #    frame = tk.Frame(
    #        master=grid_section,
    #        relief=tk.RAISED,
    #        borderwidth=1,
    #    )
       button = tk.Button(
           master=grid_section,
           borderwidth=1,)
       button.grid(row=i, column=j)         # Place the frame in the i -th row, j-th column

       label = tk.Label(master=button, text=f"Row {i}\nColumn {j}")
       label.pack(padx=5, pady=5)

 

# Start the GUI event loop
root.mainloop()