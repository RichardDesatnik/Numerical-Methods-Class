import numpy as np
import matplotlib.pyplot as plt
import math

#y1 = math.sin(x)+ math.log(x) - 1
#y2 = math.exp(x) + (x**2) + (-3*x) + (-2)

x_root = [-0.390272,1.44624]
y_root = [0,0]

y1_lst = []
y2_lst = []
x_lst = []
zero_lst = []
y1_1_lst = []

for x in np.arange(.01,15,0.01):
    x_lst.append(x)
    zero_lst.append(0)
    y1 = math.sin(x)+ math.log(x) - 1   
    print(y1)
    y1_lst.append(y1)

print("length of x_lst")
print(len(x_lst))

plt.title("Find Root f(x) = e^x + x^2 -3x -2")
plt.plot(x_lst,y1_lst, color = "blue", linewidth=2)

plt.plot(x_lst,zero_lst, color = "green")
plt.scatter(x_root, y_root, color = "red", marker= 'x', linewidth = 4)
plt.show()