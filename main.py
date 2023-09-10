import tkinter as tk
import numpy as np

def display(filename):
    list = []
    f = open(filename, "r")
    list= f.readlines()
    print(list)
    f.close()
    list = fix_string(list)
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

    #print(display)
    f = open("Kennenlernen/display.txt", "w")
    for k in display:
        #print(k)
        f.write(k)
    f.close()

def fix_string(list):
    count = len(list)
    print(count)
    for i in range(0,count):
        #fix für ä
        if "Ã¤" in list[i]:
            list[i] = list[i].replace("Ã¤","ä")
            #print(list[i])
        # fix für ö
        if "Ã¶" in list[i]:
            list[i] = list[i].replace("Ã¶","ö")
            #print(list[i])
        #fix für ü
        if "Ã¼" in list[i]:
            list[i] = list[i].replace("Ã¼","ü")
            #print(list[i])
        # fix für Ä
        if "Ã„" in list[i]:
            list[i] = list[i].replace("Ã„", "Ä")
            #print(list[i])
        # fix für Ö
        if "Ã–" in list[i]:
            list[i] = list[i].replace("Ã–", "Ö")
            #print(list[i])
        # fix für ü
        if "Ãœ" in list[i]:
            list[i] = list[i].replace("Ãœ", "Ü")
            #print(list[i])
        # fix für ß
        if "ÃŸ" in list[i]:
            list[i] = list[i].replace("ÃŸ","ß")
            #print(list[i])
        #Dieses eine behinderte e ws Vasi unbedingt bei Pokemon einfügen musste AHHHHHHH
        if "Ã©" in list[i]:
            list[i] = list[i].replace("Ã©","é")
            #print(list[i])
    return list

def text(text, content):
    inscount = len(content)
    text.delete(1.0,'end')
    for i in range(0, inscount):
        text.insert('end', disp[i])

shuffle()
disp = display("Kennenlernen/display.txt")

root = tk.Tk()
root.title("Kennlernbingo<3")
root.geometry("700x1000")
frm = tk.Frame(root)
frm.grid()
tk.Label(frm, text="").grid(column=0, row=0, padx=30, pady=20)
tk.Label(frm, text="Mögliche Auswahl:\n", font=('times', 15)).grid(column=1, row=0)
T = tk.Text(frm, width=70, height=53 )
text(T, disp)
T.grid(column=1,row=1)
tk.Button(frm, text="Mischen", command=shuffle).grid(column=1, row=2)


root.mainloop()