import tkinter as tk


def shuffle():
    root.destroy()

root = tk.Tk()
root.title("Kennlernbingo<3")
root.geometry("700x1000")
frm = tk.Frame(root)
frm.grid()
tk.Label(frm, text="").grid(column=0, row=0, padx=30, pady=20)
tk.Label(frm, text="Mögliche Auswahl:\n", font=('times', 15)).grid(column=1, row=1)
tk.Button(frm, text="Mischen", command=shuffle()).grid(column=1, row=0)

root.mainloop()