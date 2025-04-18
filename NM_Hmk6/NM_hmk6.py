import matplotlib.pyplot as plt
import numpy as np
import math 

n_lst = []
Bn_analytical = []
Bn_Fourier = []
Bn_Finite_Diff = []

def error(Ta_lst, Tn_lst,N):
    summation = 0.0
    i = 0
    N = len(Ta_lst)
    for k in range(N):
        Ta = Ta_lst[k]
        Tn = Tn_lst[k]
        if abs(Ta) < 1e-15:
            continue
        rel_err = (Ta - Tn)/Ta
        summation = summation + (rel_err)**2
        i = i + 1
    if i == 0:
        return 0.0
    return math.sqrt(summation / i)

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

alpha = 0.01
T_0_1_Bna_3_lst = []
T_0_1_BnF_3_lst = []
T_0_1_Bna_5_lst = []
T_0_1_BnF_5_lst = []

T_1_Bna_3_lst = []
T_1_BnF_3_lst = []
T_1_Bna_5_lst = []
T_1_BnF_5_lst = []

T_10_Bna_3_lst = []
T_10_BnF_3_lst = []
T_10_Bna_5_lst = []
T_10_BnF_5_lst = []

x_lst = []

t = 0.1
for x in np.arange(0,1.05,0.05):
    x_lst.append(x)
    T_0_1_Bna_3 = 0
    T_0_1_BnF_3 = 0
    for n in np.arange(1,4,1):
        T_0_1_Bna_3 = T_0_1_Bna_3 + ((1600/((n*math.pi)**3))*(1-math.cos(n*math.pi)))*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        T_0_1_BnF_3 = T_0_1_BnF_3 + (Bn_Fourier[n-1])*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        
    T_0_1_Bna_3_lst.append(T_0_1_Bna_3)
    T_0_1_BnF_3_lst.append(T_0_1_BnF_3)

    T_0_1_Bna_5 = 0
    T_0_1_BnF_5 = 0    
    
    for n in np.arange(1,6,1):
        T_0_1_Bna_5 = T_0_1_Bna_5 + ((1600/((n*math.pi)**3))*(1-math.cos(n*math.pi)))*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        T_0_1_BnF_5 = T_0_1_BnF_5 + (Bn_Fourier[n-1])*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        
    T_0_1_Bna_5_lst.append(T_0_1_Bna_5)
    T_0_1_BnF_5_lst.append(T_0_1_BnF_5)
    
t = 1
for x in np.arange(0,1.05,0.05):
    T_1_Bna_3 = 0
    T_1_BnF_3 = 0
    for n in np.arange(1,4,1):
        T_1_Bna_3 = T_1_Bna_3 + ((1600/((n*math.pi)**3))*(1-math.cos(n*math.pi)))*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        T_1_BnF_3 = T_1_BnF_3 + (Bn_Fourier[n-1])*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        
    T_1_Bna_3_lst.append(T_1_Bna_3)
    T_1_BnF_3_lst.append(T_1_BnF_3)

    T_1_Bna_5 = 0
    T_1_BnF_5 = 0    
    
    for n in np.arange(1,6,1):
        T_1_Bna_5 = T_1_Bna_5 + ((1600/((n*math.pi)**3))*(1-math.cos(n*math.pi)))*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        T_1_BnF_5 = T_1_BnF_5 + (Bn_Fourier[n-1])*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        
    T_1_Bna_5_lst.append(T_1_Bna_5)
    T_1_BnF_5_lst.append(T_1_BnF_5)

