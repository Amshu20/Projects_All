import tkinter as tk
import random
def rando():
    global entry
    aa=entry.get()
    a,b=map(int,aa.split(','))
    label.config(text=f"Random Number:{random.randint(a,b)}")
root = tk.Tk()
entry = tk.Entry(root)
entry.insert(0,"")
label = tk.Label(root,text='...')
l1 = tk.Label(root,text='Enter the Min and Max value separated by comma')
l1.pack()
entry.pack()
btn = tk.Button(root,text='Randomize',command=rando)
btn.pack()
label.pack()
root.mainloop()