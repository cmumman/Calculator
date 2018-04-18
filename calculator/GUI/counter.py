import Tkinter as tk

counter = 0


def count_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

loop = tk.Tk()

loop.title("counting seconds")
label = tk.Label(loop, fg="red")
label.pack()
count_label(label)
button = tk.Button(loop, text="stop", width=50, command=loop.destroy).pack()
loop.mainloop()
