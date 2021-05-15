# semi-empirical mass formula in units of MeV

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="dark")


# SET COEFFICIENTS
a_1 = 15.8
a_2 = 18.3
a_3 = 0.714
a_4 = 23.2
a_5_odd = 0
a_5_even = 12.0
a_5_evenOdd = -12.0

massNum = int(input("Enter atomic number")) # USER INPUTS A AND Z VALUES
atNum = int(input("Enter proton number."))


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

print("Binding energy: " + str(semf(massNum,atNum)) + " MeV")

def bOverA(A,Z):# RETURN B/A

    b_a5_odd = (a_1*A) - (a_2*A**(2/3)) - (a_3*(Z**2)/(A**(1/3))) - (a_4*((A-2*Z)**2)/A) + (a_5_odd/(A**(1/2)))
    b_a5_even = (a_1*A) - (a_2*A**(2/3)) - (a_3*(Z**2)/(A**(1/3))) - (a_4*((A-2*Z)**2)/A) + (a_5_even/(A**(1/2)))
    b_a5_AevenZodd = (a_1*A) - (a_2*A**(2/3)) - (a_3*(Z**2)/(A**(1/3))) - (a_4*((A-2*Z)**2)/A) + (a_5_evenOdd/(A**(1/2)))

    if A % 2 != 0 and Z % 2 != 0:
        return (b_a5_odd)/A
    elif A % 2 == 0 and Z % 2 == 0:
        return (b_a5_even)/A
    elif A % 2 == 0 and Z % 2 != 0:
        return (b_a5_AevenZodd)/A

print("Binding energy per nucleon: " + str(bOverA(massNum,atNum)) + "MeV")

# Make a function to find most stable isotope of Z using A=Z,2Z,3Z

def semf_zMultiples(Z): # Loop through A = Z,2Z,3Z and print most stable
    energyList = []
    for n in range(1,4):
        b_a5_odd = (a_1*(n*Z)) - (a_2*(n*Z)**(2/3)) - (a_3*(Z**2)/((n*Z)**(1/3))) - (a_4*(((n*Z)-2*Z)**2)/(n*Z)) + (a_5_odd/((n*Z)**(1/2)))
        b_a5_even = (a_1*(n*Z)) - (a_2*(n*Z)**(2/3)) - (a_3*(Z**2)/((n*Z)**(1/3))) - (a_4*(((n*Z)-2*Z)**2)/(n*Z)) + (a_5_even/((n*Z)**(1/2)))
        b_a5_AevenZodd = (a_1*(n*Z)) - (a_2*(n*Z)**(2/3)) - (a_3*(Z**2)/((n*Z)**(1/3))) - (a_4*(((n*Z)-2*Z)**2)/(n*Z)) + (a_5_evenOdd/((n*Z)**(1/2)))

        if (n*Z) % 2 != 0:
            energyList.append(((b_a5_odd)/(n*Z),n))
        elif (n*Z) % 2 == 0 and Z % 2 == 0:
            energyList.append(((b_a5_even)/(n*Z),n))
        elif (n*Z) % 2 == 0 and Z % 2 != 0:
            energyList.append(((b_a5_AevenZodd)/(n*Z),n))
    return energyList

print("\nMost stable isotope (from A = Z,2Z,3Z) has B/A = " + str((max(semf_zMultiples(atNum)))[0]) + " MeV & A = " + str((max(semf_zMultiples(atNum)))[1]) +"Z")

# Loop through Z = 1 to Z = 100 to find highest B/A

def semf_zMultiplesMax(Z): # Same as previous but returns max value tuple in function.
    energyList = []
    for n in range(1,4):
        b_a5_odd = (a_1*(n*Z)) - (a_2*(n*Z)**(2/3)) - (a_3*(Z**2)/((n*Z)**(1/3))) - (a_4*(((n*Z)-2*Z)**2)/(n*Z)) + (a_5_odd/((n*Z)**(1/2)))
        b_a5_even = (a_1*(n*Z)) - (a_2*(n*Z)**(2/3)) - (a_3*(Z**2)/((n*Z)**(1/3))) - (a_4*(((n*Z)-2*Z)**2)/(n*Z)) + (a_5_even/((n*Z)**(1/2)))
        b_a5_AevenZodd = (a_1*(n*Z)) - (a_2*(n*Z)**(2/3)) - (a_3*(Z**2)/((n*Z)**(1/3))) - (a_4*(((n*Z)-2*Z)**2)/(n*Z)) + (a_5_evenOdd/((n*Z)**(1/2)))

        if (n*Z) % 2 != 0:
            energyList.append(((b_a5_odd)/(n*Z),n,Z))
        elif (n*Z) % 2 == 0 and Z % 2 == 0:
            energyList.append(((b_a5_even)/(n*Z),n,Z))
        elif (n*Z) % 2 == 0 and Z % 2 != 0:
            energyList.append(((b_a5_AevenZodd/(n*Z)),n,Z))
    return max(energyList)

mostStableIsotopes = []

for i in range(1,101): #
    mostStableIsotopes.append(semf_zMultiplesMax(i))

print("\nWhen looping from Z = 1 to Z = 100 and using the above method for A, this SEMF calculator shows the most stable Z to be " + str(max(mostStableIsotopes)[2]) + " with a B/A of " +  str(max(mostStableIsotopes)[0]) + " MeV. In reality, the most stable is Z = 28.")

# plot graph of B/A vs Z using mostStableIsotopes


isotopeArray = np.array(mostStableIsotopes) # convert to array to use as x and y data

#sns.set()
plt.plot((isotopeArray[:,1])*(isotopeArray[:,2]),isotopeArray[:,0],color='b',linewidth=1.0)
plt.scatter(10, 6.2271106453568965, marker='o', label='(10,4)Be')
plt.scatter(50, 8.599690995547174, marker='o', label='(50,23)V')
plt.scatter(100, 8.05691130342879, marker='o', label='(100,36)Kr')
plt.scatter(150, 7.767223034783923, marker='o', label='(150,71)Lu')
plt.scatter(200, 7.653838942173183, marker='o', label='(200,87)Fr')
plt.xlabel('Nucleon Number A')
plt.ylabel('Binding Energy per Nucleon (MeV)')
plt.legend(loc='lower right')
plt.title('B/A vs. A')
plt.savefig('binding_energy1.pdf')
plt.show()
