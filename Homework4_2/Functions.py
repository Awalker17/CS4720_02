
# read from a file for testing.
def setupFile(File_object):
    String1 = File_object.readline()[:-1]
    String2 = File_object.readline()[:-1]

    return String1, String2

# for the next two functions because the string may not have the same number of letters
# a try except will allow the use of the same code for the last letter of a string
#if they are not the same length then a change needs to be made so just return 1

# Check the next letter in string 2 and compare to the current letter in string 1
# if they are the same then we need to insert a letter into string 1
def checkForInsert(String1, String2, index):
    try:
        if String1[index] == String2[index+1] and not String1[index+1] == String2[index+1]:
            return 1
        else:
            return 0
    except IndexError:
        return 0

# Check the next letter in string 1 and compare to the current letter in string 2
# if they are the same then we need to delete a letter into string 1
def checkForDelete(String1, String2, index):
    try:
        if String1[index+1] == String2[index] and not String1[index+1] == String2[index+1]:
            return 1
        else:
            return 0
    except IndexError:
        return 0