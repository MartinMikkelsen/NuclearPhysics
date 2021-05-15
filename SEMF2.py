# semi-empirical mass formula in units of MeV

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="dark")

# SET COEFFICIENTS in MeV
a_1 = 15.2              #Volume term
a_2 = 15.8              #Surface term
a_3 = 0.686             #Coulomb term
a_4 = 44.7/2            #Symmetry term/2
a_5_odd = 0             #Odd pairing term
a_5_even = 5.0          #Even pairing term
a_5_evenOdd = -5.0      #EvenOdd pairing term

#AtomicNumber = int(input("Enter atomic number")) # USER INPUTS A AND Z VALUES
#ProtonNumber = int(input("Enter proton number."))

#A = np.linspace(0,400,400, dtype = int) #This is used for the proton/neutron seperation energy
#Z = 11.0                                #This is used for the proton/neutron seperation energy

def semf(A,Z):# RETURN BINDING ENERGY WITH RELEVENT A5 COEFFICIENT

    b_a5_odd = (a_1*A) - (a_2*A**(2/3)) - (a_3*(Z**2)/(A**(1/3))) - (a_4*((A-2*Z)**2)/A) + (a_5_odd/(A**(1/2)))
    b_a5_even = (a_1*A) - (a_2*A**(2/3)) - (a_3*(Z**2)/(A**(1/3))) - (a_4*((A-2*Z)**2)/A) + (a_5_even/(A**(1/2)))
    b_a5_AevenZodd = (a_1*A) - (a_2*A**(2/3)) - (a_3*(Z**2)/(A**(1/3))) - (a_4*((A-2*Z)**2)/A) + (a_5_evenOdd/(A**(1/2)))

    if A % 2 != 0:
        return b_a5_odd
    elif A % 2 == 0 and Z % 2 == 0:
        return b_a5_even
    elif A % 2 == 0 and Z % 2 != 0:
        return b_a5_AevenZodd

#print("Binding energy: " + str(semf(AtomicNumber,ProtonNumber)) + " MeV")

def bOverA(A,Z):# RETURN BINDING ENERGY PER NUCLEON

    b_a5_odd = (a_1*A) - (a_2*A**(2/3)) - (a_3*(Z**2)/(A**(1/3))) - (a_4*((A-2*Z)**2)/A) + (a_5_odd/(A**(1/2)))
    b_a5_even = (a_1*A) - (a_2*A**(2/3)) - (a_3*(Z**2)/(A**(1/3))) - (a_4*((A-2*Z)**2)/A) + (a_5_even/(A**(1/2)))
    b_a5_AevenZodd = (a_1*A) - (a_2*A**(2/3)) - (a_3*(Z**2)/(A**(1/3))) - (a_4*((A-2*Z)**2)/A) + (a_5_evenOdd/(A**(1/2)))

    if A % 2 != 0 and Z % 2 != 0:
        return (b_a5_odd)/A
    elif A % 2 == 0 and Z % 2 == 0:
        return (b_a5_even)/A
    elif A % 2 == 0 and Z % 2 != 0:
        return (b_a5_AevenZodd)/A

#print("Binding energy per nucleon: " + str(bOverA(AtomicNumber,ProtonNumber)) + "MeV")

#The most stable isobar for a given A corresponds to the minimum mass. This leads to

for A in range(2,400): #NEUTRON SEPERATION ENERGY. When Sn<0 ground state neutron emission will be possible
    Sn  = semf(A,Z)-semf(A-1,Z)

for Z in range(2,400): #PROTON SEPERATION ENERGY
    Sp  = semf(A,Z)-semf(A-1,Z-1)
    #print(Sp)
