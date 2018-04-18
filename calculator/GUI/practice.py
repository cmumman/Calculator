import Tkinter as tk
import ttk
from Tkinter import *

root = tk.Tk()
frame = ttk.Frame(root,padding=(10,10),borderwidth=100, relief = "sunken")
label = ttk.Label(root,text="Hello").pack()
check = ttk.Checkbutton(root,text="metic").pack()
button = ttk.Button(root,text="Hi",command="submitform").pack()
check1 = ttk.Checkbutton(root, text="Use Metric",command="metricChanged", variable="measureSystem",onvalue='metric', offvalue='imperial').pack()
phone = 9818675938
radio =ttk.Radiobutton(root,text="english",variable=phone, value='home').pack()
radio =ttk.Radiobutton(root,text="Hindi",variable=phone, value='home').pack()
name = StringVar()
entry = ttk.Entry(root,textvariable = name).pack()
print('current value is %s' % name.get())

countryvar = ["india","USA"]
country = ttk.Combobox(root, textvariable=countryvar).pack()
#input1 = StringVar()
#input1_entry = ttk.Entry(root,textvariable=input1)
#input1_entry.grid(column=2, row=1, sticky=("w", "e"))
#input1.set('New value to display')
root.mainloop()