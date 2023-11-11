import logging

# read from a file for testing.
def setupFile(file_name):
    File_object = open(file_name, "r")

    String1 = File_object.readline()[:-1]
    String2 = File_object.readline()
    File_object.close()

    return String1, String2

def deleteALetter(String, index):
    print("Deleting a letter")
    String = String[:index] + String[index+1:]
    return String
def changeALetter(String, index, changeTo):
    print("replacing a letter")
    String = String[:index] + changeTo + String[index+1:]
    return String
def insertALetter(String, index, letterToInsert):
    print("Inserting a letter")
    String = String[:index] + letterToInsert + String[index:]
    return String

def SearchAhead(String1, String2, currentIndex):
    substring = "_" * currentIndex + String1[currentIndex:]
    SearchFor = String2[currentIndex]
    #print("SEARCHING FOR:", SearchFor, "in", substring)
    if SearchFor in substring:
        return String1.index(SearchFor)
    else:
        return -1
def checkWordisSame(String1, String2, index):
    check = True
    newIndex = 0
    for i in range(index):
        if String1[i] != String2[i]:
            newIndex = i
            check = False
    return check, newIndex