t = 10
for x in np.arange(0,1.05,0.05):
    T_10_Bna_3 = 0
    T_10_BnF_3 = 0
    for n in np.arange(1,4,1):
        T_10_Bna_3 = T_10_Bna_3 + ((1600/((n*math.pi)**3))*(1-math.cos(n*math.pi)))*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        T_10_BnF_3 = T_10_BnF_3 + (Bn_Fourier[n-1])*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        
    T_10_Bna_3_lst.append(T_10_Bna_3)
    T_10_BnF_3_lst.append(T_10_BnF_3)

    T_10_Bna_5 = 0
    T_10_BnF_5 = 0    
    
    for n in np.arange(1,6,1):
        T_10_Bna_5 = T_10_Bna_5 + ((1600/((n*math.pi)**3))*(1-math.cos(n*math.pi)))*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        T_10_BnF_5 = T_10_BnF_5 + (Bn_Fourier[n-1])*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
        
    T_10_Bna_5_lst.append(T_10_Bna_5)
    T_10_BnF_5_lst.append(T_10_BnF_5)

print("Errors")
print("t=0.1 n=3")
print(error(Ta_lst=T_0_1_Bna_3_lst,Tn_lst=T_0_1_BnF_3_lst,N=len(T_0_1_Bna_3_lst)))
print("t=0.1 n=5")
print(error(Ta_lst=T_0_1_Bna_5_lst,Tn_lst=T_0_1_BnF_5_lst,N=len(T_0_1_Bna_5_lst)))
print("t=1 n=3")
print(error(Ta_lst=T_1_Bna_3_lst,Tn_lst=T_1_BnF_3_lst,N=len(T_1_Bna_3_lst)))
print("t=1 n=5")
print(error(Ta_lst=T_1_Bna_5_lst,Tn_lst=T_1_BnF_5_lst,N=len(T_1_Bna_5_lst)))
print("t=10 n=3")
print(error(Ta_lst=T_10_Bna_3_lst,Tn_lst=T_10_BnF_3_lst,N=len(T_10_Bna_3_lst)))
print("t=10 n=5")
print(error(Ta_lst=T_10_Bna_5_lst,Tn_lst=T_10_BnF_5_lst,N=len(T_10_Bna_5_lst)))

plt.plot(x_lst, T_0_1_Bna_3_lst, linestyle="-",  linewidth=1, alpha=0.9, label="t=0.1 Analytical 3")
plt.plot(x_lst, T_0_1_BnF_3_lst, linestyle="--", linewidth=1, alpha=0.9, label="t=0.1 Fourier 3")

plt.plot(x_lst, T_0_1_Bna_5_lst, linestyle="-",  linewidth=1, alpha=0.9, label="t=0.1 Analytical 5")
plt.plot(x_lst, T_0_1_BnF_5_lst, linestyle="--", linewidth=1, alpha=0.9, label="t=0.1 Fourier 5")

plt.plot(x_lst, T_1_Bna_3_lst,  linestyle="-",  linewidth=1, alpha=0.9, label="t=1 Analytical 3")
plt.plot(x_lst, T_1_BnF_3_lst,  linestyle="--", linewidth=1, alpha=0.9, label="t=1 Fourier 3")

plt.plot(x_lst, T_1_Bna_5_lst,  linestyle="-",  linewidth=1, alpha=0.9, label="t=1 Analytical 5")
plt.plot(x_lst, T_1_BnF_5_lst,  linestyle="--", linewidth=1, alpha=0.9, label="t=1 Fourier 5")

plt.plot(x_lst, T_10_Bna_3_lst, linestyle="-",  linewidth=1, alpha=0.9, label="t=10 Analytical 3")
plt.plot(x_lst, T_10_BnF_3_lst, linestyle="--", linewidth=1, alpha=0.9, label="t=10 Fourier 3")

plt.plot(x_lst, T_10_Bna_5_lst, linestyle="-",  linewidth=1, alpha=0.9, label="t=10 Analytical 5")
plt.plot(x_lst, T_10_BnF_5_lst, linestyle="--", linewidth=1, alpha=0.9, label="t=10 Fourier 5")
plt.xlabel("Length")
plt.ylabel("Temperature")
plt.legend()
plt.title("Analytical and Fourier Length vs Temp t=0.1,1,10 Bn = 3 and 5")
plt.show()