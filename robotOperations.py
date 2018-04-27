import time
import os

X = 0
Y = 0
Z = 15000
R = 0

#24 selector bit 1 = claw, 0 = fingers
#23 operation bit 0 = close, 1 = open

def openFingers(ser): 
    writeSerialCommand(ser,b'@DO(24)=0\r')
    writeSerialCommand(ser,b'@DO(23)=1\r')

def closeFingers(ser):
    writeSerialCommand(ser,b'@DO(24)=0\r')
    writeSerialCommand(ser,b'@DO(23)=0\r')

def moveToOrigin(ser):
    writeSerialCommand(ser,b'@MOV %i %i %i %i\r' % (X, Y, Z, R))
    
def rotateToDeg(ser,angle):
    full_rotation = 100000
    R = (angle/360)*full_rotation
    writeSerialCommand(ser,b'@MOV %i %i %i %i\r' % (X, Y, Z, R))

def printResponse(ser):
    response = ser.read(100)
    print(response)

def writeSerialCommand(ser,command):
    time.sleep(0.01)
    ser.write(command)
    time.sleep(0.01)
    response = ser.read(100)
    print(response)
