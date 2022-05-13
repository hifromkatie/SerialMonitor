import os
import machine
from machine import Pin, UART
import time

def new_serial(newLine,sDir):
    if len(screenList)>19:
        screenList.pop(0)
    newItem = []
    newItem.append(newLine)
    newItem.append(sDir)
    screenList.append(newItem)
    write_screen()

        

def write_screen():
    uartScreen.write(bytes([0xFF, 0xCD])) #clear screen
    uartScreen.write(bytes([0xFF, 0xCC, 0x00, 0x00, 0x00, 0x00]))#set origin ot 0,0UARTuartScreen.write(bytes([0xFF, 0xE7, 0xFF, 0xFF]))#forground/text colour white
    uartScreen.write(bytes([0xFF, 0xE6, 0x00, 0x00]))#background colour black
    uartScreen.write(bytes([0xFF, 0xE5, 0x00, 0x02])) #set font 3
    for i in range(len(screenList)):
        if screenList[i][1] == 0:
            uartScreen.write(bytes([0xFF, 0xDD, 0x00, 0x00])) #not italic
        else:
            uartScreen.write(bytes([0xFF, 0xDD, 0x00, 0x01])) #italic
        uartScreen.write(bytes([0x00, 0x18, ord(screenList[i][0]), 0x0a, 0x00])) #d 
    


screenList = []

intLED = Pin(25, Pin.OUT)
buttonA = Pin(16, Pin.IN, Pin.PULL_UP)
buttonB = Pin(17, Pin.IN, Pin.PULL_UP)
buttonC = Pin(18, Pin.IN, Pin.PULL_UP)
buttonD = Pin(19, Pin.IN, Pin.PULL_UP)

txScreen = Pin(4, Pin.OUT)
rxScreen = Pin(5, Pin.IN)
rstScreen = Pin(3, Pin.OUT, Pin.PULL_UP)

uartComms = UART(0, 9600)
uartScreen = UART(1, tx=txScreen,rx=rxScreen, baudrate = 9600)

rstScreen.value(0)
time.sleep(0.5)
rstScreen.value(1)
time.sleep(3) #wait 3 seconds before screen comms
uartScreen.write(bytes([0xFF, 0xCD])) #clear screen
uartScreen.write(bytes([0xFF, 0xCC, 0x00, 0x00, 0x00, 0x00]))#set origin ot 0,0
uartScreen.write(bytes([0xFF, 0xE7, 0xFF, 0xFF]))#forground/text colour white
uartScreen.write(bytes([0xFF, 0xE6, 0x00, 0x00]))#background colour black
uartScreen.write(bytes([0xFF, 0xE5, 0x00, 0x02])) #set font 3

while True:

    intLED.value(0)
    if buttonA.value()==0:
        uartComms.write(bytes([0x61, 0x0a]))
        new_serial("a",1)
        time.sleep(0.5)
    if buttonB.value()==0:
        uartComms.write(bytes([0x62, 0x0a]))
        new_serial("b",1)  
        time.sleep(0.5)
    if buttonC.value()==0:
        uartComms.write(bytes([0x63, 0x0a]))
        new_serial("c",1)       
        time.sleep(0.5)
    if buttonD.value()==0:
        uartComms.write(bytes([0x64, 0x0a]))
        new_serial("d",1)      
        time.sleep(0.5)
    #write_screen()
