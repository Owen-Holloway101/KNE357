
import serial
import time
from robotOperations import openFingers
from robotOperations import closeFingers
from robotOperations import moveToOrigin
from robotOperations import rotateToDeg
from robotOperations import writeSerialCommand

port = "COM1"
baud = 9600
termination = '\r'

with serial.Serial(port,baud,timeout=1,parity=serial.PARITY_NONE, xonxoff=0) as ser:
    #moveToOrigin(ser)
    #rotateToDeg(ser,180)
    #writeSerialCommand(ser,b'@P1=10000 10000 0 0\r')
    #writeSerialCommand(ser,b'@P2=20000 10000 0 0\r')
    #writeSerialCommand(ser,b'@P3=20000 30000 0 0\r')
    #writeSerialCommand(ser,b'@P4=10000 30000 0 0\r')
    #writeSerialCommand(ser,b'@CP P1, P2, P3, P4\r')
    openFingers(ser)
    time.sleep(1.5)
    closeFingers(ser)
    #time.sleep(1)
    response = ser.read(100)
    print(response)
    ser.close()


