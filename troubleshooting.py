import wiringpi as pi
from time import sleep


pi.wiringPiSetup()

#set up all mcp23017 
pi.mcp23017Setup(65,0x20)
pi.mcp23017Setup(81,0x21)
pi.mcp23017Setup(97,0x22)
pi.mcp23017Setup(113,0x23)
pi.mcp23017Setup(129,0x24)
pi.mcp23017Setup(145,0x25)
pi.mcp23017Setup(161,0x26)
pi.mcp23017Setup(177,0x27)


#example, first and last pin are acting up
#input them to just test their connection

print('first, we need to set the desired pins both to inputs')
print('this ensures there isnt a problem with them')

left_pin = input("enter value of left pin:\n")
right_pin = input("enter value of right pin:\n")
vL = int(left_pin)
vR = int(right_pin)

print(f'left pin is pin {vL} and reads {pi.digitalRead(vL)}')
print(f'right pin is pin {vR} and reads {pi.digitalRead(vR)}')
print('both pins are now set to inputs and should read 0 unless stated otherwise')
print('  ')

print('now we set the left pin to an output pin and set to a high voltage')
pi.pinMode(vL,1)
pi.digitalWrite(vL,1)
print('and read the value of the input pin, which is the right pin')
print(f'output pin {vL} set high, right pin {vR} reads {pi.digitalRead(vR)}')
print('  ')

print('if the pins are connected this will read 1, if not it will read 0')
print('  ')

print('finally, we set the output pin back to low and then back to an input')
print('this is so we can make sure the output pin is working correctly unless noted otherwise')
pi.digitalWrite(vL,0)
pi.pinMode(vL,0)
sleep(5)
print(f'left pin is pin {vL} and reads {pi.digitalRead(vL)}')
print(f'right pin is pin {vR} and reads {pi.digitalRead(vR)}')









