'''This program is will contain labels 
and buttons  '''

from tkinter import *
from tkinter import ttk

root = Tk()

# Create button and labels
# Where do we want it - root and the text
lbltitle = ttk.Label(text='Sunshine Adventure Camp', font=(('Arial'), 15))
lbltitle.grid(row=0, column=0, columnspan=4, pady=10)

root.geometry('400x370+650+350') 
root.mainloop()
