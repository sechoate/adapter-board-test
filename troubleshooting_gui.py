import PySimpleGUI as sg
import wiringpi as pi
from time import sleep



layout = [[sg.Text('Enter Pin 1')],
          [sg.Input()],
          [sg.Text('Enter Pin 2')],
          [sg.Input()],
          [sg.Button('Run')],
          [sg.Output(size=(50,10), key='-OUTPUT-')]]

window = sg.Window('Troubleshooting', layout)

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




while True:
    event, values = window.read()
    
    #print(type(int(values[0])))
    values1 = int(values[0])
    values2 = int(values[1])
    
    out = pi.pinMode(values1,1)
    high = pi.digitalWrite(values1,1)
    read = pi.digitalRead(values2)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        window['-OUTPUT-'].update(values['-IN-'])
    print('Pin {} reads {}'.format(values1,read))


window.close()









