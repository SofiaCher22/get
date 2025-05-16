import RPi.GPIO as GPIO
import time


dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def calculate_sleep_time(per):
   
    return per/ (256 * 2)

try:
    period_input = float(input("Введите период треугольного сигнала: "))
    if period_input < 0:
        print("Error: Число < 0")
    else:
        sleep_dur = calculate_sleep_time(period_input)
        print("Формирование треугольного сигнала...")
        while True:
            for value in range(256):
                GPIO.output(dac, dec2bin(value))
                time.sleep(sleep_dur)
            for value in range(254, -1, -1):
                GPIO.output(dac, dec2bin(value))
                time.sleep(sleep_dur)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
