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
        rel_err = (Ta - Tn)**2/(Ta**2+1e-8)
        summation = summation + rel_err
        i = i + 1
    if i == 0:
        return 0.0
    return math.sqrt(summation / i)

for n in np.arange(1,500,1):
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

T_01_Analytical = []
T_1_Analytical = []
T_10_Analytical = []

x_lst = []

t = 0.1
for x in np.arange(0,1.05,0.05):
    x_lst.append(x)
    T_0_1_Bna_3 = 0
    T_0_1_BnF_3 = 0
    T_01_A = 0
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

    for n in np.arange(1,500,1):
        T_01_A = T_01_A + ((1600/((n*math.pi)**3))*(1-math.cos(n*math.pi)))*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
    T_01_Analytical.append(T_01_A)

    
t = 1
for x in np.arange(0,1.05,0.05):
    T_1_Bna_3 = 0
    T_1_BnF_3 = 0
    T_1_A = 0
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

    for n in np.arange(1,500,1):
        T_1_A = T_1_A + ((1600/((n*math.pi)**3))*(1-math.cos(n*math.pi)))*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
    T_1_Analytical.append(T_1_A)

t = 10
for x in np.arange(0,1.05,0.05):
    T_10_Bna_3 = 0
    T_10_BnF_3 = 0
    T_10_A = 0
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

    for n in np.arange(1,500,1):
        T_10_A = T_10_A + ((1600/((n*math.pi)**3))*(1-math.cos(n*math.pi)))*(math.sin(n*math.pi*x))*math.exp((-(n*math.pi)**2)*t*alpha)
    T_10_Analytical.append(T_10_A)

###############################

delta_x = 0.05
delta_t = 0.025

Start_Temp_lst = []

def Temp (T_p1,T1,T_m1):
    T_next = (0.1*(T_m1+T_p1)) + (0.8*T1)
    return T_next

def start_condition (x):
    T_x = 100*(1-(4*((x-0.5)**2)))
    return T_x

L=20

x_lst = []
for i in np.arange(0,21):
    x = i*delta_x
    x_lst.append(x)
    Start_Temp_lst.append(start_condition(x))

Temp_new_01 = Start_Temp_lst
Temp_new_1 = Start_Temp_lst
Temp_new_10 = Start_Temp_lst

for j in np.arange(1,(0.1/delta_t)+1.0):
    Temp_lst = []
    for i in np.arange(0,(1.0/delta_x)+1.0):
        if i == 0:
            Temp_lst.append(0)
        elif (i != 0 and i != L):
            Temp_lst.append(Temp(T_p1=Temp_new_01[int(i+1)],T1=Temp_new_01[int(i)],T_m1=Temp_new_01[int(i-1)]))
        elif int(i) == L:
            Temp_lst.append(0)
    Temp_new_01 = Temp_lst

for j in np.arange(1.0,(1.0/delta_t)+1):
    Temp_lst = []
    for i in np.arange(0.0,(1.0/delta_x)+1):
        if i == 0:
            Temp_lst.append(0)
        elif (i != 0 and i != L):
            Temp_lst.append(Temp(T_p1=Temp_new_1[int(i+1)],T1=Temp_new_1[int(i)],T_m1=Temp_new_1[int(i-1)]))
        elif int(i) == L:
            Temp_lst.append(0)
    Temp_new_1 = Temp_lst

for j in np.arange(1,(10.0/delta_t)+1):
    Temp_lst = []
    for i in np.arange(0,(1.0/delta_x)+1):
        if i == 0:
            Temp_lst.append(0)
        elif (i != 0 and i != L):
            Temp_lst.append(Temp(T_p1=Temp_new_10[int(i+1)],T1=Temp_new_10[int(i)],T_m1=Temp_new_10[int(i-1)]))
        elif int(i) == L:
            Temp_lst.append(0)
    Temp_new_10 = Temp_lst

###############################


