"""
Problem 2: Edit Distance Problem

Make an Algorithm to change one word to another by manipulating
the letter in a string.
You have 3 options:
Change a letter
insert a letter
delete a letter
"""


# making some unique errors for the use of this program
class NoSimularLetter(ValueError):
    pass


class ValuesNotTheSame(Exception):
    pass


from Functions import *

from colorama import Fore, Style
import time

String1, String2 = setupFile(r"TesterFile.txt")

String1 = String1.lower()
String2 = String2.lower()
String_Index = 0

# This algorithm will keep running untill the two strings are the same
while (String1 != String2):

    # Check first Letter
    try:
        # if there are extra letters in front of the word remove them.
        if String1[0] != String2[0]:
            index = SearchAhead(String1, String2, 0)
            if index > -1:
                String1 = String1[index:]
                print("Removed front letter")
            else:
                # There are no letters in string 1 that match string 2
                raise NoSimularLetter
    except NoSimularLetter:
        # if there are letters missing from string 1 add them
        if String1[0] != String2[0]:
            index = SearchAhead(String2, String1, 0)
            if index > -1:
                String1 = String2[0:index] + String1
                for i in range(0, len(String2[0:index])):
                    String1 = insertALetter(String1, i, String2[i])
            else:
                # if there is no simular starting letters replace the first letter
                String1 = changeALetter(String1, String_Index, String2[String_Index])
                # print(String1)
    # print("String1", String1, "String2", String2)

    try:
        # If the two letters are simular then the algorithm moves on
        if String1[String_Index] == String2[String_Index]:
            print(Fore.GREEN + "All good here moving on " + Style.RESET_ALL)
            String_Index += 1
        else:
            # Otherwise you need to make a change
            raise ValuesNotTheSame
    except IndexError:
        # if the try raised an Index error then it has reached the end of one of the strings
        # and now needs to fix the ending of the string
        print("fixing end")
        check, index = checkWordisSame(String1, String2, String_Index)
        if not check:
            # print("check Failed going back to", index, String1)
            String_Index = index - 1
            time.sleep(1)
            continue

        # if we get an index error on this if statement
        # then we know we need to handle the end of the word
        if len(String1) > len(String2):
            # Take off the end of string 1
            String1 = String1[:String_Index]
        else:
            # Tack on the end of String 2
            String1 = String1 + String2[String_Index:]
        print(String1)
    except ValuesNotTheSame:
        # Working in the middle of a string and trying to find if a letter should be deleted, changed, or inserted
        # print("Got:", String1[String_Index], "was expecting", String2[String_Index])
        # print(String_Index)
        # This is a slightly more advanced letter deleting algorith.
        # Will now delete a letter if multiple are added.
        try:
            index = SearchAhead(String1, String2, String_Index)
            if index > 0:
                String1 = deleteALetter(String1, String_Index)
                # print(String1)
                continue  # continue as to increment the letters and re-run the algorithm
        except IndexError:
            pass
            # print("String1 was too short. Continuing")

        # This is a slightly more advanced letter inserting algorith.
        # Will now insert a letter if multiple are missing.
        try:
            index = SearchAhead(String2, String1, String_Index)
            if index > 0:
                String1 = insertALetter(String1, String_Index, String2[String_Index])
                # print(String1)
                continue
        except IndexError:
            pass
            # print("String2 was too short. Continuing")

        # this is the standard letter replacement
        try:
            if String1[String_Index + 1] == String2[String_Index + 1]:
                String1 = changeALetter(String1, String_Index, String2[String_Index])
                # print(String1)
                continue
        except IndexError:
            pass
            # print("Not the same length")

        # if this part of the algorithm is reached then there was no logical step to manipulate
        # string1 so brute force change the letter to equal string 1
        # This only changes a single letter does not change the entire string.
        # Aka the helping hand function.
        print(Fore.RED + "There is no logical way forward" + Style.RESET_ALL)
        print("\t Engaging brute Force")
        String1 = changeALetter(String1, String_Index, String2[String_Index])
        # print(String1)

print(String1)
