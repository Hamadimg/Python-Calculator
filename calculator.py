# importing the module
import tkinter as tk 

# creating main tkinter window/toplevel 
root = tk.Tk()
root.geometry("350x450")

main_window = tk.Frame(root)
main_window.pack(fill=tk.BOTH, expand=True)
#create display screen
screen_text = tk.StringVar()
Screen = tk.Label(main_window, textvariable= screen_text)
Screen.pack(fill=tk.BOTH, expand=True)

grid_section = tk.Frame(main_window)
grid_section.pack(fill=tk.BOTH, expand=True)

def resize(event):
    # Update the font size based on the height 
    # You may need to adjust the resizing factor depending on your setup
    newSize = -max(int(event.height / 3), 1)
    Screen.config(font=("TkDefaultFont", newSize))

Screen.bind('<Configure>', resize)



def update_screen(text):
    if text== "→":
        screen_text.set(eval(screen_text.get()))
    elif text == "c":
        screen_text.set("")
    else:
        screen_text.set(screen_text.get() + text)


def compute(screen_text):
    screen_text.set(eval(screen_text))

buttons = [{"row":0, "column":0, "text": "0"},
           {"row":0, "column":1, "text": "1"},
           {"row":0, "column":2, "text": "2"},
           {"row":0, "column":3, "text": "+"},
           {"row":1, "column":0, "text": "3"},
           {"row":1, "column":1, "text": "4"},
           {"row":1, "column":2, "text": "5"},
           {"row":1, "column":3, "text": "-"},
           {"row":2, "column":0, "text": "6"},    
           {"row":2, "column":1, "text": "7"},     
           {"row":2, "column":2, "text": "8"},    
           {"row":2, "column":3, "text": "*"},     
           {"row":3, "column":0, "text": "9"},    
           {"row":3, "column":1, "text": "/"},     
           {"row":3, "column":2, "text": "c"},    
           {"row":3, "column":3, "text": "→"},         
           ]

for button in buttons:
    
    tk_button = tk.Button(
    master=grid_section,
    borderwidth=1, activeforeground="yellow", text=button["text"], command=lambda btn_text=button["text"]: update_screen(btn_text))
    tk_button.grid(row=button["row"], column=button["column"], sticky="nsew")
    # tk_label = tk.Label(master=tk_button, text=button["text"])
    # tk_label.pack(padx=5, pady=5)
    grid_section.rowconfigure(button["row"], weight=1)
    grid_section.columnconfigure(button["column"], weight=1)
# Label for user input session

# Buttons on grid with numbers 0-9 and +-*/ and one clear, one delete and enter to calculate and replace label
    # Buttons on cli

# Start the GUI event loop
root.mainloop()