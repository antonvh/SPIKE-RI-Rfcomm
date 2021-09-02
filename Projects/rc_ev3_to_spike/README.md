# Remote controlling an EV3 robot with a Robot Inventor hub in Python

## LEGO used in this demo
Just two simple robots: 
- One EV3 brick with motors in ports B and C
- A simple spike tank robot with a caster wheel. Motors in ports A and B.
![Remote control EV3 and SPIKE Prime robots](robots.jpeg)

## Installation
1. Run ev3dev.org on your EV3 brick
2. Pair the hub with the EV3 brick through brickman on the EV3 brick. Remember to press the little Bluetooth button on the hub. 
3. Write down the Bluetooth address when done. It looks like this: `A8:E2:C1:9B:A0:61`

## Usage
Control the tank with the EV3 motors
Press the center button on the EV3 brick to stop

## How it works
The EV3 brick sets motor voltages using a REPL command over Bluetooth RFCOMM. 