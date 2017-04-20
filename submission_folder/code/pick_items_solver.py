import os

DIRECTORY = "../../project_instances/"

for file_name in os.listdir(DIRECTORY):
    file_obj = open(DIRECTORY + file_name, "r")
    MAX_POUNDS = round(float(file_obj.readline()),2)
    MAX_MONEY = round(float(file_obj.readline()),2)
    N = int(file_obj.readline())
    C = int(file_obj.readline())
    items = []
    constraints = []
    for i in range(N):
        items.append(file_obj.readline())
    for i in range(C):
        constraints.append(file_obj.readline())

    
