from tkinter import *
from random import sample
root = Tk()
root.title('App')
root.iconbitmap('py.ico')

# menu_ch = StringVar()
# color = menu_ch.get()
# options = ['Red','Blue','Black','White','Yellow']


# def show(color):
#     OutWin = Toplevel()
#     OutWin.title('Another')
#     lbl = Label(OutWin,text='           ',background=color)
#     lbl.pack()
# menu = OptionMenu(root, menu_ch, *options, command=show)
# menu.pack()

# check = StringVar()
# def show():
#     lbl = Label(root,text=check.get())
#     lbl.pack()
# rdbtn1 = Radiobutton(root,text='True',variable=check,value='R1 Selected',command=show)
# rdbtn2 = Radiobutton(root,text='False',variable=check,value='R2 Selected',command=show)

# rdbtn1.select()
# rdbtn1.pack()
# rdbtn2.pack()

# cnt = IntVar()
# ent = Entry(root)
# ent.pack()
# value = sample(ent.get().split(','),cnt.get())
# lbl2 = Label(root,text=value)
# lbl2.pack()
# def selected():
#     lbl = Label(root,text=sample((ent.get()).split(','),cnt.get()))
#     lbl.pack()
# btn = Button(root,text='click',command=selected)
# btn.pack()
# sld = Scale(root,from_=1,to=10,orient=HORIZONTAL,variable=cnt,command=selected)
# sld.pack()


root.mainloop()