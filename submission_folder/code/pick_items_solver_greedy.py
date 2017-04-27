import os
import numpy as np
import pq
import graph

DIRECTORY = "../../project_instances/"
OUTPUT_DIRECTORY = "../output/"

for file_name in os.listdir(DIRECTORY):
    #Ensures that only .in files are opened
    if not file_name.endswith(".in"):
        continue
    file_obj = open(DIRECTORY + file_name, "r")
    
    #Set variables
    MAX_POUNDS = round(float(file_obj.readline()),2)
    MAX_MONEY = round(float(file_obj.readline()),2)
    N = int(file_obj.readline())
    C = int(file_obj.readline())
    items = []
    constraints = []
    constraint_matrix = np.ones((N,N))
    p = pq.PriorityQueue()#keeps track of best items
    total_money = 0
    total_weight = 0
    items_taken = []
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

    #Create independent set
    #place items of independent set into PQ based on weight/profit ratio
    for i in range(5):
        item = items[i]
        ratio = float(item[2])/float(item[3])
        p.push(item, ratio)

    #Greedy part
    while total_money <= MAX_MONEY and total_weight <= MAX_POUNDS and not p.isEmpty():
        item = p.pop()
        items_taken.append(item[0])
        total_weight += float(item[2])
        total_money += float(item[3])

    #Create output file
    f = open(OUTPUT_DIRECTORY + file_name[:-3] + ".out", "w+")

    for item in items_taken:
        f.write(item + "\n")
