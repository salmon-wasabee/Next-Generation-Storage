#!/usr/bin/env python3

import tkinter as tk
import serial
import time

# Serial port configuration
SERIAL_PORT = '/dev/serial/by-id/usb-Arduino_UNO_R4_Minima_38101818373233355BD333324B572D3A-if00'  # Update this to the correct port
BAUD_RATE = 9600

# Function to send command to Arduino
def send_command(command):
    command_with_newline = command + '\n'  # Append newline character
    ser.write(command_with_newline.encode())
    status_label.config(text=f"Command sent: {command}")


# Function to move stepper motor forward (clockwise)
def move_forward():
    send_command("CW")

# Function to move stepper motor backward (counter-clockwise)
def move_backward():
    send_command("CCW")

# Initialize serial connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
except serial.SerialException:
    print("Serial port not available")
    exit()

# Create main window
root = tk.Tk()
root.title("Stepper Motor Controller")

# Create and place widgets
steps_label = tk.Label(root, text="Control:")
steps_label.grid(row=0, column=0)

forward_button = tk.Button(root, text="Forward", command=move_forward)
forward_button.grid(row=1, column=0)

backward_button = tk.Button(root, text="Backward", command=move_backward)
backward_button.grid(row=1, column=1)

status_label = tk.Label(root, text="Send CW for forward, CCW for backward")
status_label.grid(row=2, columnspan=2)

# Run the main event loop
root.mainloop()
