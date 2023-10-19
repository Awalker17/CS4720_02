"""
Problem 2: Edit Distance Problem

Make an Algorithm to change one word to another by manipulating
the letter in a string.
You have 3 options:
Change a letter
insert a letter
delete a letter
"""

class NoSimularLetter(ValueError):
    pass
class ValuesNotTheSame(Exception):
    pass

from Functions import *

String1, String2 = setupFile(r"TesterFile.txt")

String1 = String1.lower()
String2 = String2.lower()
String_Index = 0
while(String1 != String2):

    #Check first Letter
    try:
        if String1[0] != String2[0]:
            index = SearchAhead(String1, String2, 0)
            if index > -1:
                String1 = String1[index:]
                print("Removed front letter")
            else:
                raise NoSimularLetter
    except NoSimularLetter:
        if String1[0] != String2[0]:
            index = SearchAhead(String2, String1, 0)
            if index > -1:
                String1 = String2[0:index] + String1
                print("Added Front letters")
            else:
                raise NoSimularLetter

    try:
        if String1[String_Index] == String2[String_Index]:
            print("All good here moving on")
            String_Index += 1
        else:
            raise ValuesNotTheSame
    except IndexError:
        print("fixing end")
        # if we get an index error on this if statement
        # then we know we need to handle the end of the word
        if len(String1) > len(String2):
            #Take off the end of string 1
            String1 = String1[:String_Index]
        else:
            #Tack on the end of String 2
            String1 = String1 + String2[String_Index:]
    except ValuesNotTheSame:
        print("Got:", String1[String_Index], "was expecting", String2[String_Index])
        # This is a slightly more advanced letter deleting algorith.
        # Will now delete a letter if multiple are added.
        try:
            index = SearchAhead(String1, String2, String_Index)
            if index > 0:
                print("Deleting a letter")
                String1 = deleteALetter(String1, index -1)
                print(String1)
                continue #continue as to increment the letters and re-run the algorithm
        except IndexError:
            print("String1 was too short. Continuing")

        # This is a slightly more advanced letter inserting algorith.
        # Will now insert a letter if multiple are missing.
        try:
            index = SearchAhead(String2, String1, String_Index)
            if index > 0:
                print("Inserting a letter")
                String1 = insertALetter(String1, String_Index-1, String2[String_Index])
                print(String1)
                continue
        except IndexError:
            print("String2 was too short. Continuing")

        #this is the standard letter replacement
        try:
            if String1[String_Index+1] == String2[String_Index + 1]:
                print("replacing a letter")
                String1 = changeALetter(String1, String_Index, String2[String_Index])
                print(String1)
                continue
        except IndexError:
            print("Not the same length")



print(String1)