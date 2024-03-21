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

# Function to move stepper motors forward (clockwise)
def move_forward():
    send_command("CW")  # Corrected command for clockwise rotation

# Function to move stepper motors backward (counter-clockwise)
def move_backward():
    send_command("CCW")  # Corrected command for counter-clockwise rotation

# Function to stop stepper motors
def stop_motors():
    send_command("STOP")  # Corrected command to stop the motors

# Initialize serial connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
except serial.serialutil.SerialException:
    print("Serial port not available")
    exit()


# Create main window
root = tk.Tk()
root.title("Dual Stepper Motor Controller")

# Create and place widgets
steps_label = tk.Label(root, text="Control:")
steps_label.grid(row=0, column=0)

forward_button = tk.Button(root, text="Forward", command=move_forward)
forward_button.grid(row=1, column=0)

backward_button = tk.Button(root, text="Backward", command=move_backward)
backward_button.grid(row=1, column=1)

stop_button = tk.Button(root, text="Stop", command=stop_motors)
stop_button.grid(row=1, column=2)

status_label = tk.Label(root, text="Send CW1/CW2 for forward, CCW1/CCW2 for backward, STOP1/STOP2 to stop")
status_label.grid(row=2, columnspan=3)

# Run the main event loop
root.mainloop()
