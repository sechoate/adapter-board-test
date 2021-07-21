# Adapter Board Test
This is the Python code for testing Dune adapter boards. Additional requirements for running are a Raspberry Pi, a custom test board, and a Dune adapter board. 

## Additional Requirements 
There are three additional hardware requirements for working with this code. First is a Raspberry Pi. During the writing of the code, a Raspberry Pi 3 model B V 1.2 was used. This is an important detail because if a different model is used then the numbering of the pins are not guarateed to be the same. The second requirement is a custom test board. The layout for the test board is included in the repoistory under the name Dune Test Jig PCB Layout Final.pdf. The obvious third requirement would be the Dune adapter board that is being tested, which is plugged into the test board. 
### Reading the Test Board Layout 
The test board mainly consists of a Raspberry Pi header, which connects to a Raspberry Pi using a ribbon cable, and seven additional MCP23017 I/O expanders each with their own hex address and set number of pins. The Pi header is labeled as J1 while each of the expanders are labeled U1-U8 (they are not placed on the board in numerical order). 

- U1 corresponds to the expander that is addressed as 0x20 and this uses pins 65-80. 
- U2 corresponds to 0x21 and uses pins 81-96. 
- U3 corresponds to 0x22 and uses pins 97-112. 
- U4 corresponds to 0x23 and uses pins 113-128. 
- U5 corresponds to 0x24 and uses pins 129-144. 
- U6 corresponds to 0x25 and uses pins 145-160. 
- U7 corresponds to 0x26 and uses pins 161-176. 
- U8 corresponds to 0x27 and uses pins 177-192. 

These addresses and pin numbers are set up at the beginning of the code. Other components of the test board which are labeled include J2, J3, J4, and J5. These are the regions that the adapter board will plug into. It will be plugged directly into J4 and J5 and will be connected with ribbon cables for J2 and J3. 

## Method
### Numbering
Each space on the test board has a corresponding number which is determined by what it is connected to, either an I/O expander or the Pi header. When the adapter board is plugged in, the pins subsequently recieve the number corresponding to the space on the test board they are plugged into. The package used in the code is called wiringpi and so the wiringpi numbering system is used.
#### Pi Header
The physcial board numbers and their associated wiringpi numbers can be found by inputting the command "gpio readall" in the terminal when connected to the Raspberry Pi. Inputting "pinout" in the terminal will give a visual representaion of the physical pin numbering of the board. The "gpio readall" input will output a table of physical pin numbers and their corresponding wiringpi numbers. The wiringpi numbers were used in the code and the pins used can be found by using the test board layout document and tracing the wiring from each applicable space on J4 to the Pi header. This gives the physical number to be converted to a wiringpi number.  
#### MCP23017 I/O Expanders
As mentioned previously, each expander has a corresponding address and set number of pins. Sixteen pins on each expander are able to be used as I/O pins. When looking at the test board layout document, these are the top eight pins on U1-U8 on each side with the right side being side A and the left side being side B. The following image shows the numbering system on these expanders (from https://learn.adafruit.com/mcp230xx-gpio-expander-on-the-raspberry-pi/hooking-it-all-up):

![mcp23017](https://user-images.githubusercontent.com/87721944/126425425-3c148019-5ee0-4a77-8128-35377a87cc8f.png)

The numbering starts with GPA0 and goes numerically through GPB7. For example, for U1 which is addressed as 0x20, the pin corresponding to A0 would be numbered 65 in the code and the pin corresponding to B0 would be numbered 73. I/O pins which are used in the code are only able to be connected to GPA/B, so those are the only ones we need to worry about numbering. 
### The Code
The main idea of the code is that the pins on the J4 side of the test board will always be set as outputs while the pins on the J5 side of the test board will always be set as inputs. The middle row is all connected together as a ground line and there are eight additional ground pins in the middle of each row on the adapter board, these become more obvious when looking at the adapter board. Pairs are defined by the pairs of pins that should be connected. For example, when looking at the test board layout, the pins on the adapter board corresponding to the first spot on J4 and last spot on J5 on the left row of the test board should be connected to each other and this is defined as pair 1. Similarly the pins corresponding to the first spot on J4 and last spot on J5 on the right row should be connected to each other and are defined as pair 33. Each pin is in one pair so there is only one connection per pin and adjacent pins should not be connected, this will be reflected in the outputs. The code begins by defining a reset function which sets all the voltages on the expanders to zero in order to reduce the possibility of a floating voltage giving an improper readout. From there it goes pair by pair, first testing the pins that should be connected and then testing the pins that should not be connected. So, for the first pin on J4 on the left row when looking at the test board layout, it will test to see that the pin is connected to the last pin on J5 on the left row by setting the first pin to a high voltage (~3.3 V) and then reading the last pin to see if it reads a high voltage as well. It will then go through every other possible pin on the input side, keeping the first pin set to a high voltage, skipping the last pin since we already tested that one, and reading if there are any other pins reading a high voltage indicating they are connected to the first pin. The output pin is then set to a low voltage (0 V) and the reset function is run again and we move onto the next pair. This process is repeated for every pin on the output side of the board. The middle ground rail is tested in a similar fashion where the ground pin is set high and tested with every expander on the J5 side of the test board to see if anything is connected. The additional eight ground pins are just tested against the pins in the surrounding area, but the method is similar. All the results are output in three files, which are discussed in a later section.      

## User Input
The user only needs to change the saved names (**not** variable names, don't change those) of the output files, if necessary, at the beginning of the code.

## Outputs 
As mentioned, there are three output files with variable names connected_file, adjacent_file, and ground_file (the actual txt file names can and most likely will be changed).    
### connected_file
This is the output for the connected pairs of pins. The readout will be of the form "Pair {} is Connected/Not Connected" where {} is the pair number. For a working adapter board, all pairs should read as connected. If a pair reads not connected then this is a problem that needs to be further examined on the adapter board.
### adjacent_file
This is the output file for the adjacent pairs of pins which should not be connected. An event that would lead to adjacent pins being connected would be if there was excess solder connecting the adjacent pins. The output will be of the form "Pin {} is Connected/Not Connected" where {} is the pin number which corresponds to the pin number of the expander that it is connected to. For a working adapter board, all adjacent pins should read as not connected. If a pair reads as connected then there is a problem that needs to be further examined on the adapter board. 
### ground_file
This is the output file for the ground pins, both the main ground rail and the eight additional ground pins. They are of similar format to the other files with the pin number being whatever corresponding number on the expander that pin is connected to. The readout should all be not connected. If any read as connected then there is a problem on the adapter board. 

It is also important to note that the reason we are able to have one side of the board remain as outputs and the other remain as inputs is because of the way the pairs are connected. Since each pin on the output side is connected to only one pin on the input side, if adjacent pins are connected to the output pin this will be reflected in the reading of the input pin. If we refer back to the first and last pin on the left side when looking at the test board, let's say that some solder is bridging the first pin of the left side and the first pin on the right side. The output of connected_file would then read that pair 1 and pair 33 are not connected and the output of adjacent_file would read under the appropriate pin number that pin 177 is connected and pin 152 is connected. This demonstrates that even though we don't explicitly test the first pins on the left and right side of the test board, the connection will still be caught since both pins are connected to an input pin which is being tested. 
## Troubleshooting code + gui
