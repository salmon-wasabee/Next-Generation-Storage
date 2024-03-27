# RFID.py

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

# Example usage
# Assuming the RFID reader reads the value "0007677391" and stores it in the variable rfid_value
# Assuming 'entry_widget' is the Tkinter Entry widget where the RFID value should be inserted
rfid_value = "0007677391"
entry_widget = None  # Replace with actual Entry widget reference

# Call the read_rfid function with the RFID value and the Entry widget
is_valid = read_rfid(rfid_value, entry_widget)

# Print the result
print(f"The RFID card with value {rfid_value} is valid: {is_valid}")
