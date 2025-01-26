import math
import tkinter as ml
import time

window = ml.Tk()
window.title = (" Analog clock ")
window.geometry=("500x500")

def clk_work():
    sec=int(time.strftime("%S"))
    min=int(time.strftime("%M"))
    hours=int(time.strftime("%I"))

    sec_x=sec_hand_len*math.sin(math.radians(sec*6))+center_x
    sec_y=-1*sec_hand_len*math.cos(math.radians(sec*6))+center_y
    canvas.coords(sec_hand,center_x,center_y,sec_x,sec_y)

    min_x = min_hand_len * math.sin(math.radians(min * 6)) + center_x
    min_y = -1 * min_hand_len * math.cos(math.radians(min * 6)) + center_y
    canvas.coords(min_hand, center_x, center_y,min_x, min_y,)

    hours_x=hours_hand_len * math.sin(math.radians(hours * 30)) +center_x
    hours_y=-1*hours_hand_len*math.cos(math.radians(hours * 30))+center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    canvas.after(1000,clk_work)



canvas = ml.Canvas(width=500,height=500,bg='grey')
canvas.pack()

img=ml.PhotoImage(file="D:\clock-face-without-hands.png")
canvas.create_image(240,240,image=img)

sec_hand_len=150
min_hand_len=130
hours_hand_len=95
center_x=240
center_y=240

sec_hand=canvas.create_line(240,240,240+sec_hand_len,240+sec_hand_len,width=2.5,fill='black')
min_hand=canvas.create_line(240,240,240+min_hand_len,240+min_hand_len,width=3.5,fill='red')
hours_hand=canvas.create_line(240,240,240+hours_hand_len,240+hours_hand_len,width=3.5,fill='yellow')


clk_work()
window.mainloop()




