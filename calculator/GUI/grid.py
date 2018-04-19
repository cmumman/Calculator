import Tkinter as tk
import ttk
from Tkinter import *
from Tkinter import *

top = tk.Tk()
root = ttk.Frame(top,padding=(3,3,12,12))
frame = ttk.Frame(root, borderwidth=1, relief="sunken", width=200, height=100)
namelbl = ttk.Label(root, text="Name")
name = ttk.Entry(root)

onevar = BooleanVar()
twovar = BooleanVar()
threevar  = BooleanVar()

onevar.set(True)
twovar.set(True)
threevar.set(True)



one = ttk.Checkbutton(root,text="one",variable=onevar, onvalue = True)
two = ttk.Checkbutton(root,text ="two",variable =twovar,onvalue= False)
three = ttk.Checkbutton(root,text="three",variable=threevar,onvalue=True)
Ok = ttk.Button(root,text="OK")
Cancel = ttk.Button(root,text="Cancel")
list_box = Listbox(root,height = 10)

root.grid(column=1,row=1,sticky=(N,S,E,W))

frame.grid(column=0,row=0,columnspan=3,rowspan=3,sticky=(N,S,E,W))
namelbl.grid(column=3,row=0)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
Ok.grid(column=3, row=3)
Cancel.grid(column=4, row=3)
list_box.grid(column=4,row=2)



root.mainloop()


