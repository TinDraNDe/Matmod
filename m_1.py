import matplotlib.pyplot as plt
import numpy as np 
import math

#----- VÅRA PARAMETRAR ----- #
e = 20
a0 = 4
k = 0.01
#------KONCENTRATIONER-------# 

a = lambda t: a0 * math.e**(-k * e * t)
b = lambda t: a0 - a0 * math.e**(-k * e * t) 

x = np.linspace(0,5,100)

#plt.title('Koncentrationer)
#plt.plot(b(x))
#plt.plot(a(x))
#plt.legend(['[B]','[A]'])

#plt.show()

#---------DERIVATOR----------#

dadt = lambda t: -k  * e * a(t) 
dbdt = lambda t: k * e * a(t) 

plt.title('Derivator')
plt.plot(dadt(x))
plt.plot(dbdt(x))
plt.legend(['d[B]/dt','d[A]/dt'])
plt.show()

