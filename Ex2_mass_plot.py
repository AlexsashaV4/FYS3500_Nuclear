
import matplotlib.pyplot as plt
#from typing_extensions import Required
import numpy as np
#######################
#Variables initialisation
#######################
z=np.linspace(10,100,1000)
a=136
a_v=15.8
a_s=18.3
a_c=0.714
a_sym=23.4
a_p=12
m_p=938.28
m_n=939.28
m_e=0.51
def mass(A,Z):
    if A%2==0:
        m=Z*(m_p+m_e) +(A-Z)*m_n 
        b=( a_v*A - a_s*pow(A,2/3) - a_c*(Z*(Z-1))/pow(A,1/3) - a_sym*(pow((2*Z-A),2))/A + a_p*(pow(A,-1/2)))
        return m-b
    else:
        return Z*(m_p+m_e) +(A-Z)*m_n -(a_v*A - a_s*pow(A,2/3) - a_c*(Z*(Z-1))/pow(A,1/3) - a_sym*(pow((2*Z-A),2))/A)
def massodd(A,Z):
        m=Z*(m_p+m_e) +(A-Z)*m_n
        b=(a_v*A - a_s*pow(A,2/3) - a_c*(Z*(Z-1))/pow(A,1/3) - a_sym*(pow((2*Z-A),2))/A - a_p*(pow(A,-1/2)))
        return  m-b

Z_min= (m_n-m_p-m_e + a_c*pow(a,-1/3)+4*a_sym)/(2*a_c*pow(a,-1/3) + 8*a_sym*pow(a,-1))
print("The minimum Z is: " ,Z_min)

plt.plot(z,mass(135,z)*0.001,label='A=135', color="orange" )
plt.plot(z,massodd(136,z)*0.001,label='A=136 odd-odd', color= "green"  )
plt.plot(z,mass(136,z)*0.001,label='A=136 even-even' )
plt.legend()
plt.xlabel("Z")
plt.xticks()
plt.ylabel("Mev")
plt.grid()
plt.show()
