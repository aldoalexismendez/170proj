import random
import sys

problem_num = sys.argv[1]
MAX_POUNDS = 2**(32) - 1 
MAX_MONEY = 2**(32) - 1
MAX_N = 100000 #200,000 number of items
MAX_C = 125000 #200,000 number of constraints
name = "problem"
rest_name = ".in"
items = []
constraints = []
classes = [i for i in range(0,1000)]

#create random items of class 1-1000 (can tweak parameters)
for i in range(1, int(MAX_N/4)):
    c = random.choice(classes)
    weight = 1000*random.random()
    cost = 1000*random.random()
    resale = cost + 100*random.random()
    temp = "item" + str(i) + "; " + str(c) + "; "
    temp += str(round(weight,2)) + "; " + str(round(cost,2)) + "; " +str(round(resale,2))
    items.append(temp)

#create random constraints
for i in range(0,int(MAX_C/4)):
    num_c = int(5*random.random())
    #ensures there are at least 2 variables per constraint
    if num_c < 2:
        num_c += 2
    temp = ""
    for i in range(num_c):
        temp += str(random.choice(classes)) + ", "
    temp = temp[:-2]
    constraints.append(temp)

#create/open file
f = open(name + problem_num + rest_name, "w+")
f.write(str(MAX_POUNDS) + "\n")
f.write(str(MAX_MONEY) + "\n")
f.write(str(MAX_N) + "\n")
f.write(str(MAX_C) + "\n")

#write items
for item in items:
    f.write(item)
    f.write("\n")
#for loop, write constraints
for constraint in constraints:
    f.write(constraint)
    f.write("\n")

f.close()
