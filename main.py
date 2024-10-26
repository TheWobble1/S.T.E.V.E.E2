from tkinter import *
import subprocess

root = Tk()

root.title("S.T.E.V.E.E")
root.geometry('420x200')

def Trading_Capital():
    def clicked():
        res = "Confirmed: " + txt.get()
        lbl2.configure(text=res)

    lbl1 = Label(root, text="Trading Capital?")
    lbl1.grid(column=0, row=0)

    lbl2 = Label(root)
    lbl2.grid(column=3, row=0)

    btn1 = Button(root, text="Confirm",
                  fg="red", command=clicked)

    btn1.grid(column=2, row=0)

    txt = Entry(root, width=10)
    txt.grid(column=1, row=0)

def Initiate_Trading():
    def clicked():
        res = 'Initiating'
        lbl1.configure(text=res)
        subprocess.run(['python', 'DataDownload.py'])

    btn1 = Button(root, text='Start Trading',
                  fg='green', command=clicked)

    lbl1 = Label(root)
    lbl1.grid(column =2, row =1)

    btn1.grid(column=1, row=1)

Trading_Capital()
Initiate_Trading()
root.mainloop()