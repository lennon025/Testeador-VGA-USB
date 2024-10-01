# Leno Perdomo Cespedes
from machine import Pin, I2C, ADC
import machine, ssd1306, utime

señal = machine.PWM(Pin(28))
señal.freq(1000)
señal.duty_u16(500000)
boton=Pin(12, Pin.IN)
count=0

gp0 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp1 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp2 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp3 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp4 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp5 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp6 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp7 = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp8 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp9 = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp10 = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp11 = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp12 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
gp13 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)



i2c = machine.I2C(0, scl=machine.Pin(21), sda=machine.Pin(20))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.text('Monitor tester', 10, 0)
oled.show()
oled.fill(0)
utime.sleep(2)
oled.text('VGA-USB', 30, 0)
oled.show()
utime.sleep(2)
oled.fill(0)
oled.show()

    
       

while True:
    if gp1.value()==1:
        print("1")
####################################### VGA ####################################    
    if boton.value() ==0:
        oled.fill(0)
        oled.text('VGA', 0, 5)
        oled.text('1', 30, 0)
        oled.text('2', 30, 8)
        oled.text('3', 45, 0)
        oled.text('4', 45, 8)
        oled.text('5', 60, 0)
        oled.text('6', 60, 8)
        oled.text('7', 75, 0)
        oled.text('8', 75, 8)
        oled.text('9', 90, 0)
        oled.text('10', 90, 8)
        oled.text('12', 110, 8)
        oled.text('X', 110, 0)
        oled.text('VGA',0, 40)
        
        #oled.text('1', 30, 30)
        oled.text('-', 30, 40)
        oled.text('|', 36, 30)
        oled.text('|', 36, 40)
        oled.text('|', 36, 50)
        #oled.text('2', 30, 50)
        
        #oled.text('3', 45, 30)
        oled.text('-', 45, 40)
        oled.text('|', 52, 30)
        oled.text('|', 52, 40)
        oled.text('|', 52, 50)
        #oled.text('4', 45, 50)
        
        #oled.text('5', 60, 30)
        oled.text('-', 60, 40)
        oled.text('|', 68, 30)
        oled.text('|', 68, 40)
        oled.text('|', 68, 50)      
        #oled.text('6', 60, 50)
        
        #oled.text('7', 75, 30)
        oled.text('-', 75, 40)
        oled.text('|', 82, 30)
        oled.text('|', 82, 40)
        oled.text('|', 82, 50)
        #oled.text('8', 75, 50)
        
        #oled.text('9', 90, 30)
        oled.text('-', 90, 40)
        oled.text('-', 100, 40)
        oled.text('|', 105, 30)
        oled.text('|', 105, 40)
        oled.text('|', 105, 50)
        #oled.text('10', 90, 50)
        
        #oled.text('X', 112, 30)
        oled.text('-', 110, 40)
        oled.text('-', 114, 40)
        oled.text('X', 112, 30)
        #oled.text('12', 112, 50)
        oled.show()
        
        if gp1.value()==1:
            oled.text('1', 30, 30)
            oled.show()
            utime.sleep_ms(50)
        if gp2.value()==1:
            oled.text('2', 30, 50)
            oled.show()
            utime.sleep_ms(50)
        if gp3.value()==1:
            oled.text('3', 45, 30)
            oled.show()
            utime.sleep_ms(50)
        if gp4.value()==1:
            oled.text('4', 45, 50)
            oled.show()
            utime.sleep_ms(50)
        if gp5.value()==1:
            oled.text('5', 60, 30)
            oled.show()
            utime.sleep_ms(50)
        if gp6.value()==1:
            oled.text('6', 60, 50)
            oled.show()
            utime.sleep_ms(50)
        if gp7.value()==1:
            oled.text('7', 75, 30)
            oled.show()
            utime.sleep_ms(50)
        if gp8.value()==1:
            oled.text('8', 75, 50)
            oled.show()
            utime.sleep_ms(50)
        if gp9.value()==1:
            oled.text('9', 90, 30)
            oled.show()
            utime.sleep_ms(50)
        if gp10.value()==1:
            oled.text('10', 90, 50)
            oled.show()
            utime.sleep_ms(50)
        if gp11.value()==1:
            oled.text('12', 112, 50)
            oled.show()
            utime.sleep_ms(50)
            
   ################################################## USB ###############################
    if boton.value() ==1:
        oled.fill(0)
        oled.text('USB', 0, 5)
        oled.text('1', 30, 0)
        oled.text('2', 30, 8)
        oled.text('3', 50, 0)
        oled.text('4', 50, 8)
        oled.text('5', 70, 0)
        oled.text('6', 70, 8)
        oled.text('7', 90, 0)
        oled.text('8', 90, 8)
        oled.text('X', 110, 0)
        oled.text('X', 110, 8)
        oled.text('USB', 0, 40)
        
        # oled.text('1', 30, 30)
        oled.text('-', 30, 40)
        oled.text('|', 40, 30)
        oled.text('|', 40, 40)
        oled.text('|', 40, 50)
        # oled.text('2', 30, 50)
        
       # oled.text('3', 50, 30)
        oled.text('-', 50, 40)
        oled.text('|', 60, 30)
        oled.text('|', 60, 40)
        oled.text('|', 60, 50)
       # oled.text('4', 50, 50)
        
       # oled.text('5', 70, 30)
        oled.text('-', 70, 40)
        oled.text('|', 80, 30)
        oled.text('|', 80, 40)
        oled.text('|', 80, 50)      
       # oled.text('6', 70, 50)
                
       # oled.text('7', 90, 30)
        oled.text('-', 90, 40)
        oled.text('|', 100, 30)
        oled.text('|', 100, 40)
        oled.text('|', 100, 50)
       # oled.text('8', 90, 50)

        
       # oled.text('X', 110, 30)
        oled.text('-', 110, 40)        
       # oled.text('X', 110, 50)
        oled.show()
        
        if gp1.value()==1:
            oled.text('1', 30, 30)
            oled.show()
            utime.sleep_ms(50)
        if gp2.value()==1:
            oled.text('2', 30, 50)
            oled.show()
            utime.sleep_ms(50)
        if gp3.value()==1:
            oled.text('3', 50, 30)
            oled.show()
            utime.sleep_ms(50)
        if gp4.value()==1:
            oled.text('4', 50, 50)
            oled.show()
            utime.sleep_ms(50)
        if gp5.value()==1:
            oled.text('5', 70, 30)
            oled.show()
            utime.sleep_ms(50)
        if gp6.value()==1:
            oled.text('6', 70, 50)
            oled.show()
            utime.sleep_ms(50)
        if gp7.value()==1:
            oled.text('7', 90, 30)
            oled.show()
            utime.sleep_ms(50)
        if gp8.value()==1:
            oled.text('8', 90, 50)
            oled.show()
            utime.sleep_ms(50)

    utime.sleep(2)