print("Errors")
print("t=0.1 n=3")
print(error(Ta_lst=T_01_Analytical,Tn_lst=T_0_1_BnF_3_lst,N=len(T_0_1_Bna_3_lst)))
print("t=0.1 n=5")
print(error(Ta_lst=T_01_Analytical,Tn_lst=T_0_1_BnF_5_lst,N=len(T_0_1_Bna_5_lst)))
print("t=0.1 Finite Diff")
print(error(Ta_lst=T_01_Analytical,Tn_lst=Temp_new_01,N=len(T_0_1_Bna_5_lst)))
print("t=1 n=3")
print(error(Ta_lst=T_1_Analytical,Tn_lst=T_1_BnF_3_lst,N=len(T_1_Bna_3_lst)))
print("t=1 n=5")
print(error(Ta_lst=T_1_Analytical,Tn_lst=T_1_BnF_5_lst,N=len(T_1_Bna_5_lst)))
print("t=1 Finite Diff")
print(error(Ta_lst=T_1_Analytical,Tn_lst=Temp_new_1,N=len(T_1_Bna_5_lst)))
print("t=10 n=3")
print(error(Ta_lst=T_10_Analytical,Tn_lst=T_10_BnF_3_lst,N=len(T_10_Bna_3_lst)))
print("t=10 n=5")
print(error(Ta_lst=T_10_Analytical,Tn_lst=T_10_BnF_5_lst,N=len(T_10_Bna_5_lst)))
print("t=10 Finite Diff")
print(error(Ta_lst=T_10_Analytical,Tn_lst=Temp_new_10,N=len(T_10_Bna_5_lst)))

print(T_10_Analytical)
print(len(T_10_Analytical))
print(Temp_new_10)
print(len(Temp_new_10))


plt.plot(x_lst, T_01_Analytical, linestyle="-",  linewidth=1, alpha=0.9,label="t=0.1 Analytical")
#plt.plot(x_lst, T_0_1_Bna_3_lst, linestyle="-",  linewidth=1, alpha=0.9, label="t=0.1 Analytical 3")
plt.plot(x_lst, T_0_1_BnF_3_lst, linestyle="--", linewidth=1, alpha=0.9, label="t=0.1 Fourier 3")

#plt.plot(x_lst, T_0_1_Bna_5_lst, linestyle="-",  linewidth=1, alpha=0.9, label="t=0.1 Analytical 5")
plt.plot(x_lst, T_0_1_BnF_5_lst, linestyle="--", linewidth=1, alpha=0.9, label="t=0.1 Fourier 5")
plt.plot(x_lst,Temp_new_01, linestyle="--",  linewidth=1, alpha=0.9,label="t=0.1 Finite Diff")

plt.plot(x_lst, T_1_Analytical, linestyle="--", linewidth=1, alpha=0.9, label="t=1 Analytical")
#plt.plot(x_lst, T_1_Bna_3_lst,  linestyle="-",  linewidth=1, alpha=0.9, label="t=1 Analytical 3")
plt.plot(x_lst, T_1_BnF_3_lst,  linestyle="--", linewidth=1, alpha=0.9, label="t=1 Fourier 3")

#plt.plot(x_lst, T_1_Bna_5_lst,  linestyle="-",  linewidth=1, alpha=0.9, label="t=1 Analytical 5")
plt.plot(x_lst, T_1_BnF_5_lst,  linestyle="--", linewidth=1, alpha=0.9, label="t=1 Fourier 5")
plt.plot(x_lst,Temp_new_1, linestyle="--",  linewidth=1, alpha=0.9,label="t=1 Finite Diff")

plt.plot(x_lst, T_10_Analytical, linestyle="-",  linewidth=1, alpha=0.9, label="t=10 Analytical")
#plt.plot(x_lst, T_10_Bna_3_lst, linestyle="-",  linewidth=1, alpha=0.9, label="t=10 Analytical 3")
plt.plot(x_lst, T_10_BnF_3_lst, linestyle="--", linewidth=1, alpha=0.9, label="t=10 Fourier 3")

#plt.plot(x_lst, T_10_Bna_5_lst, linestyle="-",  linewidth=1, alpha=0.9, label="t=10 Analytical 5")
plt.plot(x_lst, T_10_BnF_5_lst, linestyle="--", linewidth=1, alpha=0.9, label="t=10 Fourier 5")
plt.plot(x_lst,Temp_new_10, linestyle="--",  linewidth=1, alpha=0.9,label="t=10 Finite Diff")


plt.xlabel("Length")
plt.ylabel("Temperature")
plt.legend()
plt.title("Analytical, Fourier, Finite Diff Length vs Temp t=0.1,1,10 Bn = 3 and 5")
plt.show()