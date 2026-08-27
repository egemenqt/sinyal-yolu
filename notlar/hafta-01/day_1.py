import numpy as np
import matplotlib.pyplot as plt
freq = 3
time = np.linspace(-1,1,500)
sin_wave = np.sin(2*np.pi*freq*time)
plt.figure(figsize=(12, 4))
plt.plot(time, sin_wave, label='Sine Wave (3 Hz)')
t_point = 1/freq
y_point = np.sin(2*np.pi*freq*t_point)  
period_ends = np.array([1, 2, 3]) / freq  
y_ends = np.sin(2*np.pi*freq*period_ends)  

plt.scatter(period_ends, y_ends, color="green", zorder=5)
plt.text(period_ends[-1], y_ends[-1], "  1 sn'de 3 periyot tamam", color="green")


plt.scatter(t_point, y_point, color="red", zorder=5)
plt.text(t_point, y_point, f"  T(Periol)={t_point:.2f}", color="red") 
plt.title('Basic Signals')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)
plt.show()