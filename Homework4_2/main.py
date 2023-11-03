'''
How many steps does it take to chage one sting to another.
In this program you can only: change, insert, or delete
'''
from Functions import *
def countDifference(String1, String2, m, changes = []):
    # Check the first letter
    if String1[0] == String2[0]:
        changes.append(0)
    else:
        # run both checks
        insert = checkForInsert(String1, String2, 0)
        delete = checkForDelete(String1, String2, 0)
        if insert:  # if insert returned true add a black character to correct the indexes for fallowing charaters
            String1 = "_" + String1
        elif delete:  # if delete returned try remove a character to correct the indexes for the fallowing characters.
            String1 = String1[1:]

        # if both are false then a change needs to be made we don't have to check
        # if the letter isn't the same (doesn't matter what the change is) make one change
        changes.append(1)

    # print(changes[0])

    for index in range(1, m):
        try:
            #print(String1[index], String2[index])
            if String1[index] == String2[index]:
                changes.append(changes[index - 1])
            else:
                # run both checks
                insert = checkForInsert(String1, String2, index)
                delete = checkForDelete(String1, String2, index)
                if insert:  # if insert returned true add a black character to correct the indexes for fallowing charaters
                    String1 = String1[:index] + "_" + String1[index:]

                elif delete:  # if delete returned try remove a character to correct the indexes for the fallowing characters.
                    String1 = String1[:index] + String1[index + 1:]

                # if both are false then a change needs to be made we don't have to check
                # if the letter isn't the same (doesn't matter what the change is) make one change

                changes.append(1 + changes[index - 1])
                #print(String1)
        except IndexError:
            # While checking each letter
            # if either String1 or String2 is too short there needs to have a change made
            # whether is insert or delete add one to the count
            changes.append(1 + changes[index - 1])
            '''
            try:
                print(" ", String2[index])
            except IndexError:
                print(String1[index])
            print(changes)
            '''

    return changes[-1]


File_object = open(r"Tester.txt", "r")

for i in range(0,8):
    String1, String2 = setupFile(File_object)
    print(String1 + ",", String2 + ", m = " + str(max(len(String1), len(String2))))
    F = []
    changes = countDifference(String1, String2, max(len(String1), len(String2)), F )
    print("Number of Changes: ",changes, "\n")

File_object.close()

