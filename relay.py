import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(18, GPIO.OUT) # Set pin 18 as output

try:
    while True:
        GPIO.output(18, GPIO.LOW)  # Turn ON
        print("GPIO 18 ON")
        time.sleep(60)              # Wait 5 seconds

        GPIO.output(18, GPIO.HIGH)   # Turn OFF
        print("GPIO 18 OFF")
        time.sleep(60)              # Wait 5 seconds

except KeyboardInterrupt:
    print("\nStopped by user")

finally:
    GPIO.cleanup()  # Clean up GPIO settings on exit