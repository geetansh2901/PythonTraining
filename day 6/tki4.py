from tkinter import *

import tkinter.messagebox
root=Tk()

tkinter.messagebox.showinfo('Fuck', 'Jellyfishes are immortal')
answer=tkinter.messagebox.askquestion('Question 1','Do you like emojis?')

if answer=='yes':
    print('They are cancer')
root.mainloop()