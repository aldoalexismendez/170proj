import os
import pq

#Used PriorityQueue class from CS188

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

        #Populate constraint map
        for j in temp:
            new_temp = [k for k in temp if k != j]
            for q in new_temp:
                try:
                    constraints_map[j].append(q)
                except KeyError:
                    constraints_map[j] = [q]

    #place items into PQ based on weight/profit ratio
    for item in items:
        try:
            ratio = float(item[2])/(float(item[4]) - float(item[3]))
        except ZeroDivisionError:
            ratio = 0
        if ratio >= 0: #ensures only non-negative profit items are added
            p.push(item, ratio)

    #Greedy part
    while not p.isEmpty():
        item = p.pop()
        item_name = item[0]
        item_class = int(item[1])
        item_weight = float(item[2])
        item_cost = float(item[3])
        incompatible_classes = constraints_map[item_class]

        #Constraint
        if item_class in total_constraints: #item is incompatible with classes so far
            continue

        #items_taken.append(item_name)
        for c in incompatible_classes: total_constraints.append(c)
        if total_weight + item_weight > MAX_POUNDS or total_money + item_cost > MAX_MONEY:
            continue
        else:
            total_weight += item_weight
            total_money += item_cost
            items_taken.append(item_name)

    #Create output file
    f = open(OUTPUT_DIRECTORY + file_name[:-3] + ".out", "w+")
    for item in items_taken:
        f.write(item + "\n")
