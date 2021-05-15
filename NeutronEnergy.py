import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")



A = np.linspace(0.01,200,200)
hbar = 197.326 #MeV fm
r0 = 1.4 #fm
mn = 939.57 #MeV/c^2
U0 = 40 #MeV
R = r0*A**(1/3)

E1= (np.pi**2*hbar**2)/(2*mn*(R)**2)-U0
E2= (np.pi**2*hbar**2*2**2)/(2*mn*(R)**2)-U0
E3= (np.pi**2*hbar**2*3**2)/(2*mn*(R)**2)-U0
E4= (np.pi**2*hbar**2*4**2)/(2*mn*(R)**2)-U0

Einf1= (np.pi**2*hbar**2)/(2*mn*R**2)-U0
Einf2= (np.pi**2*hbar**2*2**2)/(2*mn*R**2)-U0
Einf3= (np.pi**2*hbar**2*3**2)/(2*mn*R**2)-U0
Einf4= (np.pi**2*hbar**2*4**2)/(2*mn*R**2)-U0



As = [5,25,50,75,100,125,150,175,200]
As1 = [25,50,75,100,125,150,175,200]
As2 = [75,100,125,150,175,200]
As3 = [200]

Es = [19.949199999999998,-31.278799999999997, -34.1176,-35.3594,-36.088,-36.5778,-36.934599999999996,-37.208499999999994,-37.4268]
Es1 = [-7.198400000000003, -17.0791,-21.7455,-24.543300000000002,-26.4441, -27.836899999999996, -28.9106,-29.769]
Es2 = [1.4931,-6.4591, -10.266300000000001, -13.165899999999999,-15.4451,-17.288700000000002]
Es3 = [-1.3560999999999985]



g1 = sns.scatterplot(x=As,y=Es,color='maroon')
g2 = sns.scatterplot(x=As1,y=Es1,color='b')
g3 = sns.scatterplot(x=As2,y=Es2,color='orange')
g4 = sns.scatterplot(x=As3,y=Es3, color='k')
plt.legend(['$0s_{1/2}$', '$1s_{1/2}$','$2s_{1/2}$','$3s_{1/2}$'])

sns.lineplot(x=A,y=Einf2,linewidth=2.5, linestyle='--',color='b')
sns.lineplot(x=A,y=Einf3,linewidth=2.5, linestyle='--',color='orange')
sns.lineplot(x=A,y=Einf4,linewidth=2.5, linestyle='--',color='k')
g5=sns.lineplot(x=A,y=Einf1,linewidth=2.5, linestyle='--',color='maroon')

#sns.scatterplot(x=As,y=Es, color='maroon', marker='o',s=50)
plt.ylim([-50,75])


plt.ylabel("E [MeV]")
plt.xlabel("A")
plt.savefig('NeutronEnergy.pdf')
fig = plt.figure()
