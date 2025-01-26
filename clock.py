from tkinter import *
import time

class Clock:
    def __init__(self):
        self.clk=Tk()
        self.clk.title('Digital Clock')
        self.clk.geometry('500x500')
        self.clk.configure(bg='pink')

        self.lblclk=Label(master=self.clk,text='00:00:00',font=('consolas',20,'bold'))
        self.lblclk.pack()
        self.update_clk()

    def update_clk(self):

        hours=time.strftime('%I')
        minutes=time.strftime('%M')
        second=time.strftime('%S')
        am_or_pm=time.strftime('%p')

        time_text=hours + ':' + minutes + ':' + second + '  ' + am_or_pm
        self.lblclk.configure(text=time_text)
        self.clk.after(1000,self.update_clk)




if __name__ == '__main__':
        C = Clock()
        C.clk.mainloop()


