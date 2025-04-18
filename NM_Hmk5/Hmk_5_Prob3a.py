import math

def func(theta,b):
    f_theta = math.sqrt( 1.0 - (1.0 - b**2)*(math.sin(theta))**2 )
    print(f_theta)
    return(f_theta)

b_lst = [.25,.5,.75]

w1 = 0.171324
w2 = 0.360763
w3 = 0.467913
w4 = 0.467913
w5 = 0.360763
w6 = 0.171324
#theta1 = ((math.pi*0.5)/2) + (((math.pi*0.5)/2)*((1/3)**0.5))
#theta2 = ((math.pi*0.5)/2) + (((math.pi*0.5)/2)*(-((1/3)**0.5)))

#mid = (0 + math.pi/2)/2   # = pi/4
#half = (math.pi/2 - 0)/2  # = pi/4
theta1 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(-.93247)
theta2 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(-.661209)
theta3 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(-.238619)
theta4 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(.238619)
theta5 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(.661209)
theta6 = ((0 + math.pi/2)/2) + ((math.pi/2 - 0)/2)*(.93247)

print("thetas")
print(theta1)
print(theta2)
print(theta3)
print(theta4)
print(theta5)
print(theta6)

for b in b_lst:
    print("for b at:" + str(b))
    per = 4*(math.pi/4)*(w1*func(theta1,b) + w2*func(theta2,b) + w3*func(theta3,b) + w4*func(theta4,b) + w5*func(theta5,b)+ w6*func(theta6,b))
    print(per)