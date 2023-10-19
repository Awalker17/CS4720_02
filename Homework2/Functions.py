import logging

# read from a file for testing.
def setupFile(file_name):
    File_object = open(file_name, "r")

    String1 = File_object.readline()[:-1]
    String2 = File_object.readline()
    File_object.close()

    return String1, String2

def deleteALetter(String, index):
    String = String[:index] + String[index+1:]
    return String
def changeALetter(String, index, changeTo):
    String = String[:index] + changeTo + String[index+1:]
    return String
def insertALetter(String, index, letterToInsert):
    String = String[:index+1] + letterToInsert + String[index+1:]
    return String

def SearchAhead(String1, String2, currentIndex):
    SearchFor = String2[currentIndex]
    if SearchFor in String1:
        return String1.index(SearchFor)
    else:
        return -1


