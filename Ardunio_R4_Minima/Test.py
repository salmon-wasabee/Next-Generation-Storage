import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600) # Change port if necessary
time.sleep(2) # Allow some time for the connection to establish

def move_forward():
    ser.write(b'F')

def move_backward():
    ser.write(b'B')

# Example usage
move_forward()
time.sleep(2) # Wait for 2 seconds
move_backward()

# Close the serial connection when done
ser.close()
