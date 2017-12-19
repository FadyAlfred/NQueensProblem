from tkinter import *
import NQueensProblem


root = Tk()
root.geometry("1000x1000")
boardFrame = Frame(root, width=1000, height=1000)
boardFrame.place(anchor="c", relx=.5, rely=.5)
whites = []
board = [None] * 32
var = StringVar(root)
img = PhotoImage(file="Queen1.png")

def sel():
    selection = var.get()
    return selection



def convertList(list):
    for l in range(len(list)):
        Matrix = [[0 for x in range(list.__len__())] for y in range(list.__len__())]
        for n in range(len(list)):
             value = list[n]
             for m in range(len(list)):
                 if (value == (m)):
                     Matrix[n][m] = 1
    return Matrix



def draw(rows,columns,Matrix):
    for i in range(rows):
        for j in range(columns):
            value=Matrix[i][j]
            if (i % 2 == 0):
                if (j % 2 == 0):
                  if(value==1):
                      whiteLabel = Label(boardFrame,image=img, bg="white").grid(row=i, column=j)
                  else:
                      whiteLabel = Label(boardFrame, bg="white", width=10, height=4).grid(row=i, column=j)
                else:
                  if(value==1):
                      whiteLabel = Label(boardFrame,image=img, bg="black").grid(row=i, column=j)
                  else:
                      blackLabel = Label(boardFrame, bg="black", width=10, height=4,).grid(row=i, column=j)

            else:
                if (j % 2 == 0):
                  if(value==1):
                      whiteLabel = Label(boardFrame,image=img, bg="black").grid(row=i, column=j)
                  else:
                      blackLabel = Label(boardFrame, bg="black", width=10, height=4).grid(row=i, column=j)

                else:
                  if(value==1):
                      whiteLabel = Label(boardFrame,image=img, bg="white").grid(row=i, column=j)
                  else:
                      whiteLabel = Label(boardFrame, bg="white", width=10, height=4).grid(row=i, column=j)

def callback(list):
    selection=sel()
    if(selection == "4x4"):
        if(len(convertList(list))==4):
            draw(4,4,convertList(list))
    if (selection == "5x5"):
        if (len(convertList(list)) == 5):
            draw(5, 5, convertList(list))
    if (selection == "6x6"):
        if (len(convertList(list)) == 6):
            draw(6, 6, convertList(list))
    if (selection == "7x7"):
        if (len(convertList(list)) == 7):
            draw(7, 7, convertList(list))
    if (selection == "8x8"):
        if (len(convertList(list)) == 8):
            draw(8, 8, convertList(list))
    if (selection == "9x9"):
        if (len(convertList(list)) == 9):
            draw(9, 9, convertList(list))
    if (selection == "10x10"):
        if (len(convertList(list)) == 10):
            draw(10, 10, convertList(list))
    #mbutton1.config(state="disable")
    mbutton2.config(state="normal")
    mbutton3.config(state="normal")


def pickNumber():
    selection = sel()
    if (selection == "4x4"):
        global lists
        lists = NQueensProblem.call_place(4)
    if (selection == "5x5"):
        global lists
        lists = NQueensProblem.call_place(5)
    if (selection == "6x6"):
        global lists
        lists = NQueensProblem.call_place(6)
    if (selection == "7x7"):
        global lists
        lists = NQueensProblem.call_place(7)
    if (selection == "8x8"):
        global lists
        lists = NQueensProblem.call_place(8)
    if (selection == "9x9"):
        global lists
        lists = NQueensProblem.call_place(9)
    if (selection == "10x10"):
        global lists
        lists = NQueensProblem.call_place(10)
    mbutton1.config(state="normal")


counter=1
emptyList=[]

def next(lists):
    global counter
    if(-1<counter<len(lists)):
        if(counter==0):
            counter = counter + 2
            list=lists[counter-1]
            print(counter)
            callback(list)
        else:
            counter = counter + 1
            list = lists[counter - 1]
            print(counter)
            callback(list)


def previous(lists):
    global counter
    if(0<counter<len(lists)+1):
        if(counter==len(lists)):
            counter = counter - 2
            list = lists[counter]
            print(counter)
            callback(list)
        else:
            counter = counter - 1
            list=lists[counter]
            print(counter)
            callback(list)

option=["4x4","5x5","6x6","7x7","8x8","9x9","10x10"]

w = OptionMenu(root,var,*option)
var.set("8x8")
w.configure(background='white')
w.pack()
mbutton1 = Button(text="Start", relief=GROOVE,command=lambda:callback(lists[0]))
mbutton2 = Button(text="Next", relief=GROOVE,command=lambda:next(lists))
mbutton3 = Button(text="Previous", relief=GROOVE,command=lambda:previous(lists))
mbutton4 = Button(text="set", relief=GROOVE,command=lambda:pickNumber())
mbutton4.configure(background='white')
mbutton4.pack()
mbutton1.configure(background='white')
mbutton1.config(state="disable")
mbutton1.pack()
mbutton2.configure(background='white')
mbutton2.config(state="disable")
mbutton2.pack(anchor=E)
mbutton3.configure(background='white')
mbutton3.config(state="disable")
mbutton3.pack(anchor=W)

root.mainloop()




