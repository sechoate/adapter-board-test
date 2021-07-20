import wiringpi as pi
from time import sleep
import numpy as np

#output files
connected_file = 'final_connected.txt'  #output for connected pins, should be 1
adjacent_file = 'final_adj.txt'  #output for every other pin, should be 0
ground_file = 'ground.txt' #output for ground pins, should be 0

#setup
pi.wiringPiSetup()
pi.mcp23017Setup(177,0x27)
pi.mcp23017Setup(145,0x25)
pi.mcp23017Setup(129,0x24)
pi.mcp23017Setup(113,0x23)
pi.mcp23017Setup(161,0x26)
pi.mcp23017Setup(97,0x22)
pi.mcp23017Setup(81,0x21)
pi.mcp23017Setup(65,0x20)

def reset():  #define reset function to set all expanders to 0 V, run before every pin
    #0x20 expander, pins 65-80, set to V = 0
    for j0 in list(range(65,81)):
        pi.pinMode(j0,1)  #set to output
        pi.digitalWrite(j0,0)  #set to low voltage
    #0x21 expander, pins 81-96, set V = 0
    for j1 in list(range(81,97)):
        pi.pinMode(j1,1)
        pi.digitalWrite(j1,0)
    #0x22 expander, pins 97-112, set V = 0
    for j2 in list(range(97,113)):
        pi.pinMode(j2,1)
        pi.digitalWrite(j2,0)
    #0x23 expander, pins 113-128, set V = 0
    for j3 in list(range(113,129)):
        pi.pinMode(j3,1)
        pi.digitalWrite(j3,0)
    #0x24 expander, pins 129-144, set V = 0
    for j4 in list(range(129,145)):
        pi.pinMode(j4,1)
        pi.digitalWrite(j4,0)
    #0x25 expander, pins 145-160, set V = 0
    for j5 in list(range(145,161)):
        pi.pinMode(j5,1)
        pi.digitalWrite(j5,0)
    #0x26 expander, pins 161-176, set V = 0
    for j6 in list(range(161,177)):
        pi.pinMode(j6,1)
        pi.digitalWrite(j6,0)
    #0x27 expander, pins 177-192, set V = 0
    for j7 in list(range(177,193)):
        pi.pinMode(j7,1)
        pi.digitalWrite(j7,0)

reset()

print('Pin 1')
#pi pin 8, wiringpi 15 -> out
#0x27 pin 177 -> in
pi.pinMode(15,1)  #output
pi.pinMode(177,0) #input
pi.digitalWrite(15,1) #output to high
#Test RX 1
readoutrx1 = pi.digitalRead(177)
with open(connected_file, 'w+') as f:
    if readoutrx1 == 0:
        f.write("Pair 1 Not Connected \n")
        f.close()
    elif readoutrx1 == 1:
        f.write("Pair 1 Connected \n")
        f.close()
#Test RX*
with open(adjacent_file, 'w+') as f1:
    f1.write('Pin 1 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 177
    for i2 in list(range(178,193)):  #skip 177
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(15,0) #output to low

reset()

print('Pin 2')
#pi pin 16, wiringpi 4 -> out
#0x27 pin 178 -> in
pi.pinMode(4,1)  #output
pi.pinMode(178,0) #input
pi.digitalWrite(4,1) #output to high
#Test RX 2
readoutrx2 = pi.digitalRead(178)
with open(connected_file, 'a') as f:
    if readoutrx2 == 0:
        f.write("Pair 2 Not Connected \n")
        f.close()
    elif readoutrx2 == 1:
        f.write("Pair 2 Connected \n")
        f.close()
#Test RX*
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 2 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 178
    pi.pinMode(177,0)
    readoutrxb = pi.digitalRead(177)
    if readoutrxb == 0:
        f1.write("Wiringpi Pin 177 is Not Connected \n")
    elif readoutrxb == 1:
        f1.write("Wiringpi Pin 177 is Connected \n")
    for i2 in list(range(179,193)): #skip 178
        pi.pinMode(i2,0)
        readoutrxc = pi.digitalRead(i2)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxd = pi.digitalRead(i3)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)
        readoutrxe = pi.digitalRead(i4)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(4,0) #output to low

reset()

print('Pin 3')
#pi pin 18, wiringpi 5 -> out
#0x27 pin 179 -> in
pi.pinMode(5,1)  #output
pi.pinMode(179,0) #input
pi.digitalWrite(5,1) #output to high
#Test RX 3
readoutrx3 = pi.digitalRead(179)
with open(connected_file, 'a') as f:
    if readoutrx3 == 0:
        f.write("Pair 3 Not Connected \n")
        f.close()
    elif readoutrx3 == 1:
        f.write("Pair 3 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 3 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 179
    for i2 in list(range(177,179)): #177-178
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(180,193)): #skip 179
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(5,0) #output to low

reset()

print('Pin 4')
#pi pin 22, wiringpi 6 -> out
#0x27 pin 180 -> in
pi.pinMode(6,1)  #output
pi.pinMode(180,0) #input
pi.digitalWrite(6,1) #output to high
#Test RX 4
readoutrx4 = pi.digitalRead(180)
with open(connected_file, 'a') as f:
    if readoutrx4 == 0:
        f.write("Pair 4 Not Connected \n")
        f.close()
    elif readoutrx4 == 1:
        f.write("Pair 4 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 4 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 180
    for i2 in list(range(177,180)):  #177-179
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(181,193)): #skip 180
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(6,0) #output to low

reset()

print('Pin 5')
#pi pin 36, wiringpi 27 -> out
#0x27 pin 181 -> in
pi.pinMode(27,1)  #output
pi.pinMode(181,0) #input
pi.digitalWrite(27,1) #output to high
#Test RX 5
readoutrx5 = pi.digitalRead(181)
with open(connected_file, 'a') as f:
    if readoutrx5 == 0:
        f.write("Pair 5 Not Connected \n")
        f.close()
    elif readoutrx5 == 1:
        f.write("Pair 5 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 5 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 181
    for i2 in list(range(177,181)):  #177-180
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(182,193)): #skip 181
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(27,0) #output to low

reset()

print('Pin 6')
#pi pin 37, wiringpi 25 -> out
#0x27 pin 182 -> in
pi.pinMode(25,1)  #output
pi.pinMode(182,0) #input
pi.digitalWrite(25,1) #output to high
#Test RX 6
readoutrx6 = pi.digitalRead(182)
with open(connected_file, 'a') as f:
    if readoutrx6 == 0:
        f.write("Pair 6 Not Connected \n")
        f.close()
    elif readoutrx6 == 1:
        f.write("Pair 6 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 6 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 182
    for i2 in list(range(177,182)): #177-181
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(183,193)): #skip 182
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(25,0) #output to low

reset()

print('Pin 7')
#pi pin 35, wiringpi 24 -> out
#0x27 pin 183 -> in
pi.pinMode(24,1)  #output
pi.pinMode(183,0) #input
pi.digitalWrite(24,1) #output to high
#Test RX 7
readoutrx7 = pi.digitalRead(183)
with open(connected_file, 'a') as f:
    if readoutrx7 == 0:
        f.write("Pair 7 Not Connected \n")
        f.close()
    elif readoutrx7 == 1:
        f.write("Pair 7 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 7 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 183
    for i2 in list(range(177,183)): #177-182
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(184,193)): #skip 183
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(24,0) #output to low

reset()

