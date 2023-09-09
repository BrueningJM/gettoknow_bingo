import tkinter as tk



def shuffle():
    display= ["a \n","b \n"]
    lines = []
    f = open("Kennenlernen/Fragen Kennenlern-Bingo.txt","r")
    print(f.read())

shuffle()
f = open("Kennenlernen/Fragen Kennenlern-Bingo.txt","r")
display = ["a \n", "b \n"]
root = tk.Tk()
root.title("Kennlernbingo<3")
root.geometry("700x1000")
frm = tk.Frame(root)
frm.grid()
text = display[1]
tk.Label(frm, text="").grid(column=0, row=0, padx=30, pady=20)
tk.Label(frm, text="Mögliche Auswahl:\n", font=('times', 15)).grid(column=1, row=0)
T = tk.Text(frm, width=50, height=50 )
T.insert(1.0,"haha")
T.grid(column=1,row=1)
tk.Button(frm, text="Mischen", command=shuffle).grid(column=1, row=2)




root.mainloop()