import serial
import time

# XBee setting
serdev = '/dev/ttyUSB3'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())

s.write("ATMY 0x103\r\n".encode())
char = s.read(3)
print("Set MY 0x103.")
print(char.decode())

s.write("ATDL 0x203\r\n".encode())
char = s.read(3)
print("Set DL 0x203.")
print(char.decode())

s.write("ATID 0x1\r\n".encode())
char = s.read(3)
print("Set PAN ID 0x1.")
print(char.decode())

s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())

s.write("ATMY\r\n".encode())
char = s.read(4)
print("MY :")
print(char.decode())

s.write("ATDL\r\n".encode())
char = s.read(4)
print("DL : ")
print(char.decode())

s.write("ATCN\r\n".encode())
char = s.read(3)
print("Exit AT mode.")
print(char.decode())

print("start sending RPC")

# send RPC to remote
s.write("/myled3/write 1\r".encode())
while True:
    line = s.read(20)
    print(line.decode())

s.close()