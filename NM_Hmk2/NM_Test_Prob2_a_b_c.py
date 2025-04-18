import matplotlib.pyplot as plt

time_file = open("C:/Users/rdesa/NM_Test_Data/output_Test2_b_t.txt", "r")
data = time_file.read() 
data_time = data.replace('\n', ' ')
time_file.close()

B0_file = open("C:/Users/rdesa/NM_Test_Data/output_Test2_b_x1_B0.txt", "r")
data = B0_file.read() 
data_B0 = data.replace('\n', ' ')
B0_file.close() 

B001_file = open("C:/Users/rdesa/NM_Test_Data/output_Test2_b_x1_B001.txt", "r")
data = B001_file.read() 
data_B001 = data.replace('\n', ' ')
B001_file.close() 

B01_file = open("C:/Users/rdesa/NM_Test_Data/output_Test2_b_x1_B01.txt", "r")
data = B01_file.read() 
data_B01 = data.replace('\n', ' ')
B01_file.close() 

B1_file = open("C:/Users/rdesa/NM_Test_Data/output_Test2_b_x1_B1.txt", "r")
data = B1_file.read() 
data_B1 = data.replace('\n', ' ')
B1_file.close() 

B10_file = open("C:/Users/rdesa/NM_Test_Data/output_Test2_b_x1_B10.txt", "r")
data = B10_file.read() 
data_B10 = data.replace('\n', ' ')
B10_file.close() 

def data_to_list(data_into_list):
    t_list = []
    time_str = ''
    for data in data_into_list:
        if data == ',':
            time = float(time_str)
            t_list.append(time)
            time_str = ''
        if data == ' ':
            pass
        elif data == ',':
            pass
        elif data == '.':
            time_str = time_str+data
        else:
            time_str = time_str+data 
    return t_list

t = data_to_list(data_time)
x1_B0 = data_to_list(data_B0)
x1_B001 = data_to_list(data_B001)
x1_B01 = data_to_list(data_B01)
x1_B1 = data_to_list(data_B1)
x1_B10 = data_to_list(data_B10)



fig, axes = plt.subplots(nrows=1, ncols=1)

fig.suptitle('Test Problem 2a b c x1', fontsize=12)

#axes.plot(t, x1_B0, color="blue")
#axes.set_title("B = 0", fontsize=14)
#axes.set_ylabel("x displacement", fontsize=14)
#axes.set_xlabel("time", fontsize=14)
#axes[0].set_ylim(-10, 10)
#axes[0].set_ylabel("c = 0")
#axes[0].legend(["x1 mass 1m","x2 mass 3m"], fontsize="large")

#axes.plot(t, x1_B001, color="blue")
#axes.set_title("B = 0.01", fontsize=14)
#axes.set_ylabel("x displacement", fontsize=14)
#axes.set_xlabel("time", fontsize=14)
#axes.set_ylim(-5, 5)
#axes[0].set_ylabel("c = 0")
#axes[0].legend(["x1 mass 1m","x2 mass 3m"], fontsize="large")

#axes.plot(t, x1_B01, color="blue")
#axes.set_title("B = 0.1", fontsize=14)
#axes.set_ylabel("x displacement", fontsize=14)
#axes.set_xlabel("time", fontsize=14)
#axes.set_ylim(-5, 5)
#axes[0].set_ylabel("c = 0")
#axes[0].legend(["x1 mass 1m","x2 mass 3m"], fontsize="large")

#axes.plot(t, x1_B1, color="blue")
#axes.set_title("B = 1", fontsize=14)
#axes.set_ylabel("x displacement", fontsize=14)
#axes.set_xlabel("time", fontsize=14)
#axes.set_ylim(-5, 5)
#axes[0].set_ylabel("c = 0")
#axes[0].legend(["x1 mass 1m","x2 mass 3m"], fontsize="large")

axes.plot(t, x1_B10, color="blue")
axes.set_title("B = 10", fontsize=14)
axes.set_ylabel("x displacement", fontsize=14)
axes.set_xlabel("time", fontsize=14)
axes.set_ylim(-5, 5)
#axes[0].set_ylabel("c = 0")
#axes[0].legend(["x1 mass 1m","x2 mass 3m"], fontsize="large")

plt.show()