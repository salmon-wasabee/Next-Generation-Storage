# RFID.py
import tkinter as tk

def read_rfid(input_value, text_widget):
    # The expected RFID value
    expected_value = "0007677391"
    
    # Check if the input value matches the expected value
    if input_value == expected_value:
        # Insert the value into the text widget
        text_widget.insert('end', input_value)
        return True
    else:
        return False

