import logging
import time
from Functions import *
from Plot_Results import *

# use # on disable line to enable debug print statements
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

'''
Error with runtime counts so the program pauses for .01 which add .01 t the runtime
the wait time is then subtacted to make the runtime a accurate as posible. 
'''
WAITTIME = .01

# saves the runtimes in a list for the plotting step
AVE_RUNTIME_E = []
AVE_RUNTIME_G = []

# opens a file to save all the runtimes to for your veiwing and debugging pleasuerpy
# under Times.txt
times = open(r"Times.txt", "w")
times.write("NUMBER OF ITEMS\t\tExhaustive\t\t\t\tGreedy\n")

# main program run
for i in range(3, 16):
    # Average runtime counter
    average_T_Exahstive = 0
    average_T_greedy = 0

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

        # Print search exhaustive algorithm results
        print("EXHAUSTIVE:\nBring\n", highest_combo)
        print("Total Value\n", highest_value)
        print("Total Weight\n", highest_weight)
        print("TIME TO COMPLETE ALGORITHM", (time.time() - starttime - WAITTIME))

        logging.debug("NUMBER OF COMBINATIONS " + str(counter) + " for " + str(i) + " items")

        starttime = time.time()  # start timer

        # run search algo.
        value, weight = greedySerch(Objects, Max_weight)

        time.sleep(WAITTIME)  # wait number of seconds
        stoptime = time.time()  # stop timer
        average_T_greedy += stoptime - starttime - WAITTIME  # add timer to average

        # print results of greedy algorithm
        print("Greedy:\nBring\n", highest_combo)
        print("Total Value\n", highest_value)
        print("Total Weight\n", highest_weight)

        print("TIME TO COMPLETE ALGORITHM", (time.time() - starttime - WAITTIME))

    # find search algorithm time average
    average_T_Exahstive /= 5
    average_T_greedy /= 5

    # append to average runtime list (plotting)
    AVE_RUNTIME_E.append(average_T_Exahstive)
    AVE_RUNTIME_G.append(average_T_greedy)

    # write to file
    times.write("{:20s}".format(str(i)) + "{:20s}".format(str(average_T_Exahstive)))
    times.write("\t" + str(average_T_greedy) + "\n")

times.close()  # Close file

plot_runtimes(AVE_RUNTIME_E, AVE_RUNTIME_G)  # make plot
plot_Items(Objects)