print('Pin 8')
#pi pin 33, wiringpi 23 -> out
#0x27 pin 184 -> in
pi.pinMode(23,1)  #output
pi.pinMode(184,0) #input
pi.digitalWrite(23,1) #output to high
#Test RX 8
readoutrx8 = pi.digitalRead(184)
with open(connected_file, 'a') as f:
    if readoutrx8 == 0:
        f.write("Pair 8 Not Connected \n")
        f.close()
    elif readoutrx8 == 1:
        f.write("Pair 8 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 8 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 184
    for i2 in list(range(177,184)): #177-183
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(185,193)): #skip 184
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(23,0) #output to low

reset()

print('Pin 9')
#pi pin 31, wiringpi 22 -> out
#0x27 pin 185 -> in
pi.pinMode(22,1)  #output
pi.pinMode(185,0) #input
pi.digitalWrite(22,1) #output to high
#Test RX 9
readoutrx9 = pi.digitalRead(185)
with open(connected_file, 'a') as f:
    if readoutrx9 == 0:
        f.write("Pair 9 Not Connected \n")
        f.close()
    elif readoutrx9 == 1:
        f.write("Pair 9 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 9 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 185
    for i2 in list(range(177,185)): #177-184
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(186,193)): #skip 185
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(22,0) #output to low

reset()

print('Pin 10')
#pi pin 23, wiringpi 14 -> out
#0x27 pin 186 -> in
pi.pinMode(14,1)  #output
pi.pinMode(186,0) #input
pi.digitalWrite(14,1) #output to high
#Test RX 10
readoutrx10 = pi.digitalRead(186)
with open(connected_file, 'a') as f:
    if readoutrx10 == 0:
        f.write("Pair 10 Not Connected \n")
        f.close()
    elif readoutrx10 == 1:
        f.write("Pair 10 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 10 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 186
    for i2 in list(range(177,186)): #177-185
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(187,193)): #skip 186
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(14,0) #output to low

reset()

print('Pin 11')
#pi pin 21, wiringpi 13-> out
#0x27 pin 187 -> in
pi.pinMode(13,1)  #output
pi.pinMode(187,0) #input
pi.digitalWrite(13,1) #output to high
#Test RX 11
readoutrx11 = pi.digitalRead(187)
with open(connected_file, 'a') as f:
    if readoutrx11 == 0:
        f.write("Pair 11 Not Connected \n")
        f.close()
    elif readoutrx11 == 1:
        f.write("Pair 11 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 11 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 187
    for i2 in list(range(177,187)): #177-186
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(188,193)): #skip 187
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(13,0) #output to low

reset()

print('Pin 12')
#pi pin 19, wiringpi 12-> out
#0x27 pin 188 -> in
pi.pinMode(12,1)  #output
pi.pinMode(188,0) #input
pi.digitalWrite(12,1) #output to high
#Test RX 12
readoutrx12 = pi.digitalRead(188)
with open(connected_file, 'a') as f:
    if readoutrx12 == 0:
        f.write("Pair 12 Not Connected \n")
        f.close()
    elif readoutrx12 == 1:
        f.write("Pair 12 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 12 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 188
    for i2 in list(range(177,188)): #177-187
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(189,193)): #skip 188
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(12,0) #output to low

reset()

print('Pin 13')
#pi pin 15, wiringpi 3-> out
#0x27 pin 189 -> in
pi.pinMode(3,1)  #output
pi.pinMode(189,0) #input
pi.digitalWrite(3,1) #output to high
#Test RX 13
readoutrx13 = pi.digitalRead(189)
with open(connected_file, 'a') as f:
    if readoutrx13 == 0:
        f.write("Pair 13 Not Connected \n")
        f.close()
    elif readoutrx13 == 1:
        f.write("Pair 13 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 13 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 189
    for i2 in list(range(177,189)): #177-188
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(190,193)): #skip 189
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(3,0) #output to low

reset()

