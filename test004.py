import tkinter as tk

root = tk.Tk()
root.title("Packer")
root.geometry("200x200")
color = ('red','blue','green','yellow')

#ラベルの作成
for x in range(4):
    label = tk.Label(root, text="Label{}".format(x),background=color[x])
    label.pack(fill = 'both')

root.mainloop()