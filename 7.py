import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
comp = 14
troyka = 13
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def dec_bin(N):
    return [int(X) for X in bin(N)[2:].zfill(8)]   


def update_leds(x):
    b = dec_bin(int(x/3.3 * 255))
    GPIO.output(leds, b)


def adc():
    value = 0
    for i in range(7, -1, -1):
        value += 2**i
        GPIO.output(dac, dec_bin(value))
        time.sleep(0.001)
        if GPIO.input(comp) == 1:
            value -= 2**i
    return value

try:
    measured = []
    start = time.time()
    GPIO.output(troyka, 1)
    print('zariadka')

    while True:
        value = adc()
        
        print(value)
        # v = value * 3.3/256
        measured.append(value)
        # update_leds(v)
        if value >= 206:
            break

    GPIO.output(troyka, 0)
    print('rasriadka')

    while True:
        value = adc()
        #v = value * 3.3/256
        print(value)
        measured.append(value)
        #update_leds(v)
        if value <= 77:
            break
    

    final = time.time()
    Time = final - start

    plt.plot(measured)
    plt.grid()
    plt.show()

    with open('data.txt', 'w') as outfile:
        outfile.write('\n'.join(map(str, measured)))    
    
    
    Quant = 3.3/256
    Vd = 1/(Time/len(measured))
    a = [str(Quant), str(Vd)]
    with open('setting.txt', 'w') as outfile1:
        outfile1.write('\n'.join(a))  
    
    
    print('Общая продолжительность эксперимента: ', Time)
    print('Период: ', Time/len(measured))
    print('Частота дискретизации ', Vd)
    print('Шаг квантования ', Quant)

    
     
except KeyboardInterrupt:
            print('Stopped')


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()