print('Pin 14')
#pi pin 13, wiringpi 2-> out
#0x27 pin 190 -> in
pi.pinMode(2,1)  #output
pi.pinMode(190,0) #input
pi.digitalWrite(2,1) #output to high
#Test RX 14
readoutrx14 = pi.digitalRead(190)
with open(connected_file, 'a') as f:
    if readoutrx14 == 0:
        f.write("Pair 14 Not Connected \n")
        f.close()
    elif readoutrx14 == 1:
        f.write("Pair 14 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 14 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 190
    for i2 in list(range(177,190)): #177-189
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    for i3 in list(range(191,193)): #skip 190
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(2,0) #output to low

reset()

print('Pin 15')
#pi pin 11, wiringpi 0-> out
#0x27 pin 191 -> in
pi.pinMode(0,1)  #output
pi.pinMode(191,0) #input
pi.digitalWrite(0,1) #output to high
#Test RX 15
readoutrx15 = pi.digitalRead(191)
with open(connected_file, 'a') as f:
    if readoutrx15 == 0:
        f.write("Pair 15 Not Connected \n")
        f.close()
    elif readoutrx15 == 1:
        f.write("Pair 15 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 15 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 191
    for i2 in list(range(177,191)): #177-190
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    pi.pinMode(192,0) #192
    readoutrxc = pi.digitalRead(192)
    if readoutrxc == 0:
        f1.write("Wiringpi Pin 192 is Not Connected \n")
    elif readoutrxc == 1:
        f1.write("Wiringpi Pin 192 is Connected \n")
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxd = pi.digitalRead(i3)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)
        readoutrxe = pi.digitalRead(i4)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(0,0) #output to low

reset()

print('Pin 16')
#pi pin 7, wiringpi 7-> out
#0x27 pin 192 -> in
pi.pinMode(7,1)  #output
pi.pinMode(192,0) #input
pi.digitalWrite(7,1) #output to high
#Test RX 16
readoutrx16 = pi.digitalRead(192)
with open(connected_file, 'a') as f:
    if readoutrx16 == 0:
        f.write("Pair 16 Not Connected \n")
        f.close()
    elif readoutrx16 == 1:
        f.write("Pair 16 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 16 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192, skipping 192
    for i2 in list(range(177,192)): #177-191
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(7,0) #output to low

reset()

print('Pin 17')
#0x20 pin 80 -> out
#0x21 pin 81 -> in
pi.pinMode(80,1)  #output
pi.pinMode(81,0) #input
pi.digitalWrite(80,1) #output to high
#Test RX 17
readoutrx17 = pi.digitalRead(81)
with open(connected_file, 'a') as f:
    if readoutrx17 == 0:
        f.write("Pair 17 Not Connected \n")
        f.close()
    elif readoutrx17 == 1:
        f.write("Pair 17 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 17 RX* Test \n')
    #test 0x21 expander, 81-96, skip 81
    for i1 in list(range(82,97)): #82-96
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(80,0) #output to low

reset()

print('Pin 18')
#0x20 pin 79 -> out
#0x21 pin 82 -> in
pi.pinMode(79,1)  #output
pi.pinMode(82,0) #input
pi.digitalWrite(79,1) #output to high
#Test RX 18
readoutrx18 = pi.digitalRead(82)
with open(connected_file, 'a') as f:
    if readoutrx18 == 0:
        f.write("Pair 18 Not Connected \n")
        f.close()
    elif readoutrx18 == 1:
        f.write("Pair 18 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 18 RX* Test \n')
    #test 0x21 expander, 81-96, skip 82
    pi.pinMode(81,0)
    readoutrxa = pi.digitalRead(81)
    if readoutrxa == 0:
        f1.write("Wiringpi Pin 81 is Not Connected \n")
    elif readoutrxa == 1:
        f1.write("Wiringpi Pin 81 is Connected \n")
    for i2 in list(range(83,97)): #83-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(79,0) #output to low

reset()

print('Pin 19')
#0x20 pin 78 -> out
#0x21 pin 83 -> in
pi.pinMode(78,1)  #output
pi.pinMode(83,0) #input
pi.digitalWrite(78,1) #output to high
#Test RX 19
readoutrx19 = pi.digitalRead(83)
with open(connected_file, 'a') as f:
    if readoutrx19 == 0:
        f.write("Pair 19 Not Connected \n")
        f.close()
    elif readoutrx19 == 1:
        f.write("Pair 19 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 19 RX* Test \n')
    #test 0x21 expander, 81-96, skip 83
    for i1 in list(range(81,83)): #81-82
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(84,97)): #84-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(78,0) #output to low

reset()

print('Pin 20')
#0x20 pin 77 -> out
#0x21 pin 84 -> in
pi.pinMode(77,1)  #output
pi.pinMode(84,0) #input
pi.digitalWrite(77,1) #output to high
#Test RX 20
readoutrx20 = pi.digitalRead(84)
with open(connected_file, 'a') as f:
    if readoutrx20 == 0:
        f.write("Pair 20 Not Connected \n")
        f.close()
    elif readoutrx20 == 1:
        f.write("Pair 20 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 20 RX* Test \n')
    #test 0x21 expander, 81-96, skip 84
    for i1 in list(range(81,84)): #81-83
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(85,97)): #85-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(77,0) #output to low

reset()

print('Pin 21')
#0x20 pin 76 -> out
#0x21 pin 85 -> in
pi.pinMode(76,1)  #output
pi.pinMode(85,0) #input
pi.digitalWrite(76,1) #output to high
#Test RX 21
readoutrx21 = pi.digitalRead(85)
with open(connected_file, 'a') as f:
    if readoutrx21 == 0:
        f.write("Pair 21 Not Connected \n")
        f.close()
    elif readoutrx21 == 1:
        f.write("Pair 21 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 21 RX* Test \n')
    #test 0x21 expander, 81-96, skip 85
    for i1 in list(range(81,85)): #81-84
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(86,97)): #86-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(76,0) #output to low

reset()

print('Pin 22')
#0x20 pin 75 -> out
#0x21 pin 86 -> in
pi.pinMode(75,1)  #output
pi.pinMode(86,0) #input
pi.digitalWrite(75,1) #output to high
#Test RX 22
readoutrx22 = pi.digitalRead(86)
with open(connected_file, 'a') as f:
    if readoutrx22 == 0:
        f.write("Pair 22 Not Connected \n")
        f.close()
    elif readoutrx22 == 1:
        f.write("Pair 22 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 22 RX* Test \n')
    #test 0x21 expander, 81-96, skip 86
    for i1 in list(range(81,86)): #81-85
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(87,97)): #87-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(75,0) #output to low

reset()

print('Pin 23')
#0x20 pin 74 -> out
#0x21 pin 87 -> in
pi.pinMode(74,1)  #output
pi.pinMode(87,0) #input
pi.digitalWrite(74,1) #output to high
#Test RX 23
readoutrx23 = pi.digitalRead(87)
with open(connected_file, 'a') as f:
    if readoutrx23 == 0:
        f.write("Pair 23 Not Connected \n")
        f.close()
    elif readoutrx23 == 1:
        f.write("Pair 23 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 23 RX* Test \n')
    #test 0x21 expander, 81-96, skip 87
    for i1 in list(range(81,87)): #81-86
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(88,97)): #88-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(74,0) #output to low

reset()

print('Pin 24')
#0x20 pin 73 -> out
#0x21 pin 88 -> in
pi.pinMode(73,1)  #output
pi.pinMode(88,0) #input
pi.digitalWrite(73,1) #output to high
#Test RX 24
readoutrx24 = pi.digitalRead(88)
with open(connected_file, 'a') as f:
    if readoutrx24 == 0:
        f.write("Pair 24 Not Connected \n")
        f.close()
    elif readoutrx24 == 1:
        f.write("Pair 24 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 24 RX* Test \n')
    #test 0x21 expander, 81-96, skip 88
    for i1 in list(range(81,88)): #81-87
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(89,97)): #89-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(73,0) #output to low

reset()

print('Pin 25')
#0x20 pin 72 -> out
#0x21 pin 89 -> in
pi.pinMode(72,1)  #output
pi.pinMode(89,0) #input
pi.digitalWrite(72,1) #output to high
#Test RX 25
readoutrx25 = pi.digitalRead(89)
with open(connected_file, 'a') as f:
    if readoutrx25 == 0:
        f.write("Pair 25 Not Connected \n")
        f.close()
    elif readoutrx25 == 1:
        f.write("Pair 25 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 25 RX* Test \n')
    #test 0x21 expander, 81-96, skip 89
    for i1 in list(range(81,89)): #81-88
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(90,97)): #90-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(72,0) #output to low

reset()

print('Pin 26')
#0x20 pin 71 -> out
#0x21 pin 90 -> in
pi.pinMode(71,1)  #output
pi.pinMode(90,0) #input
pi.digitalWrite(71,1) #output to high
#Test RX 26
readoutrx26 = pi.digitalRead(90)
with open(connected_file, 'a') as f:
    if readoutrx26 == 0:
        f.write("Pair 26 Not Connected \n")
        f.close()
    elif readoutrx26 == 1:
        f.write("Pair 26 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 26 RX* Test \n')
    #test 0x21 expander, 81-96, skip 90
    for i1 in list(range(81,90)): #81-89
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(91,97)): #91-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(71,0) #output to low

reset()

print('Pin 27')
#0x20 pin 70 -> out
#0x21 pin 91 -> in
pi.pinMode(70,1)  #output
pi.pinMode(91,0) #input
pi.digitalWrite(70,1) #output to high
#Test RX 27
readoutrx27 = pi.digitalRead(91)
with open(connected_file, 'a') as f:
    if readoutrx27 == 0:
        f.write("Pair 27 Not Connected \n")
        f.close()
    elif readoutrx27 == 1:
        f.write("Pair 27 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 27 RX* Test \n')
    #test 0x21 expander, 81-96, skip 91
    for i1 in list(range(81,91)): #81-90
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(92,97)): #92-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(70,0) #output to low

reset()

print('Pin 28')
#0x20 pin 69 -> out
#0x21 pin 92 -> in
pi.pinMode(69,1)  #output
pi.pinMode(92,0) #input
pi.digitalWrite(69,1) #output to high
#Test RX 28
readoutrx28 = pi.digitalRead(92)
with open(connected_file, 'a') as f:
    if readoutrx28 == 0:
        f.write("Pair 28 Not Connected \n")
        f.close()
    elif readoutrx28 == 1:
        f.write("Pair 28 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 28 RX* Test \n')
    #test 0x21 expander, 81-96, skip 92
    for i1 in list(range(81,92)): #81-91
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(93,97)): #93-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(69,0) #output to low

reset()

print('Pin 29')
#0x20 pin 68 -> out
#0x21 pin 93 -> in
pi.pinMode(68,1)  #output
pi.pinMode(93,0) #input
pi.digitalWrite(68,1) #output to high
#Test RX 29
readoutrx29 = pi.digitalRead(93)
with open(connected_file, 'a') as f:
    if readoutrx29 == 0:
        f.write("Pair 29 Not Connected \n")
        f.close()
    elif readoutrx29 == 1:
        f.write("Pair 29 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 29 RX* Test \n')
    #test 0x21 expander, 81-96, skip 93
    for i1 in list(range(81,93)): #81-92
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(94,97)): #94-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(68,0) #output to low

reset()

print('Pin 30')
#0x20 pin 67 -> out
#0x21 pin 94 -> in
pi.pinMode(67,1)  #output
pi.pinMode(94,0) #input
pi.digitalWrite(67,1) #output to high
#Test RX 30
readoutrx30 = pi.digitalRead(94)
with open(connected_file, 'a') as f:
    if readoutrx30 == 0:
        f.write("Pair 30 Not Connected \n")
        f.close()
    elif readoutrx30 == 1:
        f.write("Pair 30 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 30 RX* Test \n')
    #test 0x21 expander, 81-96, skip 94
    for i1 in list(range(81,94)): #81-93
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(95,97)): #95-96
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x27 expander, 177-192
    for i3 in list(range(177,193)): #177-192
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x26 expander, 161-176
    for i4 in list(range(161,177)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(67,0) #output to low

reset()

print('Pin 31')
#0x20 pin 66 -> out
#0x21 pin 95 -> in
pi.pinMode(66,1)  #output
pi.pinMode(95,0) #input
pi.digitalWrite(66,1) #output to high
#Test RX 31
readoutrx31 = pi.digitalRead(95)
with open(connected_file, 'a') as f:
    if readoutrx31 == 0:
        f.write("Pair 31 Not Connected \n")
        f.close()
    elif readoutrx31 == 1:
        f.write("Pair 31 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 31 RX* Test \n')
    #test 0x21 expander, 81-96, skip 95
    for i1 in list(range(81,95)): #81-94
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    pi.pinMode(96,0)
    readoutrxb = pi.digitalRead(96)
    if readoutrxb == 0:
        f1.write("Wiringpi Pin 96 is Not Connected \n")
    elif readoutrxb == 1:
        f1.write("Wiringpi Pin 96 is Connected \n")
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxc = pi.digitalRead(i2)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxd = pi.digitalRead(i3)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)
        readoutrxe = pi.digitalRead(i4)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(66,0) #output to low

reset()

print('Pin 32')
#0x20 pin 65 -> out
#0x21 pin 96 -> in
pi.pinMode(65,1)  #output
pi.pinMode(96,0) #input
pi.digitalWrite(65,1) #output to high
#Test RX 32
readoutrx32 = pi.digitalRead(96)
with open(connected_file, 'a') as f:
    if readoutrx32 == 0:
        f.write("Pair 32 Not Connected \n")
        f.close()
    elif readoutrx32 == 1:
        f.write("Pair 32 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 32 RX* Test \n')
    #test 0x21 expander, 81-96, skip 96
    for i1 in list(range(81,96)): #81-96
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(65,0) #output to low

reset()

print('Pin 33')
#0x24 pin 137 -> out
#0x25 pin 152 -> in
pi.pinMode(137,1)  #output
pi.pinMode(152,0) #input
pi.digitalWrite(137,1) #output to high
#Test RX 33
readoutrx33 = pi.digitalRead(152)
with open(connected_file, 'a') as f:
    if readoutrx33 == 0:
        f.write("Pair 33 Not Connected \n")
        f.close()
    elif readoutrx33 == 1:
        f.write("Pair 33 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 33 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 152
    for i4 in list(range(145,152)): #145-151
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(153,161)): #153-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(137,0) #output to low

reset()

print('Pin 34')
#0x24 pin 138 -> out
#0x25 pin 151 -> in
pi.pinMode(138,1)  #output
pi.pinMode(151,0) #input
pi.digitalWrite(138,1) #output to high
#Test RX 34
readoutrx34 = pi.digitalRead(151)
with open(connected_file, 'a') as f:
    if readoutrx34 == 0:
        f.write("Pair 34 Not Connected \n")
        f.close()
    elif readoutrx34 == 1:
        f.write("Pair 34 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 34 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 151
    for i4 in list(range(145,151)): #145-150
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(152,161)): #152-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(138,0) #output to low

reset()

print('Pin 35')
#0x24 pin 139 -> out
#0x25 pin 150 -> in
pi.pinMode(139,1)  #output
pi.pinMode(150,0) #input
pi.digitalWrite(139,1) #output to high
#Test RX 35
readoutrx35 = pi.digitalRead(150)
with open(connected_file, 'a') as f:
    if readoutrx35 == 0:
        f.write("Pair 35 Not Connected \n")
        f.close()
    elif readoutrx35 == 1:
        f.write("Pair 35 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 35 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 150
    for i4 in list(range(145,150)): #145-149
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(151,161)): #151-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(139,0) #output to low

reset()

print('Pin 36')
#0x24 pin 140 -> out
#0x25 pin 149 -> in
pi.pinMode(140,1)  #output
pi.pinMode(149,0) #input
pi.digitalWrite(140,1) #output to high
#Test RX 36
readoutrx36 = pi.digitalRead(149)
with open(connected_file, 'a') as f:
    if readoutrx36 == 0:
        f.write("Pair 36 Not Connected \n")
        f.close()
    elif readoutrx36 == 1:
        f.write("Pair 36 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 36 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 149
    for i4 in list(range(145,149)): #145-148
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(150,161)): #150-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(140,0) #output to low

reset()

print('Pin 37')
#0x24 pin 141 -> out
#0x25 pin 148 -> in
pi.pinMode(141,1)  #output
pi.pinMode(148,0) #input
pi.digitalWrite(141,1) #output to high
#Test RX 37
readoutrx37 = pi.digitalRead(148)
with open(connected_file, 'a') as f:
    if readoutrx37 == 0:
        f.write("Pair 37 Not Connected \n")
        f.close()
    elif readoutrx37 == 1:
        f.write("Pair 37 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 37 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 148
    for i4 in list(range(145,148)): #145-147
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(149,161)): #149-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(141,0) #output to low

reset()

print('Pin 38')
#0x24 pin 142 -> out
#0x25 pin 147 -> in
pi.pinMode(142,1)  #output
pi.pinMode(147,0) #input
pi.digitalWrite(142,1) #output to high
#Test RX 38
readoutrx38 = pi.digitalRead(147)
with open(connected_file, 'a') as f:
    if readoutrx38 == 0:
        f.write("Pair 38 Not Connected \n")
        f.close()
    elif readoutrx38 == 1:
        f.write("Pair 38 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 38 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 147
    for i4 in list(range(145,147)): #145-146
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(148,161)): #148-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(142,0) #output to low

reset()

print('Pin 39')
#0x24 pin 143 -> out
#0x25 pin 146 -> in
pi.pinMode(143,1)  #output
pi.pinMode(146,0) #input
pi.digitalWrite(143,1) #output to high
#Test RX 39
readoutrx39 = pi.digitalRead(146)
with open(connected_file, 'a') as f:
    if readoutrx39 == 0:
        f.write("Pair 39 Not Connected \n")
        f.close()
    elif readoutrx39 == 1:
        f.write("Pair 39 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 39 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 146
    pi.pinMode(145,0)
    readoutrxd = pi.digitalRead(145)
    if readoutrxd == 0:
        f1.write("Wiringpi Pin 145 is Not Connected \n")
    elif readoutrxd == 1:
        f1.write("Wiringpi Pin 145 is Connected \n")
    for i4 in list(range(147,161)): #147-160
        pi.pinMode(i4,0)
        readoutrxe = pi.digitalRead(i4)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(143,0) #output to low

reset()

print('Pin 40')
#0x24 pin 144 -> out
#0x25 pin 145 -> in
pi.pinMode(144,1)  #output
pi.pinMode(145,0) #input
pi.digitalWrite(144,1) #output to high
#Test RX 40
readoutrx40 = pi.digitalRead(145)
with open(connected_file, 'a') as f:
    if readoutrx40 == 0:
        f.write("Pair 40 Not Connected \n")
        f.close()
    elif readoutrx40 == 1:
        f.write("Pair 40 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 40 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 145
    for i4 in list(range(146,161)): #146-160
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(144,0) #output to low

reset()

print('Pin 41')
#0x23 pin 121 -> out
#0x25 pin 160 -> in
pi.pinMode(121,1)  #output
pi.pinMode(160,0) #input
pi.digitalWrite(121,1) #output to high
#Test RX 41
readoutrx41 = pi.digitalRead(160)
with open(connected_file, 'a') as f:
    if readoutrx41 == 0:
        f.write("Pair 41 Not Connected \n")
        f.close()
    elif readoutrx41 == 1:
        f.write("Pair 41 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 41 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 160
    for i4 in list(range(145,160)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(121,0) #output to low

reset()

print('Pin 42')
#0x23 pin 122 -> out
#0x25 pin 159 -> in
pi.pinMode(122,1)  #output
pi.pinMode(159,0) #input
pi.digitalWrite(122,1) #output to high
#Test RX 42
readoutrx42 = pi.digitalRead(159)
with open(connected_file, 'a') as f:
    if readoutrx42 == 0:
        f.write("Pair 42 Not Connected \n")
        f.close()
    elif readoutrx42 == 1:
        f.write("Pair 42 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 42 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 159
    for i4 in list(range(145,159)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    pi.pinMode(160,0)
    readoutrxe = pi.digitalRead(160)
    if readoutrxe == 0:
        f1.write("Wiringpi Pin 160 is Not Connected \n")
    elif readoutrxe == 1:
        f1.write("Wiringpi Pin 160 is Connected \n")
    f1.close()
pi.digitalWrite(122,0) #output to low

reset()

print('Pin 43')
#0x23 pin 123 -> out
#0x25 pin 158 -> in
pi.pinMode(123,1)  #output
pi.pinMode(158,0) #input
pi.digitalWrite(123,1) #output to high
#Test RX 43
readoutrx43 = pi.digitalRead(158)
with open(connected_file, 'a') as f:
    if readoutrx43 == 0:
        f.write("Pair 43 Not Connected \n")
        f.close()
    elif readoutrx43 == 1:
        f.write("Pair 43 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 43 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 158
    for i4 in list(range(145,158)): #145-157
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(159,161)): #159-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(123,0) #output to low

reset()

print('Pin 44')
#0x23 pin 124 -> out
#0x25 pin 157 -> in
pi.pinMode(124,1)  #output
pi.pinMode(157,0) #input
pi.digitalWrite(124,1) #output to high
#Test RX 44
readoutrx44 = pi.digitalRead(157)
with open(connected_file, 'a') as f:
    if readoutrx44 == 0:
        f.write("Pair 44 Not Connected \n")
        f.close()
    elif readoutrx44 == 1:
        f.write("Pair 44 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 44 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 157
    for i4 in list(range(145,157)): #145-156
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(158,161)): #158-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(124,0) #output to low

reset()

print('Pin 45')
#0x23 pin 125 -> out
#0x25 pin 156 -> in
pi.pinMode(125,1)  #output
pi.pinMode(156,0) #input
pi.digitalWrite(125,1) #output to high
#Test RX 45
readoutrx45 = pi.digitalRead(156)
with open(connected_file, 'a') as f:
    if readoutrx45 == 0:
        f.write("Pair 45 Not Connected \n")
        f.close()
    elif readoutrx45 == 1:
        f.write("Pair 45 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 44 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 156
    for i4 in list(range(145,156)): #145-155
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(157,161)): #157-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(125,0) #output to low

reset()

print('Pin 46')
#0x23 pin 126 -> out
#0x25 pin 155 -> in
pi.pinMode(126,1)  #output
pi.pinMode(155,0) #input
pi.digitalWrite(126,1) #output to high
#Test RX 46
readoutrx46 = pi.digitalRead(155)
with open(connected_file, 'a') as f:
    if readoutrx46 == 0:
        f.write("Pair 46 Not Connected \n")
        f.close()
    elif readoutrx46 == 1:
        f.write("Pair 46 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 46 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 155
    for i4 in list(range(145,155)): #145-154
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(156,161)): #156-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(126,0) #output to low

reset()

print('Pin 47')
#0x23 pin 127 -> out
#0x25 pin 154 -> in
pi.pinMode(127,1)  #output
pi.pinMode(154,0) #input
pi.digitalWrite(127,1) #output to high
#Test RX 47
readoutrx47 = pi.digitalRead(154)
with open(connected_file, 'a') as f:
    if readoutrx47 == 0:
        f.write("Pair 47 Not Connected \n")
        f.close()
    elif readoutrx47 == 1:
        f.write("Pair 47 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 47 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 154
    for i4 in list(range(145,154)): #145-153
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(155,161)): #155-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(127,0) #output to low

reset()

print('Pin 48')
#0x23 pin 128 -> out
#0x25 pin 153 -> in
pi.pinMode(128,1)  #output
pi.pinMode(153,0) #input
pi.digitalWrite(128,1) #output to high
#Test RX 48
readoutrx48 = pi.digitalRead(153)
with open(connected_file, 'a') as f:
    if readoutrx48 == 0:
        f.write("Pair 48 Not Connected \n")
        f.close()
    elif readoutrx48 == 1:
        f.write("Pair 48 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 48 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)): #177-192
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160, skip 153
    for i4 in list(range(145,153)): #145-152
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    for i5 in list(range(154,161)): #154-160
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(128,0) #output to low

reset()

print('Pin 49')
#0x23 pin 113 -> out
#0x26 pin 168 -> in
pi.pinMode(113,1)  #output
pi.pinMode(168,0) #input
pi.digitalWrite(113,1) #output to high
#Test RX 49
readoutrx49 = pi.digitalRead(168)
with open(connected_file, 'a') as f:
    if readoutrx49 == 0:
        f.write("Pair 49 Not Connected \n")
        f.close()
    elif readoutrx49 == 1:
        f.write("Pair 49 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 49 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 168
    for i3 in list(range(161,168)): #161-167
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(169,177)): #169-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(113,0) #output to low

reset()

print('Pin 50')
#0x23 pin 114 -> out
#0x26 pin 167 -> in
pi.pinMode(114,1)  #output
pi.pinMode(167,0) #input
pi.digitalWrite(114,1) #output to high
#Test RX 50
readoutrx50 = pi.digitalRead(167)
with open(connected_file, 'a') as f:
    if readoutrx50 == 0:
        f.write("Pair 50 Not Connected \n")
        f.close()
    elif readoutrx50 == 1:
        f.write("Pair 50 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 50 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 167
    for i3 in list(range(161,167)): #161-166
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(168,177)): #168-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(114,0) #output to low

reset()

print('Pin 51')
#0x23 pin 115 -> out
#0x26 pin 166 -> in
pi.pinMode(115,1)  #output
pi.pinMode(166,0) #input
pi.digitalWrite(115,1) #output to high
#Test RX 51
readoutrx51 = pi.digitalRead(166)
with open(connected_file, 'a') as f:
    if readoutrx51 == 0:
        f.write("Pair 51 Not Connected \n")
        f.close()
    elif readoutrx51 == 1:
        f.write("Pair 51 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 51 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 166
    for i3 in list(range(161,166)): #161-165
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(167,177)): #167-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(115,0) #output to low

reset()

print('Pin 52')
#0x23 pin 116 -> out
#0x26 pin 165 -> in
pi.pinMode(116,1)  #output
pi.pinMode(165,0) #input
pi.digitalWrite(116,1) #output to high
#Test RX 52
readoutrx52 = pi.digitalRead(165)
with open(connected_file, 'a') as f:
    if readoutrx52 == 0:
        f.write("Pair 52 Not Connected \n")
        f.close()
    elif readoutrx52 == 1:
        f.write("Pair 52 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 52 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 165
    for i3 in list(range(161,165)): #161-164
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(166,177)): #166-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(116,0) #output to low

reset()

print('Pin 53')
#0x23 pin 117 -> out
#0x26 pin 164 -> in
pi.pinMode(117,1)  #output
pi.pinMode(164,0) #input
pi.digitalWrite(117,1) #output to high
#Test RX 53
readoutrx53 = pi.digitalRead(164)
with open(connected_file, 'a') as f:
    if readoutrx53 == 0:
        f.write("Pair 53 Not Connected \n")
        f.close()
    elif readoutrx53 == 1:
        f.write("Pair 53 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 53 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 164
    for i3 in list(range(161,164)): #161-163
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(165,177)): #165-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(117,0) #output to low

reset()

print('Pin 54')
#0x23 pin 118 -> out
#0x26 pin 163 -> in
pi.pinMode(118,1)  #output
pi.pinMode(163,0) #input
pi.digitalWrite(118,1) #output to high
#Test RX 54
readoutrx54 = pi.digitalRead(163)
with open(connected_file, 'a') as f:
    if readoutrx54 == 0:
        f.write("Pair 54 Not Connected \n")
        f.close()
    elif readoutrx54 == 1:
        f.write("Pair 54 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 54 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 163
    for i3 in list(range(161,163)): #161-162
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(164,177)): #164-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(118,0) #output to low

reset()

print('Pin 55')
#0x23 pin 119 -> out
#0x26 pin 162 -> in
pi.pinMode(119,1)  #output
pi.pinMode(162,0) #input
pi.digitalWrite(119,1) #output to high
#Test RX 55
readoutrx55 = pi.digitalRead(162)
with open(connected_file, 'a') as f:
    if readoutrx55 == 0:
        f.write("Pair 55 Not Connected \n")
        f.close()
    elif readoutrx55 == 1:
        f.write("Pair 55 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 55 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 162
    pi.pinMode(161,0)
    readoutrxc = pi.digitalRead(161)
    if readoutrxc == 0:
        f1.write("Wiringpi Pin 161 is Not Connected \n")
    elif readoutrxc == 1:
        f1.write("Wiringpi Pin 161 is Connected \n")
    for i3 in list(range(163,177)): #163-176
        pi.pinMode(i3,0)
        readoutrxd = pi.digitalRead(i3)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)
        readoutrxe = pi.digitalRead(i4)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(119,0) #output to low

reset()

print('Pin 56')
#0x23 pin 120 -> out
#0x26 pin 161 -> in
pi.pinMode(120,1)  #output
pi.pinMode(161,0) #input
pi.digitalWrite(120,1) #output to high
#Test RX 56
readoutrx56 = pi.digitalRead(161)
with open(connected_file, 'a') as f:
    if readoutrx56 == 0:
        f.write("Pair 56 Not Connected \n")
        f.close()
    elif readoutrx56 == 1:
        f.write("Pair 56 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 56 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 161
    for i3 in list(range(162,177)): #162-176
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(120,0) #output to low

reset()

print('Pin 57')
#0x22 pin 105 -> out
#0x26 pin 176 -> in
pi.pinMode(105,1)  #output
pi.pinMode(176,0) #input
pi.digitalWrite(105,1) #output to high
#Test RX 57
readoutrx57 = pi.digitalRead(176)
with open(connected_file, 'a') as f:
    if readoutrx57 == 0:
        f.write("Pair 57 Not Connected \n")
        f.close()
    elif readoutrx57 == 1:
        f.write("Pair 57 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 57 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 176
    for i3 in list(range(161,176)): #161-175
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    #test 0x25 expander, 145-160
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(105,0) #output to low

reset()

print('Pin 58')
#0x22 pin 106 -> out
#0x26 pin 175 -> in
pi.pinMode(106,1)  #output
pi.pinMode(175,0) #input
pi.digitalWrite(106,1) #output to high
#Test RX 58
readoutrx58 = pi.digitalRead(175)
with open(connected_file, 'a') as f:
    if readoutrx58 == 0:
        f.write("Pair 58 Not Connected \n")
        f.close()
    elif readoutrx58 == 1:
        f.write("Pair 58 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 58 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 175
    for i3 in list(range(161,175)): #161-174
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    pi.pinMode(176,0)
    readoutrxd = pi.digitalRead(176)
    if readoutrxd == 0:
        f1.write("Wiringpi Pin 176 is Not Connected \n")
    elif readoutrxd == 1:
        f1.write("Wiringpi Pin 176 is Connected \n")
    #test 0x25 expander, 145-160
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)
        readoutrxe = pi.digitalRead(i4)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    f1.close()
pi.digitalWrite(106,0) #output to low

reset()

print('Pin 59')
#0x22 pin 107 -> out
#0x26 pin 174 -> in
pi.pinMode(107,1)  #output
pi.pinMode(174,0) #input
pi.digitalWrite(107,1) #output to high
#Test RX 59
readoutrx59 = pi.digitalRead(174)
with open(connected_file, 'a') as f:
    if readoutrx59 == 0:
        f.write("Pair 59 Not Connected \n")
        f.close()
    elif readoutrx59 == 1:
        f.write("Pair 59 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 59 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 174
    for i3 in list(range(161,174)): #161-173
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(175,177)): #175-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(107,0) #output to low

reset()

print('Pin 60')
#0x22 pin 108 -> out
#0x26 pin 173 -> in
pi.pinMode(108,1)  #output
pi.pinMode(173,0) #input
pi.digitalWrite(108,1) #output to high
#Test RX 60
readoutrx60 = pi.digitalRead(173)
with open(connected_file, 'a') as f:
    if readoutrx60 == 0:
        f.write("Pair 60 Not Connected \n")
        f.close()
    elif readoutrx60 == 1:
        f.write("Pair 60 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 60 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 173
    for i3 in list(range(161,173)): #161-172
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(174,177)): #174-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(108,0) #output to low

reset()

print('Pin 61')
#0x22 pin 109 -> out
#0x26 pin 172 -> in
pi.pinMode(109,1)  #output
pi.pinMode(172,0) #input
pi.digitalWrite(109,1) #output to high
#Test RX 61
readoutrx61 = pi.digitalRead(172)
with open(connected_file, 'a') as f:
    if readoutrx61 == 0:
        f.write("Pair 61 Not Connected \n")
        f.close()
    elif readoutrx61 == 1:
        f.write("Pair 61 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 61 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 172
    for i3 in list(range(161,172)): #161-171
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(173,177)): #173-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(109,0) #output to low

reset()

print('Pin 62')
#0x22 pin 110 -> out
#0x26 pin 171 -> in
pi.pinMode(110,1)  #output
pi.pinMode(171,0) #input
pi.digitalWrite(110,1) #output to high
#Test RX 62
readoutrx62 = pi.digitalRead(171)
with open(connected_file, 'a') as f:
    if readoutrx62 == 0:
        f.write("Pair 62 Not Connected \n")
        f.close()
    elif readoutrx62 == 1:
        f.write("Pair 62 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 62 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 171
    for i3 in list(range(161,171)): #161-170
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(172,177)): #172-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(110,0) #output to low

reset()

print('Pin 63')
#0x22 pin 111 -> out
#0x26 pin 170 -> in
pi.pinMode(111,1)  #output
pi.pinMode(170,0) #input
pi.digitalWrite(111,1) #output to high
#Test RX 63
readoutrx63 = pi.digitalRead(170)
with open(connected_file, 'a') as f:
    if readoutrx63 == 0:
        f.write("Pair 63 Not Connected \n")
        f.close()
    elif readoutrx63 == 1:
        f.write("Pair 63 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 63 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 170
    for i3 in list(range(161,170)): #161-169
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(171,177)): #171-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(111,0) #output to low

reset()

print('Pin 64')
#0x22 pin 112 -> out
#0x26 pin 169 -> in
pi.pinMode(112,1)  #output
pi.pinMode(169,0) #input
pi.digitalWrite(112,1) #output to high
#Test RX 64
readoutrx64 = pi.digitalRead(169)
with open(connected_file, 'a') as f:
    if readoutrx64 == 0:
        f.write("Pair 64 Not Connected \n")
        f.close()
    elif readoutrx64 == 1:
        f.write("Pair 64 Connected \n")
        f.close()
#Test RX *
with open(adjacent_file, 'a') as f1:
    f1.write('Pin 64 RX* Test \n')
    #test 0x21 expander, 81-96
    for i1 in list(range(81,97)):
        pi.pinMode(i1,0)
        readoutrxa = pi.digitalRead(i1)
        if readoutrxa == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i1))
        elif readoutrxa == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i1))
    #test 0x27 expander, 177-192
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)
        readoutrxb = pi.digitalRead(i2)
        if readoutrxb == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i2))
        elif readoutrxb == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i2))
    #test 0x26 expander, 161-176, skip 169
    for i3 in list(range(161,169)): #161-168
        pi.pinMode(i3,0)
        readoutrxc = pi.digitalRead(i3)
        if readoutrxc == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i3))
        elif readoutrxc == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i3))
    for i4 in list(range(170,177)): #170-176
        pi.pinMode(i4,0)
        readoutrxd = pi.digitalRead(i4)
        if readoutrxd == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i4))
        elif readoutrxd == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i4))
    #test 0x25 expander, 145-160
    for i5 in list(range(145,161)):
        pi.pinMode(i5,0)
        readoutrxe = pi.digitalRead(i5)
        if readoutrxe == 0:
            f1.write("Wiringpi Pin {} is Not Connected \n".format(i5))
        elif readoutrxe == 1:
            f1.write("Wiringpi Pin {} is Connected \n".format(i5))
    f1.close()
