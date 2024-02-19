import serial

# Function to send command to Arduino
def send_command(ser, status_label, command):
    command_with_newline = command + '\n'  # Append newline character
    ser.write(command_with_newline.encode())
    status_label.config(text=f"Command sent: {command}")

# Function to move stepper motor forward (clockwise)
def move_forward(ser, status_label):
    send_command(ser, status_label, "CW")

# Function to move stepper motor backward (counter-clockwise)
def move_backward(ser, status_label):
    send_command(ser, status_label, "CCW")
