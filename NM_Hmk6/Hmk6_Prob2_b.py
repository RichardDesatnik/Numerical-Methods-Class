import matplotlib.pyplot as plt
import numpy as np

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

for j in np.arange(1,(0.1/delta_t)+1):
    Temp_lst = []
    for i in np.arange(0,(1/delta_x)+1):
        if i == 0:
            Temp_lst.append(0)
        elif (i != 0 and i != L):
            Temp_lst.append(Temp(T_p1=Temp_new_01[int(i+1)],T1=Temp_new_01[int(i)],T_m1=Temp_new_01[int(i-1)]))
        elif int(i) == L:
            Temp_lst.append(0)
    Temp_new_01 = Temp_lst

for j in np.arange(1,(1/delta_t)+1):
    Temp_lst = []
    for i in np.arange(0,(1/delta_x)+1):
        if i == 0:
            Temp_lst.append(0)
        elif (i != 0 and i != L):
            Temp_lst.append(Temp(T_p1=Temp_new_1[int(i+1)],T1=Temp_new_1[int(i)],T_m1=Temp_new_1[int(i-1)]))
        elif int(i) == L:
            Temp_lst.append(0)
    Temp_new_1 = Temp_lst

for j in np.arange(1,(10/delta_t)+1):
    Temp_lst = []
    for i in np.arange(0,(1/delta_x)+1):
        if i == 0:
            Temp_lst.append(0)
        elif (i != 0 and i != L):
            Temp_lst.append(Temp(T_p1=Temp_new_10[int(i+1)],T1=Temp_new_10[int(i)],T_m1=Temp_new_10[int(i-1)]))
        elif int(i) == L:
            Temp_lst.append(0)
    Temp_new_10 = Temp_lst

plt.plot(x_lst,Temp_new_01, label="t=0.1")
plt.plot(x_lst,Temp_new_1, label="t=1")
plt.plot(x_lst,Temp_new_10, label="t=10")
plt.xlabel("Length x")
plt.ylabel("Temperature")
plt.title("Finite Difference Temp")
plt.legend()
plt.show()