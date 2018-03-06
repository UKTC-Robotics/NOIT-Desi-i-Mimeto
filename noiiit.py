import serial

ard = serial.Serial('COM10', 9600)
for _ in range(10):
    values = []
    message = str(ard.readline())
    print (message)
    a = message.find('#')
    b = message.find('#', a + 1)
    values.append(int(message[a + 1 : b]))

    c = message.find('#', b + 1)
    values.append(int(message[b + 1: c]))

    d = message.find('#', c + 1)
    values.append (int(message[c + 1: d]))

    e = message.find('#', d + 1)
    values.append( int(message[d + 1: e]))

    f = message.find("#", e+1)
    values.append(int (message [e+1:f]))

    print("  ")
    print (values)

ard.close()
