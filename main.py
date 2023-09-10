import tkinter as tk
import numpy as np

def display(filename):
    list = []
    f = open(filename, "r")
    list= f.readlines()
    print(list)
    f.close()
    return list

def shuffle():
    display = []
    lines = []
    f = open("Kennenlernen/Fragen Kennenlern-Bingo.txt","r")
    lines = f.readlines()
    f.close()
    licount = len(lines)
    #print(f.read())
    n = 0
    while n < 50:
        rn = np.random.randint(0, licount)
        newline = lines[rn]
        newline = newline.replace("\t", "")
        newline = str(n+1) + ". " + newline
        #print(newline)
        if newline not in display:
            display.append(newline)
            n += 1

    print(display)
    f = open("Kennenlernen/display.txt", "w")
    for k in display:
        #print(k)
        f.write(k)
    f.close()


shuffle()
disp = display("Kennenlernen/display.txt")

root = tk.Tk()
root.title("Kennlernbingo<3")
root.geometry("700x1000")
frm = tk.Frame(root)
frm.grid()
tk.Label(frm, text="").grid(column=0, row=0, padx=30, pady=20)
tk.Label(frm, text="Mögliche Auswahl:\n", font=('times', 15)).grid(column=1, row=0)
T = tk.Text(frm, width=60, height=53 )
inscount = len(disp)
for i in range(0,inscount):
    T.insert('end', disp[i])
T.grid(column=1,row=1)
tk.Button(frm, text="Mischen", command=shuffle).grid(column=1, row=2)




root.mainloop()