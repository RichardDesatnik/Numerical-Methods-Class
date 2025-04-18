import matplotlib.pyplot as plt
import numpy as np
import math

def func(theta,b):
    f_theta = math.sqrt( 1.0 - (1.0 - b**2)*(math.sin(theta))**2 )
    #print(f_theta)
    return(f_theta)

#b_lst = [.25,.5,.75]

w1 = 0.652145
w2 = 0.652145
w3 = 0.347855
w4 = 0.347855

#theta1 = ((math.pi*0.5)/2) + (((math.pi*0.5)/2)*((1/3)**0.5))
#theta2 = ((math.pi*0.5)/2) + (((math.pi*0.5)/2)*(-((1/3)**0.5)))

#mid = (0 + math.pi/2)/2   # = pi/4
#half = (math.pi/2 - 0)/2  # = pi/4
theta1 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(-.339981)
theta2 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(.339981)
theta3 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(-.861136)
theta4 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(.861136)
#theta5 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(.661209)
#theta6 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(.93247)

#print("thetas")
#print(theta1)
#print(theta2)
#print(theta3)
#print(theta4)

a=1
b_list = []
approx_P_a = []
real_P_a = []

b_values = np.arange(0, 1.001, 0.001).tolist()
for b in b_values:
    b_list.append(b)
    #print("for b at:" + str(b))
    per_exact = 4*(math.pi/4)*(w1*func(theta1,b) + w2*func(theta2,b) + w3*func(theta3,b) + w4*func(theta4,b))
    real_P_a.append(per_exact)
    per_approx = math.sqrt(2)*math.pi*math.sqrt((a**2) + (b**2))
    approx_P_a.append(per_approx)
    #print(per_approx-per_exact)
    if (per_approx-per_exact)<(0.01):
        print(b)
    #print(per)

# Create the plot
plt.plot(b_list, real_P_a, color='blue', label='exact')
#plt.plot(b_list, approx_P_a, linestyle='--', color = 'red', label='approx')
# Add labels and title
plt.xlabel("b/a")
plt.ylabel("P/a")
plt.title("n=4 P/a vs. b/a plot")

# Add grid lines
#plt.grid(True)
#plt.legend()
# Show the plot
plt.show()