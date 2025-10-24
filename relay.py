# button_toggle_perfect.py
import RPi.GPIO as GPIO
import time

BUTTON = 17   # GPIO 17 (pin 11)
RELAY  = 18    # GPIO 1  (pin 7)  ← YOUR WORKING PIN

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RELAY, GPIO.OUT)

# Start OFF
GPIO.output(RELAY, GPIO.LOW)
light_on = False
button_was_pressed = False  # Track button state

print("Lamp OFF. Press button to toggle. Ctrl-C to stop.")

try:
    while True:
        button_is_pressed = GPIO.input(BUTTON) == GPIO.HIGH

        # Detect RISING EDGE: button goes from NOT pressed → PRESSED
        if button_is_pressed and not button_was_pressed:
            print("BUTTON PRESSED! (edge detected)")
            time.sleep(0.01)  # tiny debounce

            # Confirm still pressed
            if GPIO.input(BUTTON) == GPIO.HIGH:
                light_on = not light_on
                GPIO.output(RELAY, GPIO.HIGH if light_on else GPIO.LOW)
                print(f"Lamp → {'ON' if light_on else 'OFF'}")

        # Save current state for next loop
        button_was_pressed = button_is_pressed

        time.sleep(0.01)  # small delay to reduce CPU usage

except KeyboardInterrupt:
    print("\nCtrl-C → turning lamp OFF")
    GPIO.output(RELAY, GPIO.LOW)
finally:
    GPIO.cleanup()
    print("Clean exit.")