pi.digitalWrite(112,0) #output to low

reset()

print('Ground')
#main ground line
#pi pin 8, wiringpi 15 -> out
#pi pin 26, wiringpi 11 -> in
pi.pinMode(11,1)  #output
pi.digitalWrite(11,1) #output to high
with open(ground_file, 'w+') as f1:
    f1.write('Main Ground Line Test \n')
    #0x21
    for i1 in list(range(81-97)):
        pi.pinMode(i1,0)  #input
        readouta = pi.digitalRead(i1)
        #print('pin {} is {}'.format(i1,pi.digitalRead(i1)))
        if readouta == 0:
            f1.write('Ground Line is Not Connected to {} \n'.format(i1))
        elif readouta == 1:
            f1.write('Ground Line is Connected to {} \n'.format(i1))
    reset()
    #0x27
    for i2 in list(range(177,193)):
        pi.pinMode(i2,0)  #input
        readoutb = pi.digitalRead(i2)
        #print('pin {} is {}'.format(i2,pi.digitalRead(i2)))
        if readoutb == 0:
            f1.write('Ground Line is Not Connected to {} \n'.format(i2))
        elif readoutb == 1:
            f1.write('Ground Line is Connected to {} \n'.format(i2))
    reset()
    #0x26
    for i3 in list(range(161,177)):
        pi.pinMode(i3,0)  #input
        readoutc = pi.digitalRead(i3)
        #print('pin {} is {}'.format(i3,pi.digitalRead(i3)))
        if readoutc == 0:
            f1.write('Ground Line is Not Connected to {} \n'.format(i3))
        elif readoutc == 1:
            f1.write('Ground Line is Connected to {} \n'.format(i3))
    reset()
    #0x25
    for i4 in list(range(145,161)):
        pi.pinMode(i4,0)  #input
        readoutd = pi.digitalRead(i4)
        #print('pin {} is {}'.format(i4,pi.digitalRead(i4)))
        if readoutd == 0:
            f1.write('Ground Line is Not Connected to {} \n'.format(i4))
        elif readoutd == 1:
            f1.write('Ground Line is Connected to {} \n'.format(i4))
