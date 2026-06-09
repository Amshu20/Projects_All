import tkinter as tk
c=0
print(c)
def click():
    global c
    c+=1
    label.config(text=c)
def reset():
    global c
    c=0
    label.config(text=c)
root = tk.Tk()
label=tk.Label(root,text=c)
label.pack()
button = tk.Button(root,text="Click",command=click)
btn=tk.Button(root,text="Reset",command=reset)
button.pack()
btn.pack()
root.mainloop()