# Adapter Board Test
This is the Python code for testing Dune adapter boards. Additional requirements for running are a Raspberry Pi and a custom test board. 

## Additional Requirements 
There are three additional hardware requirements for running this code. First is a Raspberry Pi. During the writing of the code, a Raspberry Pi 3 model B V 1.2 was used. This is an important detail because if a different model is used then the numbering of the pins are not guarateed to be the same. The second requirement is a custom test board. The layout for the test board is included in the repoistory under the name Dune Test Jig PCB Layout Final.pdf. The obvious third requirement would be the Dune adapter board that is being tested, which is plugged into the test board. 
### Reading the Test Board Layout 
The test board mainly consists of a Raspberry Pi and seven additional MCP23017 I/O expanders each with their own hex address and set number of pins. The Pi is labeled as J1 while each of the expanders are labeled U1-U8 (they are not placed on the board in numerical order). U1 correcponds to the expander that is addressed as 0x20 and this uses pins 65-80. U2 corresponds to 0x21 and uses pins 81-96. U3 corresponds to 0x22 and uses pins 97-112. U4 corresponds to 0x23 and uses pins 113-128. U5 corresponds to 0x24 and uses pins 129-144. U6 corresponds to 0x25 and uses pins 145-160. U7 corresponds to 0x26 and uses pins 161-176. U8 corresponds to 0x27 and uses pins 177-192. 

## Method

## Outputs 

## Troubleshooting code + gui
