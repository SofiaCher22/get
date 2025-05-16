import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

pwm = GPIO.PWM(24, 1000)
pwm.start(0)  


try:
    while True:
       
        duty_cycle = float(input("Введите коэффициент заполнения (0 - 100%): "))

        
        
        pwm.ChangeDutyCycle(duty_cycle)


        voltage = 3.3 * duty_cycle / 100
        print(f'Напряжение на R-C цепи: {voltage:.2f} В')



finally:
    pwm.stop()  
    GPIO.cleanup()
