#!/usr/bin/env python3
import tkinter as tk
import serial
from arduino_commands import move_forward, move_backward
from ui import create_ui

# Serial port configuration
SERIAL_PORT = '/dev/serial/by-id/usb-Arduino_UNO_R4_Minima_38101818373233355BD333324B572D3A-if00'
BAUD_RATE = 9600

# Initialize serial connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
except serial.SerialException:
    print("Serial port not available")
    exit()

# Create the root window first
root = tk.Tk()

# Now it's safe to create Tkinter variables
status_label_text_var = tk.StringVar(value="Send CW for forward, CCW for backward")

# Create UI
create_ui(ser, move_forward, move_backward, status_label_text_var)

# Run the main event loop
root.mainloop()

# Close serial connection when exiting
ser.close()
