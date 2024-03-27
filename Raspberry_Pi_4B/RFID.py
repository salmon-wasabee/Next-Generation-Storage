# RFID.py

def read_rfid(input_value):
    # The expected RFID value
    expected_value = "0007677391"
    
    # Check if the input value matches the expected value
    if input_value == expected_value:
        return True
    else:
        return False

# Example usage
# Assuming the RFID reader reads the value "0007677391" and stores it in the variable rfid_value
rfid_value = "0007677391"
# Call the read_rfid function with the RFID value
is_valid = read_rfid(rfid_value)

# Print the result
print(f"The RFID card with value {rfid_value} is valid: {is_valid}")