pi.digitalWrite(11,0)

reset()

#back ground outer pins
#0x22 pin 97 -> in -> ground pin 1
#0x21 pin 96 -> out
#adjacent 0x22 pin 98 -> out -> ground pin 5
with open(ground_file, 'a') as f1:
    f1.write('Back Ground Pins Test \n')
    pi.pinMode(96,1)  #output
    pi.pinMode(97,0)  #input
    pi.digitalWrite(96,1)  #output to high
    readouta = pi.digitalRead(97)
    if readouta == 0:
        f1.write('Ground pin 1 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 1 is Connected \n')
    pi.digitalWrite(96,0)
    pi.pinMode(96,0)
    pi.pinMode(98,1)  #next output
    pi.digitalWrite(98,1)
    readoutb = pi.digitalRead(97)
    if readoutb == 0:
        f1.write('Ground pin 1/5 is Not Connected Adjacent \n')
    elif readoutb == 1:
        f1.write('Ground pin 1/5 is Connected Adjacent \n')
    reset()
    #0x22 pin 98 -> out -> ground pin 5
    #0x26 pin 169 -> in
    #already did adjacent to 1
    pi.pinMode(98,1)  #output
    pi.pinMode(169,0)  #input
    pi.digitalWrite(98,1)  #output to high
    readouta = pi.digitalRead(169)
    if readouta == 0:
        f1.write('Ground pin 5 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 5 is Connected \n')
        
