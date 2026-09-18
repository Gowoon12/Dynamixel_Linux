import os
from motorLLC_sync import *
from dynamixel_sdk import *

if os.name == 'nt':
    import msvcrt

    def getch():
        return msvcrt.getch().decode()

else:
    import sys
    import tty
    import termios

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch


# Motor settings
motorNo = 4
motorIDs = [1, 2, 3, 4]
motorType = [2.0, 2.0, 2.0, 2.0]

mc = motorLLC()
mc.set_motor_IDs(motorNo, motorIDs, motorType)
mc.open()
mc.torque_enable()

# Position settings
pos0 = [2000, 1050, 1800, 1650]

pos1_1 = [2500, 1050, 1800, 1650]
pos1_2 = [1600, 1050, 1800, 1650]

pos2_1 = [2000, 1400, 1800, 1650]
pos2_2 = [2000, 700, 1800, 1650]

pos3_1 = [2000, 1050, 2200, 1650]
pos3_2 = [2000, 1050, 1400, 1650]

pos4_1 = [2000, 1050, 1800, 1900]
pos4_2 = [2000, 1050, 1800, 1400]

print(
    "\n"
    "o : ORIGIN\n"
    "q : M1 up / w : M1 down\n"
    "e : M2 up / r : M2 down\n"
    "a : M3 up / s : M3 down\n"
    "d : M4 up / f : M4 down\n"
    "ESC : quit\n"
)

while True:

    key = getch()

    if key == 'o':
        mc.moveTo(pos0)
        print("o : ORIGIN")

    elif key == 'q':
        mc.moveTo(pos1_1)
        print("q : M1 up")

    elif key == 'w':
        mc.moveTo(pos1_2)
        print("w : M1 down")

    elif key == 'e':
        mc.moveTo(pos2_1)
        print("e : M2 up")

    elif key == 'r':
        mc.moveTo(pos2_2)
        print("r : M2 down")

    elif key == 'a':
        mc.moveTo(pos3_1)
        print("a : M3 up")

    elif key == 's':
        mc.moveTo(pos3_2)
        print("s : M3 down")

    elif key == 'd':
        mc.moveTo(pos4_1)
        print("d : M4 up")

    elif key == 'f':
        mc.moveTo(pos4_2)
        print("f : M4 down")

    elif key == chr(0x1b):
        print("Quit")
        break

mc.close()
