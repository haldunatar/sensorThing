import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Disable GPIO warnings

# Define the GPIO pins for the trigger and echo
TRIG = 23
ECHO = 24

# Set up the GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distance():
    # Ensure the trigger pin is set to LOW
    GPIO.output(TRIG, False)
    time.sleep(0.05)  # Shorter delay to allow sensor to settle
    
    # Send a 10us pulse to trigger the sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Record the start time
    start_time = time.time()
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Record the arrival time of the echo
    stop_time = start_time
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    # Check if we have valid times before calculating distance
    if start_time == stop_time:
        return float('inf')  # Indicates an error or out of range

    # Calculate the time difference
    time_elapsed = stop_time - start_time

    # Calculate the distance in cm (speed of sound is 34300 cm/s)
    distance = (time_elapsed * 34300) / 2

    return distance

# Threshold distance for detection in cm
threshold_distance = 25.0

try:
    while True:
        current_dist = distance()
        if current_dist == float('inf'):
            print("Out of range or error in measurement")
        elif current_dist < threshold_distance:
            print("Detected! Something is within 25 cm")
        else:
            print(f"Measured Distance = {current_dist:.1f} cm")
        
        # Shorter sleep time for faster loop iteration
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
