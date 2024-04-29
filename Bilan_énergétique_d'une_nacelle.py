# Créé par PEROUX, le 12/01/2021 en Python 3.7
from matplotlib import pyplot as plt
from math import *

m = 3000
g = 9.81
hA = 90
vA = 0
EppA =  m * g * hA


H = []
t = []
vB = []
EcB = []
EppB = []
EmB = []

for h in range(0, 80, 10):
    H.append(h)
    t.append(sqrt(2*h/g))
    vB.append(sqrt(vA**2+2*g*h))
    EcB.append(0.5 * m * (sqrt(vA**2 + 2*g*h))**2)
    EppB.append(EppA-m * g * h)
    EmB.append(0.5 * m * (sqrt(vA**2 + 2*g*h))**2 + EppA-m*g*h)



plt.plot(t, EppB,"bo--", label="EppB")
plt.plot(t, EcB,"ro--", label="EcB")
plt.plot(t, EmB,"go--", label="EmB")
plt.title("Evolution temporelle des énergies de la nacelle")
plt.xlabel("Durée de la chute (en s)")
plt.ylabel("Energies (en J)")
plt.grid()
plt.legend()
plt.show()