reset()

#0x22 pin 99 -> in -> ground pin 2
#0x22 pin 97 -> out -> ground pin 1
#adjacent 0x22 pin 100 -> out -> ground pin 6
with open(ground_file, 'a') as f1:
    pi.pinMode(97,1)  #output
    pi.pinMode(99,0)  #input
    pi.digitalWrite(97,1)  #output to high
    readouta = pi.digitalRead(99)
    if readouta == 0:
        f1.write('Ground pin 2 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 2 is Connected \n')
    pi.digitalWrite(97,0)
    pi.pinMode(97,0)
    pi.pinMode(100,1)  #next output
    pi.digitalWrite(100,1)
    readoutb = pi.digitalRead(99)
    if readoutb == 0:
        f1.write('Ground pin 2/6 is Not Connected Adjacent \n')
    elif readoutb == 1:
        f1.write('Ground pin 2/6 is Connected Adjacent \n')
    reset()
    #0x22 pin 100 -> out -> ground pin 6
    #0x22 pin 98 -> in -> ground pin 5
    #already did adjacent to 2
    pi.pinMode(100,1)  #output
    pi.pinMode(98,0)  #input
    pi.digitalWrite(100,1)  #output to high
    readouta = pi.digitalRead(98)
    if readouta == 0:
        f1.write('Ground pin 6 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 6 is Connected \n')


