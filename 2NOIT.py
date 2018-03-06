import tkinter
import serial


top = tkinter.Tk()
top.geometry('500x500')

def Result():
    print('It is working')
    msg = 'h'
    ard.write(msg.encode())

def Result2():
    print('It is working 22222')
    msg = 'l'
    ard.write(msg.encode())

ard = serial.Serial('COM11', 9600)

#boldFont = Font (size = 10, weight = "bold")

B = tkinter.Button(top, text ="Voltage in", font= 000000, bg="#642EFE", fg="black", command = Result2)
#B.place(x=75, y=100)
B.place(anchor="nw")

B1=tkinter.Button(top, text="Voltage out",font= 000000,bg="#642EFE", command = Result)
#B1.place(x=150, y=100)
#B1.place(anchor= "n")

B2=tkinter.Button(top, text="Electrical current ",font= 000000,bg="#642EFE", command = Result)
B2.place(x=200, y=200)


top.mainloop()