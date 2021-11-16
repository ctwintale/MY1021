import RPi.GPIO as GPIO
from time import sleep, strftime
from datetime import datetime
import I2C_driver as LCD
from time import *

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT
switch = 10
LED = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(switch,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)


def main():
    mylcd = LCD.lcd()
    Flag=0
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)
    
    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

    while True:
        if(GPIO.input(switch)== GPIO.HIGH and Flag==0):
            mylcd.lcd_clear()
            mylcd.lcd_display_string("Right",1)
            
            print("Button was pushed!")
            GPIO.output(LED,GPIO.HIGH)
            Flag=1
            with canvas(virtual) as draw:
                text(draw, (0, 1), '<-', fill="white", font=proportional(CP437_FONT))
            
                
        elif(GPIO.input(switch)== GPIO.HIGH and Flag==1):
            mylcd.lcd_clear()
            mylcd.lcd_display_string("end",2)
            print("LED OFF")
            GPIO.output(LED,GPIO.LOW)
            Flag=0
            with canvas(virtual) as draw:
                text(draw, (0, 1), ' ', fill="white", font=proportional(CP437_FONT))
        sleep(1)

'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
