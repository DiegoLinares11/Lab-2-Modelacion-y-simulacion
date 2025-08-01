import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1: Simulación de un sistema de retardo de primer orden
dt = 1                # Paso de tiempo (Δt) en días
T = 50                # Tiempo total de simulación (días)
tau = 5               # Retraso en días
entrada1 = 10         # Entrada constante inicial (unidades/día)
entrada2 = 20         # Entrada después del cambio (unidades/día)
t_cambio = 25         # Día en que cambia la entrada


n = int(T/dt) + 1              # Número de pasos de simulación
t = np.arange(0, T+dt, dt)     # Vector de tiempo
stock = np.zeros(n)            # Stock (nivel)
salida = np.zeros(n)           # Salida (flujo)


for i in range(1, n):
    # Entrada cambia en el día 25
    entrada = entrada1 if t[i] < t_cambio else entrada2
    
    # Salida proporcional al stock
    salida[i-1] = stock[i-1] / tau
    
    # Cambio en el stock
    dS = (entrada - salida[i-1]) * dt
    stock[i] = stock[i-1] + dS

# Última salida
salida[-1] = stock[-1] / tau

# Calcular los valores de equilibrio
Seq1 = entrada1 * tau
Seq2 = entrada2 * tau

plt.figure(figsize=(9,5))
plt.plot(t, stock, label="Stock S(t)", linewidth=2)
plt.plot(t, salida, label="Salida(t)", linestyle='--')
plt.axhline(Seq1, color='red', linestyle='--', label=f"Equilibrio inicial = {Seq1}")
plt.axhline(Seq2, color='green', linestyle='--', label=f"Equilibrio nuevo = {Seq2}")
plt.axvline(t_cambio, color='gray', linestyle=':', label="Cambio de entrada")
plt.xlabel("Tiempo (días)")
plt.ylabel("Unidades")
plt.title("Simulación de retardo de primer orden con integración de Euler")
plt.legend()
plt.grid(True)
plt.show()
