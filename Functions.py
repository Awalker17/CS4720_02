import logging
import random

# read from a file for testing.
def setupFile(file_name, num_Items):
    File_object = open(file_name, "r")
    Max = int(File_object.readline())
    T_objects = {}
    for i in range(0, num_Items):
        T_objects[i] = File_object.readline().split()
        T_objects[i] = toIntList(T_objects[i])
        print(T_objects[i])
    File_object.close()

    return Max, T_objects

# when reading in from a file fix the type from string to int
def toIntList(List):
    for i in range(0, len(List)):
        List[i] = int(List[i])
    return List

# sum all the weights and values of a given list (2d array)
def findTotal(List):  # weights are going to be first and the values second in the list
    Total_Weight = 0
    Total_Values = 0
    for item in List:
        Total_Weight += item[0]
        Total_Values += item[1]
    # print(List)
    # print(Total_Weight, Total_Values, sep= "\t")
    return Total_Values, Total_Weight

# Exhaustive search algorithm big O(2^n)
def combinations(target, data):
    for i in range(len(data)):
        new_lis = target.copy()
        new_data = data.copy()
        new_lis.append(data[i])
        new_data = data[i + 1:]

        yield new_lis

        for combo in combinations(new_lis, new_data):
            yield combo

# creates a dictionary of lists [weight, value]
# also returns the max weight of the Rocket
def NumbGenerator(numb_objects=3):
    max_weight = 10000
    Objects = {}
    for i in range(numb_objects):
        Objects[i] = [random.randint(1, 10000), random.randint(1, 100)]
    return max_weight, Objects

# Greedy search algorithm big O()
def greedySerch(Objects, Max_weight):
    counter = 0
    Items = list(Objects.values())
    Highest_weight = 0
    Highest_value = 0
    combo = []
    for item in Items:
        if ((item[0] <= Max_weight and item[1] > Highest_value)):
            counter += 1
            combo = []
            Highest_weight = item[0]
            Highest_value = item[1]
            combo.append(item)

    Cweight = Highest_weight
    SomethingFound = True
    while (Cweight < Max_weight and SomethingFound == True):
        SomethingFound = False
        Items.remove(combo[-1])
        Highest_weight = 0
        Highest_value = 0
        tempCombo = []
        for item in Items:
            counter += 1
            if (item[1] > Highest_value and (Cweight + item[0]) <= Max_weight):
                Highest_weight = item[0]
                Highest_value = item[1]
                tempCombo = item
                SomethingFound = True
        if SomethingFound:
            combo.append(tempCombo)
            Cweight = findTotal(combo)[1]

    print("With " + str(len(Objects)) + " number of items we ran " + str(counter) + " times")
    return findTotal(combo)
