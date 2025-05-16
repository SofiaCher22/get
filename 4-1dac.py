import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6 ]
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def voltage(value):
    return (value/255.0)*3.3


try:
    while True:
        a=input()
        if a=='q':
            break
        
            


        
        a=int(a)
        

    
        if a<0 or a>256:
            print('Число не лежащее в диапазоне от 0 до 256')
            continue



        binary=decimal2binary(a)
        GPIO.output(dac, binary)
        v=voltage(a)
        print('Напряжение', v)

        
except ValueError:
            
    try:
        a=float(a)
        print('ВВедите целое число')
    except ValueError:
        print('не число')
        

        



finally:


    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
