
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac_gpios = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setup(dac_gpios, GPIO.OUT)

def dec2bin(num):
    return [int(bin) for bin in bin(num)[2:].zfill(8)]


try:
    while True:
        for num in list(range(256)) + list(range(255, -1, -1)):
            GPIO.output(dac_gpios[::-1], dec2bin(num))
            time.sleep(0.001)
finally:
    GPIO.output(dac_gpios, 0)
    GPIO.cleanup()

> Соня:
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
a = GPIO.PWM(23, 10000)

a.start(0)

try:
    while True:
        Duty_cycle = (input("Insert the duty cycle "))
        if Duty_cycle == 'q':
            break
        a.start(int(Duty_cycle))
finally:
    GPIO.cleanup()

> Соня:
2,3 цап

> Соня:
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyk = 13
led = [2, 3, 4, 17, 27, 22, 10, 9][::-1]


GPIO.setup(dac, GPIO.OUT, initial = 0)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyk, GPIO.OUT, initial=1)
GPIO.setup(led, GPIO.OUT)


def dec2bin(num):
    return [int(bn) for bn in bin(num)[2:].zfill(8)]


def adc():
    volumes = [0, 1, 3, 7, 15, 31, 63, 127, 255]
    rg = [i * 32 for i in range(9)]
    result = 0
    check = [0 for i in range(8)]  
    for i in range(8):
        check[i] = 1
        GPIO.output(dac, check)
        time.sleep(0.02)
        if GPIO.input(comp) == 0:
            result += 2**(7-i)
        else:
            check[i] = 0

    volumes_rg = [abs(i - result) for i in rg]
    print(result*(3.3/256), result)
    
    return volumes[volumes_rg.index(min(volumes_rg))]


try:
    while True:
        GPIO.output(led, dec2bin(adc()))
                  

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyk, 0)
    GPIO.cleanup()
