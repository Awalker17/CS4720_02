'''
Alex Walker
10/4
MAIN PROGRAM: Knapsack problem
Funtions used in Functions.py and Plot_results.py
'''

import logging
import time
from Functions import *
from Plot_Results import *

# use # on disable line to enable debug print statements
#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

'''
Error with runtime counts so the program pauses for .01 which add .01 t the runtime
the wait time is then subtacted to make the runtime a accurate as posible. 
'''
WAITTIME = .01

# saves the runtimes in a list for the plotting step
AVE_RUNTIME_E = []
AVE_RUNTIME_G = []

AVE_WEIGHT_E = []
AVE_WEIGHT_G = []

AVE_VALUE_E = []
AVE_VALUE_G = []

EVERY_RUNTIME_E = []
EVERY_RUNTIME_G = []

EVERY_WEIGHT_E = []
EVERY_WEIGHT_G = []

# opens a file to save all the runtimes to for your veiwing and debugging pleasuerpy
# under Times.txt
times = open(r"Times.txt", "w")
times.write("NUMBER OF ITEMS\t\tExhaustive\t\t\t\tGreedy\n")

# main program run
for i in range(3, 16):
    # Average runtime counter
    average_T_Exahstive = 0
    average_T_greedy = 0

    average_W_Exahstive = 0
    average_W_greedy = 0

    average_V_Exahstive = 0
    average_V_greedy = 0

    # each amount of items is run 5 times to improve runtime data accuracy
    for j in range(5):
        # Prints out a header for the terminal output
        print("RESULTS FOR ", i, " OBJECTS\n ", "-" * 50)

        # randomly generate numbers enable logging to view
        Max_weight, Objects = NumbGenerator(i)
        logging.debug(Objects)
        logging.debug(str(Max_weight))

        # initialize search algo variable (Exhaustive)
        highest_weight = 0
        highest_value = 0
        highest_combo = []

        starttime = time.time()  # Begin runtime counter

        target = []
        values = list(Objects.values())  # get all the values out of the objects dict

        counter = 0  # number of combinations being created counter (debug purposes only)
        time.sleep(WAITTIME)  # wait for amount of seconds

        # find the best combination
        for combo in combinations(target, values):
            value, weight = findTotal(combo)
            counter += 1
            if weight <= Max_weight and value > highest_value:
                highest_weight = weight
                highest_value = value
                highest_combo = combo

        stoptime = time.time()  # stop timer

        average_T_Exahstive += stoptime - starttime - WAITTIME  # add runtime to average
        average_W_Exahstive += highest_weight
        average_V_Exahstive += highest_value
        EVERY_RUNTIME_E.append([i, stoptime - starttime - WAITTIME ])
        EVERY_WEIGHT_E.append([i, highest_weight])


        # Print search exhaustive algorithm results
        print("EXHAUSTIVE:\nBring\n", highest_combo)
        print("Total Value\n", highest_value)
        print("Total Weight\n", highest_weight)
        print("TIME TO COMPLETE ALGORITHM", (time.time() - starttime - WAITTIME))

        logging.debug("NUMBER OF COMBINATIONS " + str(counter) + " for " + str(i) + " items")

        starttime = time.time()  # start timer

        # run search algo.
        highest_combo, highest = greedySerch(Objects, Max_weight)

        time.sleep(WAITTIME)  # wait number of seconds
        stoptime = time.time()  # stop timer

        average_T_greedy += stoptime - starttime - WAITTIME  # add timer to average
        average_W_greedy += highest[1]
        average_V_greedy += highest[0]

        EVERY_RUNTIME_G.append([i, stoptime - starttime - WAITTIME])
        EVERY_WEIGHT_G.append([i, highest[1]])

        # print results of greedy algorithm
        print("GREEDY:\nBring\n", highest_combo)
        print("Total Value\n", highest[0])
        print("Total Weight\n", highest[1])

        print("TIME TO COMPLETE ALGORITHM", (time.time() - starttime - WAITTIME))

    # find search algorithm time average
    average_T_Exahstive /= 5
    average_T_greedy /= 5

    average_W_Exahstive /= 5
    average_W_greedy /= 5

    average_V_Exahstive /= 5
    average_V_greedy /= 5

    # append to average runtime list (plotting)
    AVE_RUNTIME_E.append(average_T_Exahstive)
    AVE_RUNTIME_G.append(average_T_greedy)

    AVE_WEIGHT_E.append(average_W_Exahstive)
    AVE_WEIGHT_G.append(average_W_greedy)

    AVE_VALUE_E.append(average_V_Exahstive)
    AVE_VALUE_G.append(average_V_greedy)

    # write to file
    times.write("{:20s}".format(str(i)) + "{:20s}".format(str(average_T_Exahstive)))
    times.write("\t" + str(average_T_greedy) + "\n")

times.close()  # Close file

AVE_VALUE_R = []

for i in range(len(AVE_VALUE_E)):
    AVE_VALUE_R.append(AVE_VALUE_E[i]/AVE_VALUE_G[i])

# make plots
plot_runtimes(AVE_RUNTIME_E, AVE_RUNTIME_G, EVERY_RUNTIME_E, EVERY_RUNTIME_G)
plot_Items(AVE_WEIGHT_E, AVE_WEIGHT_G,EVERY_WEIGHT_E, EVERY_WEIGHT_G)
plot_ValueRatio(AVE_VALUE_R)
