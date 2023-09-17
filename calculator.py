# importing the module
import tkinter as tk 

# creating main tkinter window/toplevel 
master = tk.Tk() 

# this wil create a label widget 
l1 = tk.Label(master, text ="This is a Label") 
l1.pack()

# button widget with 'Button' as label 
b = tk.Button(master, text ="This is a Button")
b.pack()

# Start the GUI event loop
master.mainloop()
