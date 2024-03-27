# RFID.py
import time

def read_rfid(input_value, text_widget):
    # The expected RFID value
    expected_value = "0007677391"
    
    # Check if the input value matches the expected value
    if input_value == expected_value:
        # Insert the value into the text widget
        text_widget.insert('end', input_value)
        print(True)  # Print True to the terminal
        return True
    else:
        print(False)  # Print False to the terminal
        return False

while True:
    # Assuming 'entry_widget' is the Tkinter Entry widget where the RFID value should be inserted
    # Assuming the RFID reader reads the value and stores it in the variable rfid_value
    rfid_value = "0007677391"  # Replace this line with the code to read the RFID value

    # Call the read_rfid function with the RFID value and the Entry widget
    is_valid = read_rfid(rfid_value, entry_widget)  # Replace 'entry_widget' with your actual Entry widget

    # Wait for 1 second
    time.sleep(1)