reset()

#0x22 pin 101 -> in -> ground pin 3
#0x22 pin 99 -> out -> ground pin 2
#adjacent 0x22 pin 102 -> out -> ground pin 7
with open(ground_file, 'a') as f1:
    pi.pinMode(99,1)  #output
    pi.pinMode(101,0)  #input
    pi.digitalWrite(99,1)  #output to high
    readouta = pi.digitalRead(101)
    if readouta == 0:
        f1.write('Ground pin 3 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 3 is Connected \n')
    pi.digitalWrite(99,0)
    pi.pinMode(99,0)
    pi.pinMode(102,1)  #next output
    pi.digitalWrite(102,1)
    readoutb = pi.digitalRead(101)
    if readoutb == 0:
        f1.write('Ground pin 3/7 is Not Connected Adjacent \n')
    elif readoutb == 1:
        f1.write('Ground pin 3/7 is Connected Adjacent \n')
    reset()
    #0x22 pin 102 -> out -> ground pin 7
    #0x22 pin 101 -> in -> ground pin 6
    #already did adjacent to 3
    pi.pinMode(102,1)  #output
    pi.pinMode(101,0)  #input
    pi.digitalWrite(102,1)  #output to high
    readouta = pi.digitalRead(101)
    if readouta == 0:
        f1.write('Ground pin 7 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 7 is Connected \n')

        
