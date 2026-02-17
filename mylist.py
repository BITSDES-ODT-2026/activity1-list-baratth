from machine import Pin, PWM
import time

l1 = Pin(18, Pin.OUT)
l2 = Pin(19, Pin.OUT)
l3 = Pin(33, Pin.OUT)
l4 = Pin(32, Pin.OUT)

my_leeest = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

for i in my_leeest:
    l1.value(i[0])
    l2.value(i[1])
    l3.value(i[2])
    l4.value(i[3])
    time.sleep(0.2)
