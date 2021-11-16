# Solución del Laboratorio 4

# Los parámetros T, t_final y N son elegidos arbitrariamente
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Variables aleatorias C y Z
vaC = stats.norm(5, np.sqrt(0.2))
vaZ = stats.uniform(0, np.pi/2)

# Constante omega para la parte a
w = 2*np.pi*60

# Constante theta para la parte b
theta = 1

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 10
X_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso x(t) (A y Z independientes)
for i in range(N):
	C = vaC.rvs()
	Z = vaZ.rvs()
	x_t = C * np.cos(w*t + Z)
	X_t[i,:] = x_t
	plt.plot(t, x_t)

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(X_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6)

# Graficar el resultado teórico del valor esperado
E = 10/np.pi * (np.cos(w*t) - np.sin(w*t))
plt.plot(t, E, '-.', lw=4)

# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.show()


# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Nueva figura para la autocorrelación
plt.figure()

# Valor teórico de correlación
Rxx = 25.2 * np.cos(w*t + theta)*np.cos(w*(t + taus) + theta)

# Gráficas de correlación para cada realización y la
plt.plot(t, Rxx, lw=4,)
plt.title('Autocorrelación del proceso aleatorio')
plt.xlabel(r'$t$')
plt.ylabel(r'$R_{XX}(t,t + \tau)$')
plt.show()
