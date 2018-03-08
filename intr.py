import tkinter
import threading
import time
import serial

ard = serial.Serial('COM25', 9600)
top = tkinter.Tk()
top.geometry('600x500')

kakvo = 0
def valmap(value, istart, istop, ostart, ostop):
  return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def instrument_read():
    global kakvo
    while True:
     values = []
     message = str(ard.readline())
     a = message.find('#')
     b = message.find('#', a + 1)
     values.append(int(message[a + 1: b]))

     c = message.find('#', b + 1)
     values.append(int(message[b + 1: c]))

     d = message.find('#', c + 1)
     values.append(int(message[c + 1: d]))

     e = message.find('#', d + 1)
     values.append(int(message[d + 1: e]))

     f = message.find("#", e + 1)
     values.append(int(message[e + 1:f]))

     values[0] = valmap(values[0], 0, 1023, 0, 5)
     values[1] = valmap(values[1], 0, 1023, 0, 10)
     values[2] = (((values[2]/1024) * 5000 - 2500) / 66) * 1000
     Result.config(text=values[kakvo])

     print(values[kakvo])

     if kakvo==1:
         pr.config(text= "V")
     elif kakvo == 0:
         pr.config(text="V")
     elif kakvo==2:
         pr.config(text="mA")
     elif kakvo==3:
         pr.config(text="ohm")

def voltage1():
    global kakvo
    kakvo = 0

def current():
    global kakvo
    kakvo = 2


def voltage2():
    global kakvo
    kakvo = 1


def res():
    global kakvo
    kakvo = 3


def close():
    ard.close()
    top.quit()



hb = 1
wb = 25
BV1 = tkinter.Button(top, text ="НАПРЕЖЕНИЕ 0-5V", font= 000000, bg="#cc6699", fg="black", command = voltage1,  height=hb, width= wb, activebackground= "#cc0066" )
BV1.place(x=15, y=100)

BV2=tkinter.Button(top, text="НАПРЕЖЕНИЕ 5-10V",font= 000000,bg="#cc6699", command = voltage2,   height=hb, width= wb, activebackground= "#cc0066" )
BV2.place(x=310, y=100)

BCR=tkinter.Button(top, text ="ГОЛЕМИНА НА ТОКА О-20А", font= 000000, bg="#cc6699", fg="black", command = current, height=hb, width= wb,activebackground= "#cc0066")
BCR.place(x=15, y=200)

BR=tkinter.Button(top, text ="СЪПРОТИВЛЕНИЕ 1-50k", font= 000000, bg="#cc6699", fg="black", command = res,  height=hb, width= wb , activebackground= "#cc0066",)
BR.place(x=310, y=200)

BC=tkinter.Button(top, text="CLOSE",font= 000000,bg="#cc0000", command = close, activebackground= "red")
BC.place(x=330, y=300)


pr= tkinter.Label()
pr.place(x=220, y=300)

Result = tkinter.Label()
Result.place(x=100, y=300)  #надписна кутия

Result.config(text = 'HELLO')



fun = threading.Thread(target=instrument_read)
fun.start()



top.mainloop()