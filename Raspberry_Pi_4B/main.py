#!/usr/bin/env python3

import tkinter as tk
import serial

# Serial port configuration
SERIAL_PORT = '/dev/serial/by-id/usb-Arduino_UNO_R4_Minima_38101818373233355BD333324B572D3A-if00'  # Update this to the correct port
BAUD_RATE = 9600

# Initialize serial connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
except Exception as e:
    print(f"Serial port not available: {e}")
    exit()

# Function to send command to Arduino
def send_command(command):
    command_with_newline = command + '\n'  # Append newline character
    ser.write(command_with_newline.encode())
    status_label.config(text=f"Command sent: {command}")

# Function to move stepper motors in the UP direction
def move_up():
    send_command("CCW1")
    send_command("CW2")

# Function to move stepper motors in the DOWN direction
def move_down():
    send_command("CW1")
    send_command("CCW2")

# Function to move stepper motors in the LEFT direction
def move_left():
    send_command("CW1")
    send_command("CW2")

# Function to move stepper motors in the RIGHT direction
def move_right():
    send_command("CCW1")
    send_command("CCW2")

# Function to move stepper motors diagonally UP-LEFT
def move_up_left():
    send_command("STOP1")
    send_command("CW2")

# Function to move stepper motors diagonally UP-RIGHT
def move_up_right():
    send_command("CCW1")
    send_command("STOP2")

# Function to move stepper motors diagonally DOWN-LEFT
def move_down_left():
    send_command("CW1")
    send_command("STOP2")

# Function to move stepper motors diagonally DOWN-RIGHT
def move_down_right():
    send_command("STOP1")
    send_command("CCW2")

# Function to stop stepper motors
def stop_motors():
    send_command("STOP")

# Create main window
root = tk.Tk()
root.title("Dual Stepper Motor Controller")

# Create and place widgets
steps_label = tk.Label(root, text="Control:")
steps_label.grid(row=0, column=0, columnspan=3)

up_button = tk.Button(root, text="Up", command=move_up)
up_button.grid(row=1, column=1)

up_left_button = tk.Button(root, text="Up-Left", command=move_up_left)
up_left_button.grid(row=1, column=0)

up_right_button = tk.Button(root, text="Up-Right", command=move_up_right)
up_right_button.grid(row=1, column=2)

left_button = tk.Button(root, text="Left", command=move_left)
left_button.grid(row=2, column=0)

stop_button = tk.Button(root, text="Stop", command=stop_motors)
stop_button.grid(row=2, column=1)

right_button = tk.Button(root, text="Right", command=move_right)
right_button.grid(row=2, column=2)

down_button = tk.Button(root, text="Down", command=move_down)
down_button.grid(row=3, column=1)

down_left_button = tk.Button(root, text="Down-Left", command=move_down_left)
down_left_button.grid(row=3, column=0)

down_right_button = tk.Button(root, text="Down-Right", command=move_down_right)
down_right_button.grid(row=3, column=2)

status_label = tk.Label(root, text="Use the buttons to move the stepper motors")
status_label.grid(row=4, column=0, columnspan=3)

# Run the main event loop
root.mainloop()
