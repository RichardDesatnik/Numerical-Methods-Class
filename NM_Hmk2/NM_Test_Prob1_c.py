import matplotlib.pyplot as plt
import numpy as np
import math 
np.set_printoptions(suppress=True, precision=3)
T = [25,30,35,40,45,50,60,70,80,90,100,150,200,250,273,300,350,400,450,500,600,700]
K = [459.5,317.7,233.3,180.3,143.2,118.4,85.2,66.6,54.4,46.1,40.2,23.3,16.5,12.6,11.5,10.5,8.8,7.6,6.9,6.1,5.1,4.5]


n = len(T)
sum_T = 0
sum_K = 0
sum_Tpow = 0
sum_TK = 0 

for i in range(len(T)):
    sum_T = sum_T + math.log(T[i])
    sum_K = sum_K + math.log(K[i])
    sum_Tpow = sum_Tpow + math.log(T[i])**2
    sum_TK = sum_TK + math.log(T[i])*math.log(K[i])

print(sum_T)
print(sum_K)
print(sum_Tpow)
print(sum_TK)

b1 = ((n*sum_TK) - (sum_T*sum_K))/((n*sum_Tpow)-(sum_T**2))
b0 = (sum_K - (b1*sum_T))/n

print(b1)
print(b0)

A = math.exp(b0)
print(A)

K_fit_lst = []
for i in range(len(T)):
    K_fit = A*(T[i]**b1)
    K_fit_lst.append(K_fit)


Yi_Ybar_2 = 0
sumy = 0
num_dict = 8
for i in range(len(T)):
    sumy = sumy + K[i]
Ybar = sumy/n
for i in range(len(K)):
    Yi_Ybar_2 = Yi_Ybar_2 + ((K[i]-Ybar)**2)


def R_squared(k_values):
    ks_diff = 0
    for i in range(len(K)):
        ks_diff = ks_diff + ((K[i]-k_values[i])**2)
    R = 1 - ks_diff/Yi_Ybar_2
    return R

#for label, y_values in K_T_Plot.items():
Rs = R_squared(k_values=K_fit_lst)
print(" The R Value is: "+str(Rs))

plt.plot(T, K_fit_lst, label="K(T) = 25242T^-1.36", color="green")
plt.scatter(T,K, label="Raw Data")

#plt.plot(T, E_decay_lst, label="Exponential Decay")
#Rs = R_squared(k_values=E_decay_lst)
#print("The R Value of e_decay is: "+str(Rs))
# Customize the plot
plt.xlabel("Temperature")
plt.ylabel("K Value")
plt.title("Temperature verse K")
plt.legend()  # Show legend
#plt.grid(True)  # Add grid for better visualization

# Show the plot
plt.show()