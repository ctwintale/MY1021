import time
import RPi.GPIO as GPIO

RGB_ENABLE = 1; RGB_DISABLE = 0

RGB_RED = 29; RGB_GREEN = 31; RGB_BLUE = 33
RGB = [RGB_RED,RGB_GREEN,RGB_BLUE]

def led_setup():
    GPIO.setmode(GPIO.BOARD)
    for val in RGB:
        GPIO.setup(val,GPIO.OUT)

def main():
    led_setup()
    for val in RGB:
        GPIO.output(val,RGB_ENABLE)
        print("LED ON")
        time.sleep(5)
        GPIO.output(val,RGB_DISABLE)
        print("LED OFF")
try:
    main()
finally:
    GPIO.cleanup()
    print("Closed Everything. END")

