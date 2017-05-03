import os
import numpy as np

DIRECTORY = "../../project_instances/"

for file_name in os.listdir(DIRECTORY):
    if not file_name.endswith(".in"):
        continue
    file_obj = open(DIRECTORY + file_name, "r")
    MAX_POUNDS = round(float(file_obj.readline()),2)
    MAX_MONEY = round(float(file_obj.readline()),2)
    N = int(file_obj.readline())
    C = int(file_obj.readline())
    items = []
    constraints = []
    constraint_matrix = np.ones((N,N))
    for i in range(N):
        temp = file_obj.readline().split(";")
        temp[-1] = temp[-1][:-1]
        items.append(temp)
    for i in range(C):
        #speed up the following
        temp = file_obj.readline()
        temp = temp[:-1]
        temp = [int(compatible) for compatible in temp.split(",")]
        #create compatibility matrix    
        for j in temp:
            for k in temp:
                if j != k: #can only be incompatible with others, not themselves
                    constraint_matrix[j][k] = 0
        constraints.append(temp)


    
