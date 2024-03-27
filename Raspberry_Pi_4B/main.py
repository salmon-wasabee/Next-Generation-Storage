import tkinter as tk
import serial
from RFID import read_rfid  # Import the read_rfid function from RFID.py

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
    
# Function to read RFID and update status
def read_rfid_and_update_status():
    try:
        # Assuming ser.readline() is the way you read from the serial port connected to the RFID reader
        rfid_value = ser.readline().decode().strip()
        is_valid = read_rfid(rfid_value)
        status_label.config(text=f"RFID valid: {is_valid}")
    except Exception as e:
        status_label.config(text=f"Error reading RFID: {e}")



# Create main window
root = tk.Tk()
root.title("Dual Stepper Motor Controller")

# Create and place widgets
steps_label = tk.Label(root, text="Control:")
steps_label.grid(row=0, column=0, columnspan=3)

# Add a button to read RFID
read_rfid_button = tk.Button(root, text="Read RFID", command=read_rfid_and_update_status)
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
