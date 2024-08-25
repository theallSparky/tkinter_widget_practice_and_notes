import tkinter as tk
from tkinter import ttk

def button_press_func():
    print('You pressed that button')

#tk widgets are the older, outdated looking widgets
#ttk widgets are the newer widgets which look as such

#create a window
window = tk.Tk()
# may be called root or app in other applications, but window works too
window.title('Window and widgets practice')
window.geometry('750x500')

#widgets

#tk
text = tk.Text(master = window) #multiline text input
text.pack() #.pack() places the widget in the middle at the top

#ttk widgets (the ones you want to use most often)
label = ttk.Label(master = window, text = 'This is a test label')
label.pack()

#ttk entry is a single line text entry field
entry = ttk.Entry(master = window)
entry.pack()

#button
button = ttk.Button(master = window, text = 'A button to press', command = button_press_func) # do not call the function in the command argument
button.pack()

#run
window.mainloop() # nothing after mainloop runs until the window is closed