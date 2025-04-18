import matplotlib.pyplot as plt

time_file = open("C:/Users/rdesa/NM_Test_Data/output_Test2_b_t.txt", "r")
data = time_file.read() 
data_time = data.replace('\n', ' ')
time_file.close()

G01_file = open("C:/Users/rdesa/NM_Test_Data/output_test_2diii_x1_gamma_01.txt", "r")
data = G01_file.read() 
data_G01 = data.replace('\n', ' ')
G01_file.close() 

G1_file = open("C:/Users/rdesa/NM_Test_Data/output_test_2diii_x1_gamma_1.txt", "r")
data = G1_file.read() 
data_G1 = data.replace('\n', ' ')
G1_file.close() 

G10_file = open("C:/Users/rdesa/NM_Test_Data/output_test_2diii_x1_gamma_10.txt", "r")
data = G10_file.read() 
data_G10 = data.replace('\n', ' ')
G10_file.close() 

x2G01_file = open("C:/Users/rdesa/NM_Test_Data/output_test_2diii_x2_gamma_01.txt", "r")
data = x2G01_file.read() 
x2data_G01 = data.replace('\n', ' ')
x2G01_file.close() 

x2G1_file = open("C:/Users/rdesa/NM_Test_Data/output_test_2diii_x2_gamma_1.txt", "r")
data = x2G1_file.read() 
x2data_G1 = data.replace('\n', ' ')
x2G1_file.close() 

x2G10_file = open("C:/Users/rdesa/NM_Test_Data/output_test_2diii_x2_gamma_10.txt", "r")
data = x2G10_file.read() 
x2data_G10 = data.replace('\n', ' ')
x2G10_file.close() 

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
print("t")
print(t)
x1_G01 = data_to_list(data_G01)
#print("x1_G01")
#print(x1_G01)
x1_G1 = data_to_list(data_G1)
x1_G10 = data_to_list(data_G10)
x2_G01 = data_to_list(x2data_G01)
x2_G1 = data_to_list(x2data_G1)
x2_G10 = data_to_list(x2data_G10)

fig, axes = plt.subplots(nrows=1, ncols=1)

fig.suptitle('Test Problem 2a b c x1', fontsize=12)

#axes.plot(t, x1_G01, color="blue")
#axes.plot(t, x2_G01, color="green")
#axes.set_title("Gamma = 0.1", fontsize=14)
#axes.set_ylabel("x displacement", fontsize=14)
#axes.set_xlabel("time", fontsize=14)
#axes.set_ylim(-40, 40)
#axes.legend(["x1 mass m","x2 mass gamma_m"], fontsize="large")

axes.plot(t, x1_G1, color="blue")
axes.plot(t, x2_G1, color="green")
axes.set_title("Gamma = 1", fontsize=14)
axes.set_ylabel("x displacement", fontsize=14)
axes.set_xlabel("time", fontsize=14)
axes.set_ylim(-20, 20)
axes.legend(["x1 mass m","x2 mass gamma_m"], fontsize="large")

#axes.plot(t, x1_G10, color="blue")
#axes.plot(t, x2_G10, color="green")
#axes.set_title("Gamma = 10", fontsize=14)
#axes.set_ylabel("x displacement", fontsize=14)
#axes.set_xlabel("time", fontsize=14)
#axes.set_ylim(-20, 20)
#axes.legend(["x1 mass m","x2 mass gamma_m"], fontsize="large")

plt.show()
