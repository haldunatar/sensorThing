import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(17, GPIO.OUT) # Set pin 17 as output

try:
    while True:
        GPIO.output(17, GPIO.HIGH)  # Turn ON
        print("GPIO 17 ON")
        time.sleep(5)              # Wait 5 seconds
        
        GPIO.output(17, GPIO.LOW)   # Turn OFF
        print("GPIO 17 OFF")
        time.sleep(5)              # Wait 5 seconds

except KeyboardInterrupt:
    print("\nStopped by user")

finally:
    GPIO.cleanup()  # Clean up GPIO settings on exit