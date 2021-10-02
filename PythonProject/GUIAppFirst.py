from random import choice
from tkinter import *
import time
cnt = 0
def on_click():
    global cnt
    cnt += 1
    list = txt.get().split(',')
    lbl = Label(app,text=(choice(list)),relief='ridge',borderwidth=10)
    lbl.grid(row=0,column=2,columnspan=2,padx=15)
    if btn_quit['state'] == DISABLED and txt.get().strip() != '' :
        btn_quit['state'] = NORMAL
    # if cnt > 2:
    #     lbl['text'] = ''
    #     cnt = 0

app = Tk()
app['background'] = 'magenta'
app.title('Random Picker')
app.geometry('500x200')

txt = Entry(app)
txt.grid(row=0,column=0,columnspan=2,padx=15,pady=5)

btn = Button(app,text='Click',command=on_click,font=('Courier',15),foreground='red',background='#2A3b4E')
btn.grid(row=1,column=0,padx=9,pady=2)

btn_quit = Button(app,text='quit',command=app.quit,state=DISABLED)
btn_quit.grid(row=1,column=1,padx=11,pady=2)

app.mainloop()
