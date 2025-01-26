from tkinter import Tk, Entry, Button

class Window:
    def __init__(self):
        self.win = Tk()
        self.win.title('My GUI File')
        self.win.geometry('500x500')
        self.win.configure(bg="lightblue")

        self.enamey = Entry(master=self.win, font=('consolas', 18, 'bold'),)
        self.enamey.place(x=20, y=20, width=200, height=50)

        self.enamex = Entry(master=self.win, font=('consolas', 18, 'bold'))
        self.enamex.place(x=250, y=20, width=200, height=50)


        self.btn_ok = Button(master=self.win, text='copy', font=('consolas', 18, 'bold'), command=self.show)
        self.btn_ok.place(x=20, y=100, width=200, height=50)

        self.btn_cancel = Button(master=self.win, text='CANCEL', font=('consolas', 18, 'bold'), command=self.clear)
        self.btn_cancel.place(x=260, y=100, width=200, height=50)

        self.win.mainloop()

    def show(self):

        self.enamey.insert(0, 'Yashika')
        self.enamex.insert(0,'yashika')



    def clear(self):
        self.enamex.delete(0, 'end')
        self.enamey.delete(0, 'end')


if __name__ == '__main__':
    W = Window()
