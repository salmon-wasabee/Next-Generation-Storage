import tkinter as tk
import serial

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

# Function to stop stepper motors
def stop_motors():
    send_command("STOP1")
    send_command("STOP2")

# Create main window
root = tk.Tk()
root.title("Dual Stepper Motor Controller")

# Create and place widgets
status_label = tk.Label(root, text="Use the buttons to move the stepper motors")
status_label.grid(row=4, column=0, columnspan=3)

# Define button press and release events
def on_press(event):
    send_command(event.widget.cw_command)

def on_release(event):
    stop_motors()

# Create buttons with associated commands and bind events
buttons = {
    "Up": "CCW1 CW2",
    "Down": "CW1 CCW2",
    "Left": "CW1 CW2",
    "Right": "CCW1 CCW2",
    "Up-Left": "STOP1 CW2",
    "Up-Right": "CCW1 STOP2",
    "Down-Left": "CW1 STOP2",
    "Down-Right": "STOP1 CCW2"
}

for text, command in buttons.items():
    button = tk.Button(root, text=text)
    button.cw_command = command
    button.bind("<ButtonPress>", on_press)
    button.bind("<ButtonRelease>", on_release)
    button.grid()

# Run the main event loop
root.mainloop()
