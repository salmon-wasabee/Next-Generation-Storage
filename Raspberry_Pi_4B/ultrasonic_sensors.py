import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 15
GPIO_ECHO = 18

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def measure_distance():
    # Ensure the trigger pin is low
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.5)

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 10us to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = StartTime

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # check if StopTime is actually after StartTime
    if StopTime <= StartTime:
        print("Received incorrect timing values")
        return None

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

def calibrate_sensor(actual_distance):
    measured_distance = measure_distance()
    if measured_distance is None:
        print("Failed to get measurement for calibration.")
        return None

    # Calculate calibration factor
    calibration_factor = actual_distance / measured_distance
    return calibration_factor

if __name__ == '__main__':
    try:
        # Perform calibration with a known distance (in cm)
        actual_distance = float(input("Enter the actual distance for calibration (in cm): "))
        calibration_factor = calibrate_sensor(actual_distance)
        if calibration_factor is not None:
            print(f"Calibration factor: {calibration_factor}")

        while True:
            dist = measure_distance()
            if dist is not None:
                # Apply calibration factor
                calibrated_dist = dist * calibration_factor
                print(f"Measured Distance = {calibrated_dist:.1f} cm")
            else:
                print("Invalid reading")
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

