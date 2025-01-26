from tkinter import Tk, Label,Entry,Button

class Window:
    def __init__(self):
        self.win = Tk()
        self.win.title('my gui')
        self.win.geometry('500x500')
        self.win.configure(bg='pink')

        self.lblname=Label(master=self.win,text='ENTER NAME ',font=('consolas',18,'bold'))
        self.lblname.place(x=20 , y=20 , width=200 , height=50)

        self.ename=Entry(master=self.win,font=('consolas',18,'bold'))
        self.ename.place(x=250, y=20 ,width=200,height=50)

        self.btn_ok=Button(master=self.win,text='OK',font=('consolas',18,'bold'),command=self.show)
        self.btn_ok.place(x=20 , y=100 ,width=200,height=50)

        self.btn_clr=Button(master=self.win,text='CLEAR',font=('consolas',18,'bold'),command=self.clear)
        self.btn_clr.place(x=260 , y=100 , width=200 , height=50)

        self.win.mainloop()

    def show(self):
        self.ename.insert(0,'yashika hu mai')
    def clear(self):
        self.ename.delete(0,'end')

if __name__=='__main__':
    W=Window()