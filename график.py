import numpy as np
import matplotlib.pyplot as plt

with open('data.txt', 'r') as f:
    data = np.array([int(line.strip()) for line in f.readlines()])

with open('settings.txt', 'r') as f:
    settings = [float(line.strip()) for line in f.readlines()]
    time_step = settings[0]  
    voltage_step = settings[1]  

voltage = data * voltage_step
time = np.arange(len(data)) * time_step


fig, ax = plt.subplots(figsize=(12, 6))


line, = ax.plot(time, voltage, 
                color='blue', 
                linestyle='-', 
                linewidth=1,
                marker='o',
                markersize=4,
                markeredgecolor='blue',
                markerfacecolor='red',
                markevery=20,
                label='V(t)')

ax.set_xlim([np.min(time), np.max(time)])
ax.set_ylim([np.min(voltage), np.max(voltage) * 1.1])

ax.set_xlabel('t, с', fontsize=12)
ax.set_ylabel('U, В', fontsize=12)

ax.set_title('Процесс зарядки и разрядки конденсатора в RC-цепи', 
             fontsize=14, pad=20, loc='center', wrap=True)


ax.grid(which='major', linestyle='-', linewidth=0.5, color='gray', alpha=0.7)
ax.grid(which='minor', linestyle=':', linewidth=0.5, color='gray', alpha=0.5)
ax.minorticks_on()

max_voltage_idx = np.argmax(voltage)
ch_time = time[max_voltage_idx]
dis_time = time[-1] - time[max_voltage_idx]

text_str = f'Время зарядки = {ch_time:.2f} с,Время разрядки = {dis_time:.2f} с'
ax.text(x=np.max(time)*0.5, y=np.max(voltage)*0.8, 
        s=text_str, 
        fontsize=12, 
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='green'))


ax.legend(fontsize=12)

plt.savefig('rc_plot.svg', format='svg', dpi=300)

plt.show() 