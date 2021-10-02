from tkinter import * 

root = Tk()
check = StringVar()
def show():
    lbl = Label(root, text=check.get(),relief='raised',borderwidth=2,font=15,width=15)
    lbl.grid(row=2,column=0,columnspan=2,pady=(4,0))


chk = Checkbutton(root, text='Checkbox',pady=4,variable=check,command=show,onvalue='Secilib',offvalue='Secilmeyib')
chk.grid(row=0,column=0,columnspan=2)


btn = Button(root,text='Click',relief='ridge',background='black',foreground='yellow',command=show)
btn.grid(row=1,column=0,columnspan=2)
root.mainloop()