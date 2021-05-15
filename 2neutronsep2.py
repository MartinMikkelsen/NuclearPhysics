import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")
sns.set_context("paper")

V = 0.3 #MeV
Emærke = np.linspace(-2,2,100)
E_1 = 0.
E_2 = Emærke #MeV

Eminus = 0.5*(E_1+E_2 - np.sqrt((E_1+E_2)**2-4*E_1*E_2+4*V**2))
Eplus = 1/2*(E_1+E_2 + np.sqrt((E_1+E_2)**2-4*E_1*E_2+4*V**2))


sns.lineplot(x=Emærke, y=Eminus, color='maroon', legend='brief',label='$E_-$')
sns.lineplot(x=Emærke, y=Eplus, color='b', legend='brief',label='$E_+$')

sns.lineplot(x=Emærke, y=0, linestyle='--', color='k')
plt.ylabel("Energy [MeV]")
plt.xlabel("$E'$ [MeV]")
#plt.savefig('Twolevelmixing.pdf')
plt.figure()



#probc1 = 1/(1+(Eminus-E_1)**2/(V**2))
#probc2 = 1/(1+(Eminus-E_2)**2/(V**2))

#sns.lineplot(x=Emærke, y=probc1, color='maroon',legend='brief',label='$c_{1,-}^2$')
#sns.lineplot(x=Emærke, y=probc2, color='b',legend='brief',label='$c_{2,-}^2$')
#sns.lineplot(x=Emærke, y=probc1+probc2, linestyle='--', color='k', legend='brief',label='$c_{1,-}^2+ c_{2,-}^2$')
#plt.ylabel("P ")
#plt.xlabel("$E'$ [MeV]")
#plt.savefig('Probability.pdf')
#plt.figure()
