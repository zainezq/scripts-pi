import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
digital_output_pin = 24 # change this pin number if necessary
led2_pin = 18 # change if necessary

# Set up GPIO pins
GPIO.setup(digital_output_pin, GPIO.IN)
GPIO.setup(led2_pin, GPIO.OUT)

try:
    while True:
        # Check if sound threshold is exceeded
        if GPIO.input(digital_output_pin):
            print("Sound detected!")
            # Turn on LED2 to indicate sound detection
            GPIO.output(led2_pin, GPIO.HIGH)
        else:
            # Turn off LED2 if no sound detected
            GPIO.output(led2_pin, GPIO.LOW)
        
        # Add a small delay to reduce CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()

