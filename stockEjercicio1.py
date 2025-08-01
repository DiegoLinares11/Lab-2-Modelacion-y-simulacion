import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
S0 = 100      # Stock inicial
Se = 50       # Stock en equilibrio
tau = 10      # Tiempo de retardo
t = np.linspace(0, 50, 200)  # Tiempo de 0 a 50 días

# Ecuación analítica del retardo de primer orden
S = Se + (S0 - Se) * np.exp(-t/tau)

# Graficar
plt.figure(figsize=(8,5))
plt.plot(t, S, label="Stock S(t)")
plt.axhline(Se, color='red', linestyle='--', label="Equilibrio (S_eq=50)")
plt.xlabel("Tiempo (días)")
plt.ylabel("Stock")
plt.title("Ajuste exponencial del stock con retardo de primer orden")
plt.legend()
plt.grid(True)
plt.show()
