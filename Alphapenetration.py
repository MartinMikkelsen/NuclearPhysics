import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

#Alpha penetrability, height of Coulomb barrier and Gamow peak.

l=2                             #angular momenta
r0 = 1.4*10**(-15)              #meters
alpha = 1/137                   #fine structure constant
hbar = 1.054571817*10**(-34)    #J/s
c = 3*10**8                     #m/s
E = 8.011*10**(-13)             #Joules
A = 16                          #atomic number
Z1 = 8                          #charge 1
Z2 = 2                          #charge 2
m1 = 2.6560181*10**(-26)        #mass 1 in kilograms
m2 = 6.64648*10**(-27)          #mass 2 in kilograms
mu = m1*m2/(m1+m2)              #reduces mass of the two particles
beta = np.sqrt((2*E)/(mu*c**2)) #velocity in units of the speed of light
eta = Z1*Z2*alpha/beta          #Sommerfeld parameter
k = np.sqrt(2*mu*E)/(hbar)
R = r0*A**(1/3)                 #radius

gamma = 2*np.pi*eta-np.sqrt(32*eta*k*R)
deltagamma = l*(l+1)*np.sqrt(2/(eta*k*R))

Palpha = np.exp(-deltagamma)*np.exp(-gamma)*k*R #the penetrability times the penetration factor

h = (Z1*Z2*alpha*hbar*c)/(R*1.602*10**(-13)) #height of the Coulomb barrier
#print(h)

E0 = 1.220*(Z1**2*Z2**2*mu*(1*10**6)**2)**(1/3)   #position of the Gamow peak
Delta = 0.749*(Z1**2*Z2**2*mu*(1*10**6)**5)**(1/6) #width of the Gamow peak
#print(Delta)