reset()

#0x22 pin 103 -> in -> ground pin 4
#0x22 pin 101 -> out -> ground pin 3
#adjacent 0x22 pin 104 -> out -> ground pin 8
with open(ground_file, 'a') as f1:
    pi.pinMode(101,1)  #output
    pi.pinMode(103,0)  #input
    pi.digitalWrite(101,1)  #output to high
    readouta = pi.digitalRead(103)
    if readouta == 0:
        f1.write('Ground pin 4 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 4 is Connected \n')
    pi.digitalWrite(101,0)
    pi.pinMode(101,0)
    pi.pinMode(104,1)  #next output
    pi.digitalWrite(104,1)
    readoutb = pi.digitalRead(103)
    if readoutb == 0:
        f1.write('Ground pin 4/8 is Not Connected Adjacent \n')
    elif readoutb == 1:
        f1.write('Ground pin 4/8 is Connected Adjacent \n')
    reset()
    #0x22 pin 104 -> out -> ground pin 8
    #0x22 pin 102 -> in -> ground pin 7
    #already did adjacent to 4
    pi.pinMode(104,1)  #output
    pi.pinMode(102,0)  #input
    pi.digitalWrite(104,1)  #output to high
    readouta = pi.digitalRead(102)
    if readouta == 0:
        f1.write('Ground pin 8 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 8 is Connected \n')
        
#0x24 pin 136 -> in -> ground pin 12
#0x20 pin 65 -> out
#adjacent 0x24 pin 132 -> out -> ground pin 16
with open(ground_file, 'a') as f1:
    pi.pinMode(65,1)  #output
    pi.pinMode(136,0)  #input
    pi.digitalWrite(65,1)  #output to high
    readouta = pi.digitalRead(136)
    if readouta == 0:
        f1.write('Ground pin 12 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 12 is Connected \n')
    pi.digitalWrite(65,0)
    pi.pinMode(65,0)
    pi.pinMode(132,1)  #next output
    pi.digitalWrite(132,1)
    readoutb = pi.digitalRead(136)
    if readoutb == 0:
        f1.write('Ground pin 12/16 is Not Connected Adjacent \n')
    elif readoutb == 1:
        f1.write('Ground pin 12/16 is Connected Adjacent \n')
    reset()
    #0x24 pin 132 -> out -> ground pin 16
    #0x22 pin 112 -> in
    #already did adjacent to 12
    pi.pinMode(132,1)  #output
    pi.pinMode(112,0)  #input
    pi.digitalWrite(132,1)  #output to high
    readouta = pi.digitalRead(112)
    if readouta == 0:
        f1.write('Ground pin 16 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 16 is Connected \n')
        
reset()

#0x24 pin 135 -> in -> ground pin 11
#0x24 pin 136 -> out -> ground pin 12
#adjacent 0x24 pin 131 -> out -> ground pin 15
with open(ground_file, 'a') as f1:
    pi.pinMode(136,1)  #output
    pi.pinMode(135,0)  #input
    pi.digitalWrite(136,1)  #output to high
    readouta = pi.digitalRead(135)
    if readouta == 0:
        f1.write('Ground pin 11 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 11 is Connected \n')
    pi.digitalWrite(136,0)
    pi.pinMode(136,0)
    pi.pinMode(131,1)  #next output
    pi.digitalWrite(131,1)
    readoutb = pi.digitalRead(135)
    if readoutb == 0:
        f1.write('Ground pin 11/15 is Not Connected Adjacent \n')
    elif readoutb == 1:
        f1.write('Ground pin 11/15 is Connected Adjacent \n')
    reset()
    #0x24 pin 131 -> out -> ground pin 15
    #0x24 pin 132 -> in -> ground pin 16
    #already did adjacent to 11
    pi.pinMode(131,1)  #output
    pi.pinMode(132,0)  #input
    pi.digitalWrite(131,1)  #output to high
    readouta = pi.digitalRead(132)
    if readouta == 0:
        f1.write('Ground pin 15 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 15 is Connected \n')
        
reset()

#0x24 pin 134 -> in -> ground pin 10
#0x24 pin 135 -> out -> ground pin 11
#adjacent 0x24 pin 130 -> out -> ground pin 14
with open(ground_file, 'a') as f1:
    pi.pinMode(135,1)  #output
    pi.pinMode(134,0)  #input
    pi.digitalWrite(135,1)  #output to high
    readouta = pi.digitalRead(134)
    if readouta == 0:
        f1.write('Ground pin 10 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 10 is Connected \n')
    pi.digitalWrite(135,0)
    pi.pinMode(135,0)
    pi.pinMode(130,1)  #next output
    pi.digitalWrite(130,1)
    readoutb = pi.digitalRead(134)
    if readoutb == 0:
        f1.write('Ground pin 10/14 is Not Connected Adjacent \n')
    elif readoutb == 1:
        f1.write('Ground pin 10/14 is Connected Adjacent \n')
    reset()
    #0x24 pin 130 -> out -> ground pin 14
    #0x24 pin 131 -> in -> ground pin 15
    #already did adjacent to 10
    pi.pinMode(130,1)  #output
    pi.pinMode(131,0)  #input
    pi.digitalWrite(130,1)  #output to high
    readouta = pi.digitalRead(131)
    if readouta == 0:
        f1.write('Ground pin 14 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 14 is Connected \n')

reset()

#0x24 pin 133 -> in -> ground pin 9
#0x24 pin 134 -> out -> ground pin 10
#adjacent 0x24 pin 129 -> out -> ground pin 13
with open(ground_file, 'a') as f1:
    pi.pinMode(134,1)  #output
    pi.pinMode(133,0)  #input
    pi.digitalWrite(134,1)  #output to high
    readouta = pi.digitalRead(133)
    if readouta == 0:
        f1.write('Ground pin 9 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 9 is Connected \n')
    pi.digitalWrite(134,0)
    pi.pinMode(134,0)
    pi.pinMode(129,1)  #next output
    pi.digitalWrite(129,1)
    readoutb = pi.digitalRead(133)
    if readoutb == 0:
        f1.write('Ground pin 9/13 is Not Connected Adjacent \n')
    elif readoutb == 1:
        f1.write('Ground pin 9/13 is Connected Adjacent \n')
    reset()
    #0x24 pin 129 -> out -> ground pin 13
    #0x24 pin 130 -> in -> ground pin 14
    #already did adjacent to 9
    pi.pinMode(129,1)  #output
    pi.pinMode(130,0)  #input
    pi.digitalWrite(129,1)  #output to high
    readouta = pi.digitalRead(130)
    if readouta == 0:
        f1.write('Ground pin 13 is Not Connected \n')
    elif readouta == 1:
        f1.write('Ground pin 13 is Connected \n')


