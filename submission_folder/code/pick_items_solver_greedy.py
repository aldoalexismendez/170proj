import os
import numpy as np
import pq
import graph

DIRECTORY = "../../project_instances/"
OUTPUT_DIRECTORY = "../output/"

#NEED TO IMPLEMENT, MUST RETURN LIST
def indep_set(nodes):
    return nodes

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
    #constraint_matrix = np.ones((N,N))
    p = pq.PriorityQueue()#keeps track of best items
    total_money = 0
    total_weight = 0
    items_taken = []
    total_constraints = []
    constraints_map = {i: [] for i in range(N)} #want to map class to classes, can have at most N classes
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
        #for j in temp:
        #    for k in temp:
        #        if j != k: #can only be incompatible with others, not themselves
        #            constraint_matrix[j][k] = 0
        #constraints.append(temp)

        #Populate constraint map
        for j in temp:
            new_temp = [k for k in temp if k != j]
            for q in new_temp:
                try:
                    constraints_map[j].append(q)
                except KeyError:
                    constraints_map[j] = [q]

    #Create independent set
    #indep_set = independent_set(items) #STILL NEED TO IMPLEMENT
    #random_set = random.shuffle(items)
    random_set = items

    #place items of independent set into PQ based on weight/profit ratio
    for item in random_set:
        #print float(item[2])
        #print float(item[3])
        try:
            ratio = float(item[2])/(float(item[4]) - float(item[3]))
        except ZeroDivisionError:
            ratio = 0
        if ratio >= 0: #ensures no items with negative profit are added
            p.push(item, ratio)

    #Greedy part
    #total_money <= MAX_MONEY and total_weight <= MAX_POUNDS and
    while not p.isEmpty():
        item = p.pop()
        item_name = item[0]
        item_class = int(item[1])
        item_weight = float(item[2])
        item_cost = float(item[3])
        incompatible_classes = constraints_map[item_class]

        ##
        if item_class in total_constraints: #item is incompatible with classes so far
            continue
        ##

        items_taken.append(item_name)
        for c in incompatible_classes: total_constraints.append(c)
        if total_weight + item_weight > MAX_POUNDS or total_money + item_cost > MAX_MONEY:
            break
        else:
            total_weight += item_weight
            total_money += item_cost

    #Create output file
    f = open(OUTPUT_DIRECTORY + file_name[:-3] + ".out", "w+")
    for item in items_taken:
        f.write(item + "\n")
