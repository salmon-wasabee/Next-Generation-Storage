import tkinter as tk
import serial
from RFID import read_rfid  # Import the read_rfid function from RFID.py
import time

# Serial port configuration
SERIAL_PORT = '/dev/serial/by-id/usb-Arduino_UNO_R4_Minima_38101818373233355BD333324B572D3A-if00'  # Update this to the correct port
BAUD_RATE = 115200

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

# Function to handle button press and release events for all directions
def on_button_press(*commands):
    for command in commands:
        send_command(command)

def on_button_release(event):
    send_command("STOP1")
    send_command("STOP2")
    
def read_rfid_loop():
    # Assuming the RFID reader reads the value "0007677391" and stores it in the variable rfid_value
    rfid_value = "0007677391"

    # Call the read_rfid function with the RFID value and the Entry widget
    is_valid = read_rfid(rfid_value, entry_widget)

    # Print the result
    print(f"The RFID card with value {rfid_value} is valid: {is_valid}")

    # Schedule the read_rfid_loop function to be called again after 1 second (1000 milliseconds)
    root.after(1000, read_rfid_loop)



# Create main window
root = tk.Tk()
root.title("Dual Stepper Motor Controller")

entry_widget = tk.Entry(root)
entry_widget.grid(row=0, column=0)  # Use grid instead of pack


# Schedule the read_rfid_loop function to be called after 1 second (1000 milliseconds)
root.after(1000, read_rfid_loop)

# Create and place widgets
steps_label = tk.Label(root, text="Control:")
steps_label.grid(row=1, column=0, columnspan=3)

# Entry widget for RFID input
rfid_entry = tk.Entry(root)
rfid_entry.grid(row=5, column=0)

# Add a button to read RFID
read_rfid_button = tk.Button(root, text="Read RFID", command=lambda: read_rfid(rfid_entry.get(), entry_widget))
read_rfid_button.grid(row=5, column=1)


# Create buttons with press and release event bindings for all directions
up_button = tk.Button(root, text="Up")
up_button.bind('<ButtonPress>', lambda event: on_button_press("CCW1", "CW2"))
up_button.bind('<ButtonRelease>', on_button_release)
up_button.grid(row=1, column=1)

down_button = tk.Button(root, text="Down")
down_button.bind('<ButtonPress>', lambda event: on_button_press("CW1", "CCW2"))
down_button.bind('<ButtonRelease>', on_button_release)
down_button.grid(row=3, column=1)

left_button = tk.Button(root, text="Left")
left_button.bind('<ButtonPress>', lambda event: on_button_press("CW1", "CW2"))
left_button.bind('<ButtonRelease>', on_button_release)
left_button.grid(row=2, column=0)

right_button = tk.Button(root, text="Right")
right_button.bind('<ButtonPress>', lambda event: on_button_press("CCW1", "CCW2"))
right_button.bind('<ButtonRelease>', on_button_release)
right_button.grid(row=2, column=2)

# Diagonal direction buttons
up_left_button = tk.Button(root, text="Up-Left")
up_left_button.bind('<ButtonPress>', lambda event: on_button_press("STOP1", "CW2"))
up_left_button.bind('<ButtonRelease>', on_button_release)
up_left_button.grid(row=1, column=0)

up_right_button = tk.Button(root, text="Up-Right")
up_right_button.bind('<ButtonPress>', lambda event: on_button_press("CCW1", "STOP2"))
up_right_button.bind('<ButtonRelease>', on_button_release)
up_right_button.grid(row=1, column=2)

down_left_button = tk.Button(root, text="Down-Left")
down_left_button.bind('<ButtonPress>', lambda event: on_button_press("CW1", "STOP2"))
down_left_button.bind('<ButtonRelease>', on_button_release)
down_left_button.grid(row=3, column=0)

down_right_button = tk.Button(root, text="Down-Right")
down_right_button.bind('<ButtonPress>', lambda event: on_button_press("STOP1", "CCW2"))
down_right_button.bind('<ButtonRelease>', on_button_release)
down_right_button.grid(row=3, column=2)

status_label = tk.Label(root, text="Press and hold the buttons to move the stepper motors")
status_label.grid(row=4, column=0, columnspan=3)

# Run the main event loop
root.mainloop()
