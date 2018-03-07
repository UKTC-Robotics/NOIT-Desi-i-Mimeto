import tkinter
import threading
import time
import serial

ard = serial.Serial('COM25', 9600)
top = tkinter.Tk()
top.geometry('500x500')
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




BV1 = tkinter.Button(top, text ="A0", font= 000000, bg="#00BFFF", fg="black", command = voltage1)
BV1.place(x=50, y=100)

BV2=tkinter.Button(top, text="A1",font= 000000,bg="#642EFE", command = voltage2)
BV2.place(x=100, y=100)

BCR=tkinter.Button(top, text ="A2", font= 000000, bg="#00BFFF", fg="black", command = current)
BCR.place(x=150, y=100)

BR=tkinter.Button(top, text ="A3", font= 000000, bg="#00BFFF", fg="black", command = res)
BR.place(x=200, y=100)

BC=tkinter.Button(top, text="CLOSE",font= 000000,bg="#642EFE", command = close)
BC.place(x=250, y=300)

Result = tkinter.Label()
Result.place(x=100, y=300)

Result.config(text = 'HELLO')

fun = threading.Thread(target=instrument_read)
fun.start()



top.mainloop()