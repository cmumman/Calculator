import Tkinter as tk
import calculator.Functions.time
import ttk
from Tkinter import *
'''top = tk.Tk()
logo = tk.PhotoImage(file="tenor.gif")
a = tk.Label(top,compound = tk.RIGHT,image=logo,text="vardhan").pack(side="right")
#b = tk.Label(top,text="vardhan").pack()
top.mainloop()
root = tk.Tk()
tk.Label(root,text="green",fg="green").pack()
tk.Label(root,text="red",bg="red",fg="white").pack()
tk.Label(root,text="yellow",fg="yellow",bg="orange").pack(side="right")
tk.Button(root,text="stop",command=root.destroy).pack()
root.mainloop()

counter = 0
counter1 = 0

def count_label(label,label1):
    def count():
        global counter
        counter += 1
        count_milli(label1)
        label.config(text=str(counter))
        label.after(1000,count)

    def count_milli(label1):
        global counter1
        while counter1 <= 10:
            counter1 += 1
            label1.config(test=str(counter1))
            label1.after(100, count_milli)
    count()



root=tk.Tk()
root.title("seconds counter")

label = tk.Label(root,fg="red")
label.pack()
label1 = tk.Label(root,fg="blue")
label1.pack(side="right")
#count_label(label,label1)
button = tk.Button(root,width=50,text="Stop").pack()
button = tk.Button(root,width=50,text="Close",command=root.destroy).pack()
root.mainloop()
'''


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


root = tk.Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=("n", "w", "e", "s"))
#mainframe.columnconfigure(0, weight=1)
#mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=("w", "e"))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=("W", "E"))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky="W")

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky="W")
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky="E")
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky="W")

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
#root.bind('<Return>', calculate)

root.mainloop()