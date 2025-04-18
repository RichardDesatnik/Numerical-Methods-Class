import matplotlib.pyplot as plt

x1 = [1,2,3,4]
x2 = [2,3,4,5]
t = [1,2,3,4]

plt.plot(t, x1, color="blue")
plt.plot(t, x2, color="green")

plt.title("Problem 2d x1 and x2")
plt.xlabel("x value")
plt.ylabel("time")

plt.show()

