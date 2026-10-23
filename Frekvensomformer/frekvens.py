import numpy as np
import matplotlib.pyplot as plt

frekvens = 10
amplitude = 2
slots = 32
T = 1 / frekvens
T_s = T / slots

t = np.linspace(0, T, 800, endpoint=False)
sinus = amplitude * np.sin(2 * np.pi * frekvens * t)

u = np.zeros_like(t)
forrige = 0.0

for k in range(slots):
    t_midt = k * T_s + T_s / 2
    nivaa = amplitude * np.sin(2 * np.pi * frekvens * t_midt)
    u += np.heaviside(t - k * T_s, 1) * (nivaa - forrige)
    forrige = nivaa

plt.plot(t, sinus, "r", label="Sinus")
plt.plot(t, u, "k", lw=2, label="Trapp")
plt.legend()
plt.show()