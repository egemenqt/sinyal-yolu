import numpy as np
import matplotlib.pyplot as plt

f_signal = 5          # gerçek sinyal frekansı (Hz)
duration = 1.0

# "Sürekli" gerçeği: çok yüksek çözünürlükte örnekle
t_fine = np.linspace(0, duration, 10_000)
signal_fine = np.sin(2 * np.pi * f_signal * t_fine)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

for ax, fs in zip(axes, [20, 6]):   # 20 Hz: yeterli | 6 Hz: Nyquist'in altında
    t = np.arange(0, duration, 1 / fs)
    samples = np.sin(2 * np.pi * f_signal * t)
    ax.plot(t_fine, signal_fine, alpha=0.3, label="gerçek sinyal (5 Hz)")
    ax.stem(t, samples, linefmt="C1-", markerfmt="C1o", basefmt=" ", label=f"örnekler (fs={fs} Hz)")
    ax.plot(t, samples, "C1--", alpha=0.6, label="örneklerden yeniden kurulan görünüm")
    ax.set_title(f"fs = {fs} Hz  (Nyquist limiti: {fs/2} Hz)")
    ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig("aliasing_demo.png", dpi=130)
plt.show()
