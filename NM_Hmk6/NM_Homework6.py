import matplotlib.pyplot as plt
import numpy as np
import math 

n_lst = []
Bn_analytical = []
Bn_Fourier = []
Bn_Finite_Diff = []

error = []

for n in np.arange(1,11,1):
    n_lst.append(n)
    Bn_a = (1600/((n*math.pi)**3))*(1-math.cos(n*math.pi))
    Bn_analytical.append(Bn_a)
    Bn_F = 0
    delta_x = 0.05
    for xi in np.arange(0,1,0.05):
        Bn_F = Bn_F + 100*(1-4*((xi-0.5)**2))*math.sin(n*math.pi*xi)*delta_x 
    Bn_F = Bn_F*2
    Bn_Fourier.append(Bn_F)
    print(Bn_F)

err_lst = []
k_lst = []
for k in np.arange(1,len(Bn_Fourier)):
    error = Bn_analytical[k-1] - Bn_Fourier[k-1]
    err_lst.append(error)
    k_lst.append(k)



plt.plot(n_lst,Bn_Fourier, linewidth=5, label="Bn Fourier")
plt.plot(n_lst,Bn_analytical, linestyle="--", label="Bn Analytical")

#plt.plot(k_lst,err_lst)
#plt.title("Bn Analytical - Bn Fourier")
plt.xlabel("n value")
#plt.ylabel("Difference in Bn")
plt.ylabel("Bn value")
plt.title("Bn Analytical and Fourier")
plt.legend()
plt.show()
