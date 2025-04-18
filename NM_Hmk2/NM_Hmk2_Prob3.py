import numpy as np
import matplotlib.pyplot as plt 

#radius = list(range())
step = 0.2
start = 1.0
end = 5.0

radius = [round(start + i * step, 1) 
           for i in range(int((end - start) / step) + 1)]
#print(my_list)
#np.array(range(1,.2,5))

Ti = 5
Ri = 1
Ro = 5
To = 30

temp = []
rad = []
for r in radius:
    rad.append(r)
    t = Ti + (((-Ri/r)+1)*(((Ti-To)*Ro)/(Ri-Ro)))
    temp.append(t)
    print("at r of: " + str(r) + " t is: " + str(t))

temp_n = [5, 10.2083,13.9286,16.7188,18.8889,20.625,22.0455,23.2292,24.2308,25.0893,25.8333,26.4844,27.0588,27.5694,28.0263,28.4375,28.8095,29.1477,29.4565,29.7396,30]

# Create the scatter plot
plt.scatter(rad, temp, label='y1', color ='blue', marker='s')
plt.scatter(rad, temp_n, label='y2', color ='red')

# Add a line plot for y1
plt.plot(rad, temp, linestyle='--', color ='blue', linewidth=4)
plt.plot(rad, temp_n, linestyle='--', color ='red', linewidth=2)

# Add labels and title
plt.xlabel('Radius')
plt.ylabel('Temp')
plt.title('Prob 3 Analytical vs Numerical')

# Show the legend
plt.legend()

# Show the plot
plt.show()