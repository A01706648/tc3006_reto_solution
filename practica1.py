import serial
# import csv
import keyboard
import matplotlib.pyplot as plt
import pandas as pd

from datetime import datetime

from pynput.keyboard import Key, Listener

q_pressed = False

def on_press(key):
    if key == 'q':
        q_pressed = True
    else:
        q_pressed = False

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

port = "COM3"  # IMPORTANT: modify this to the correct port where the arduino is connected
ser1 = serial.Serial(port, 9600) 

print("Trying to read the serial port")

entries = {
    "date": [],
    "temperature": [],
    "condition": []
}


def get_condition(temp: int) -> str:
    if temp < 21: return "optimum"

    return "warning"


pending = 100

while pending > 0 and not q_pressed:
    if keyboard.is_pressed('q'):
        print("You pressed 'q'")
        break

    # First check that the serial port is opened correctly
    if not ser1.isOpen():
        print('Serial is not open')
    else:
        while ser1.isOpen() and pending > 0:
            print('Serial is open')
            print("Pending entries: ", pending)
                
            serial_data = ser1.readline()  # Read a line of data from the serial port
            temperature = float(serial_data.strip())

            entries["date"].append(str(datetime.today()))  # Convert to string to export to csv
            entries["temperature"].append(temperature)
            entries["condition"].append(get_condition(temperature))

            pending -= 1

dataset = pd.DataFrame(entries)

print(dataset)

# Before finishing close the serial port.
print("closing the serial port")
ser1.close()  # Close the serial port

