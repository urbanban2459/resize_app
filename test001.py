import tkinter as tk

root = tk.Tk()
root.title("Python")
root.geometry("200x200")
btn = tk.Button(root, text="OK")
btn.pack()

#Label
lb = tk.Label(root, 
              text="Python",
              foreground='white', 
              background='blue',
              font = ('FixedSys','20','bold'))
lb.pack()


root.mainloop()