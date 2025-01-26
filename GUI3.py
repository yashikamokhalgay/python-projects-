from tkinter import Tk, Entry, Button

class Window:
    def __init__(self):
        self.win = Tk()
        self.win.title('My GUI File')
        self.win.geometry('700x700')
        self.win.configure(bg="lightblue")

        self.enamex = Entry(master=self.win, font=('consolas', 18, 'bold'))
        self.enamex.place(x=20, y=20, width=100, height=50)

        self.enamey = Entry(master=self.win, font=('consolas', 18, 'bold'))
        self.enamey.place(x=150, y=20, width=100, height=50)

        self.enamez = Entry(master=self.win, font=('consolas', 18, 'bold'))
        self.enamez.place(x=350, y=20, width=150, height=50)


        self.btn_add = Button(master=self.win, text='+', font=('consolas', 18, 'bold'), command=self.add)
        self.btn_add.place(x=20, y=90, width=100, height=50)

        self.btn_sub = Button(master=self.win, text='-', font=('consolas', 18, 'bold'), command=self.sub)
        self.btn_sub.place(x=150, y=90, width=100, height=50)

        self.btn_mul = Button(master=self.win, text='*', font=('consolas', 18, 'bold'), command=self.mul)
        self.btn_mul.place(x=280, y=90, width=100, height=50)

        self.btn_div = Button(master=self.win, text='/', font=('consolas', 18, 'bold'), command=self.div)
        self.btn_div.place(x=20, y=180, width=100, height=50)

        self.btn_floor = Button(master=self.win, text='//', font=('consolas', 18, 'bold'), command=self.floor)
        self.btn_floor.place(x=150, y=180, width=100, height=50)

        self.btn_mod = Button(master=self.win, text='%', font=('consolas', 18, 'bold'), command=self.mod)
        self.btn_mod.place(x=280, y=180, width=100, height=50)

        self.btn_cancel = Button(master=self.win, text='CLEAR', font=('consolas', 18, 'bold'), command=self.clear)
        self.btn_cancel.place(x=20, y=270, width=200, height=50)

        self.win.mainloop()

    def add(self):
        n1=int(self.enamex.get())
        n2=int(self.enamey.get())
        n3=n1+n2
        self.enamez.insert(0,n3)

    def sub(self):
        n1 = int(self.enamex.get())
        n2 = int(self.enamey.get())
        n3 = n1 - n2
        self.enamez.insert(0, n3)

    def mul(self):
        n1 = int(self.enamex.get())
        n2 = int(self.enamey.get())
        n3 = n1 * n2
        self.enamez.insert(0, n3)

    def div(self):
        n1 = int(self.enamex.get())
        n2 = int(self.enamey.get())
        n3 = n1 / n2
        self.enamez.insert(0, n3)

    def floor(self):
        n1 = int(self.enamex.get())
        n2 = int(self.enamey.get())
        n3 = n1 // n2
        self.enamez.insert(0, n3)

    def mod(self):
        n1 = int(self.enamex.get())
        n2 = int(self.enamey.get())
        n3 = n1 % n2
        self.enamez.insert(0, n3)

    def clear(self):
        self.enamex.delete(0, 'end')
        self.enamey.delete(0, 'end')
        self.enamez.delete(0,'end')


if __name__ == '__main__':
    W = Window()
