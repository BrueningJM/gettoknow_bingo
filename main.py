import tkinter as tk
import numpy as np
import time

cf = "Kennenlernen/Fragen Kennenlern-Bingo.txt"
df = "Kennenlernen/display.txt"

def display(filename):
    list = []
    f = open(filename, "r")
    list= f.readlines()
    #print(list)
    f.close()
    list = fix_string(list)
    return list

def shuffle(filename):
    display = []
    lines = []
    f = open(filename,"r")
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
        if newline in display:
            print(newline)
            continue
        elif newline == "":
            print(newline)
            continue
        else:
            display.append(newline)
            n += 1
            #print(n)

    #print(display)
    f = open("Kennenlernen/display.txt", "w")
    for k in display:
        #print(k)
        f.write(k)
    f.close()

def fix_string(list):
    count = len(list)
    #print(count)
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
        #Dieses eine behinderte e was Dustin unbedingt bei Pokemon einfügen musste AHHHHHHH
        if "Ã©" in list[i]:
            list[i] = list[i].replace("Ã©","é")
            #print(list[i])
    return list

def text(text, content):
    inscount = len(content)
    text.delete(1.0,'end')
    for i in range(0, inscount):
        text.insert('end', content[i])


shuffle(cf)
disp = display(df)

root = tk.Tk()
root.title("Kennlernbingo<3")
root.geometry("700x1000+650+0")

fra = tk.Frame(root)
fra.pack(fill=tk.BOTH, expand=1)
mycanvas = tk.Canvas(fra)
mycanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
scrollbar = tk.Scrollbar(fra,orient=tk.VERTICAL,command=mycanvas.yview())
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
mycanvas.configure(yscrollcommand=scrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))

frm = tk.Frame(mycanvas)
mycanvas.create_window((0,0), window=frm,anchor="nw")
frm.grid()




def draw_num():
    Numfield = tk.Toplevel(root)
    Numfield.title("Die Nummer ist:")
    Numfield.geometry("600x600+700+250")
    #fra.grid()
    num = np.random.randint(1,51)

    Input = T.get(1.0,'end')
    Input = Input.split("\n")
    for k in Input:
        if (str(num) + ".") in k:
            temp = k.replace((str(num) + "."),"")
            n = 0
            disp_att = ""
            for l in temp:
                disp_att += l
                if n > 24 and l == " " :
                    disp_att += "\n"
                    n= 0
                n += 1
                #print(n)
            break
        else:
            continue


    tk.Label(Numfield, text=str(num), font=('times', 70)).place(x=250,y=20)
    tk.Label(Numfield, text=str(disp_att), font=('times', 25)).place(x=50,y=225)

    tk.Button(Numfield,
              text="OK",
              font=('times',30),
              command=lambda: [Numfield.withdraw()],
              ).place(x=250,y=400)
    time.sleep(0.5)

def take_input():
    Add = f_input.get()
    print(Add)
    Add = "	" + Add + "\n"
    f = open(cf,"a")
    f.write(Add)
    f.close()

tk.Label(frm, text="").grid(column=0,row=0, padx=20)
tk.Label(frm, text="Mögliche Auswahl:\n", font=('times', 15)).grid(column=1, row=1,columnspan=2)
T = tk.Text(frm, width=75, height=51 )
text(T, disp)
T.grid(column=1,row=2,columnspan=4)
tk.Button(frm,
          text="Mischen",
          command=lambda: [shuffle(cf),text(T,display(df))],
          font=('times', 15)
          ).grid(column=1, row=3, pady=5)
tk.Button(frm, text="Nummer",
          command=draw_num,
          font=('times', 15)
          ).grid(column=2,row=3,pady=5)
f_input = tk.Entry(frm, width=100)
f_input.grid(column=1,row=4,columnspan=3)
tk.Button(frm, text = "  Dazu  ",
          command=take_input,
          font=('times', 15)
          ).grid(column=1,row=5)




root.mainloop()