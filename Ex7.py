import matplotlib.pyplot as plt
#from typing_extensions import Required
import numpy as np


########################################
#Radioactive decay chain 
########################################
# const declaration
halflife1=9.27/60 #time converted in hour
halflife2=82.73/60 #time converted in hour
lambda1 = np.log(2)/(halflife1)
lambda2 = np.log(2)/(halflife2)
n0=(37e6)/(lambda1/3600)
print(n0,"\n")
t = np.linspace(0,12,12000)
#N decay
n1=n0*np.exp(-lambda1*t)
n2= n0*(lambda1*(np.exp(-lambda1*t)-np.exp(-lambda2*t)))/(lambda2-lambda1)
n3= n0*(lambda1*(1-np.exp(-lambda2*t))-lambda2*(1-np.exp(-lambda1*t)))/(lambda1-lambda2)
plt.plot(t,n1, label="$N$ of $^{139}Cs$")
plt.plot(t,n2, label="$N$ of $^{139}Ba$")
plt.plot(t,n3, label="$N$ of $^{139}La$")
plt.xlabel("t [hours]")
plt.ylabel("N(t)")
plt.grid()
plt.legend()
plt.show()


#####################################
#Activity
#####################################
#1Curie
n0=(37e6)/lambda1 #renormalised for the plot of the activity over the 12 hour 
print(n0)
a_1= lambda1*n0*np.exp(-lambda1*t)
a_2 = lambda2*n0*(lambda1*(np.exp(-lambda1*t)-np.exp(-lambda2*t)))/(lambda2-lambda1)
plt.plot(t,a_1, label="$\mathcal{A}$ of $^{139}Cs$")
plt.plot(t,a_2, label="$\mathcal{A}$ of $^{139}Ba$")
plt.xlabel("t [hours]")
plt.ylabel("Bq")
plt.grid()
plt.legend()
plt.show()
########
#e)
print("max activity: ",np.max(a_2))
print("after ", np.where(a_2 == np.max(a_2)))

#######
#d)
#diff=abs(a_2 - a_1)
# I set 2 because the 2 functions meet themself for the first time before the 2 hours

diff=abs(a_2[:2000] - a_1[:2000])
m=np.min(diff)
print("The 2 activities are equally large: ", m)
print("after ", np.where(diff == m))