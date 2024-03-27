import serial

# Define the serial port and baud rate. Adjust these values based on your RFID reader's specifications.
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Initialize the serial connection
rfid_reader = serial.Serial(SERIAL_PORT, BAUD_RATE)

def read_rfid():
    # Read data from the RFID reader
    data = rfid_reader.readline().decode('utf-8').strip()
    return data

# Continuously read and print RFID data
try:
    while True:
        tag_id = read_rfid()
        print(f"RFID Tag ID: {tag_id}")
except KeyboardInterrupt:
    # Close the serial connection when the script is stopped
    rfid_reader.close()
    print("RFID reader closed.")
