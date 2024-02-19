import tkinter as tk
import serial
import time

# Serial port configuration
SERIAL_PORT = '/dev/tty'
BAUD_RATE = 9600

# Function to send steps to Arduino
def send_steps(steps):
    ser.write(str(steps).encode())
    status_label.config(text=f"Moving {steps} steps")

# Function to move stepper motor forward
def move_forward():
    send_steps(int(steps_entry.get()))

# Function to move stepper motor backward
def move_backward():
    send_steps(-int(steps_entry.get()))

# Initialize serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Create main window
root = tk.Tk()
root.title("Stepper Motor Controller")

# Create and place widgets
steps_label = tk.Label(root, text="Steps:")
steps_label.grid(row=0, column=0)

steps_entry = tk.Entry(root)
steps_entry.grid(row=0, column=1)

forward_button = tk.Button(root, text="Forward", command=move_forward)
forward_button.grid(row=1, column=0)

backward_button = tk.Button(root, text="Backward", command=move_backward)
backward_button.grid(row=1, column=1)

status_label = tk.Label(root, text="")
status_label.grid(row=2, columnspan=2)

# Run the main event loop
root.mainloop()

# Close serial connection when exiting
ser.close()

