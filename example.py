import os
from motorLLC_sync import *
#import numpy as np
from dynamixel_sdk import * # Uses Dynamixel SDK library. If this make error, you can try with 'pip install dynamixel-sdk' on the terminal. 

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


MIN_POS_V  = 100               # Dynamixel will rotate between this value
MAX_POS_V  = 2000              # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
MOVING_STATUS_THRESHOLD = 100               # Dynamixel moving status threshold

motorNo = 4
motorIDs = [1, 2, 3, 4]
motorType = [2.0, 2.0, 2.0, 2.0]

mc = motorLLC()
mc.set_motor_IDs(motorNo, motorIDs, motorType)
mc.open()
mc.torque_enable()

pos0 = [2000, 1050, 1800, 1650]

pos1_1 = [2500, 1050, 1800, 1650]
pos1_2 = [1600, 1050, 1800, 1650]

pos2_1 = [2000, 1400, 1800, 1650]
pos2_2 = [2000, 700, 1800, 1650]

pos3_1 = [2000, 1050, 2200, 1650]
pos3_2 = [2000, 1050, 1400, 1650]

pos4_1 = [2000, 1050, 1800, 1900]
pos4_2 = [2000, 1050, 1800, 1400]


while 1:
    print(" o : ORIGIN \n t : M1 up / w : M1 down \n e : M2 up / r : M2 down \n a : M3 up / s : M3 down \n d : M4 up / f : M4 down \n esc : quit")
    
    if getch() == chr(0x6F): # o : origin
        mc.moveTo(pos0)
        
    if getch() == chr(0x71): # q : M1 up
        mc.moveTo(pos1_1)
        print("q : M1 up")
    if getch() == chr(0x77): # w : M1 down
        mc.moveTo(pos1_2)
        print("w : M1 down")
    if getch() == chr(0x65): # e : M2 up
        mc.moveTo(pos2_1)
        print("e : M2 up")
    if getch() == chr(0x72): # r : M2 down
        mc.moveTo(pos2_2)  
        rint("r : M2 down")          
    if getch() == chr(0x61): # a : M3 up
        mc.moveTo(pos3_1)
        print("a : M3 up")
    if getch() == chr(0x73): # s : M3 down
        mc.moveTo(pos3_2)
        print("s : M3 down")
    if getch() == chr(0x64): # d : M4 up
        mc.moveTo(pos4_1)
        print("d : M4 up")
    if getch() == chr(0x66): # f : M4 down
        mc.moveTo(pos4_2)
        print("f : M4 down")    

    if getch() == chr(0x1b):
        break
        
                
mc.close()
