# Resources used during this assignment

*  https://www.geeksforgeeks.org/print-colors-python-terminal/
    Experimentation with coloring output for easier reading.
*  https://rollbar.com/blog/python-catching-multiple-exceptions/
    Refresh on the use of try excepts
*  Author, Homework1 Functions.py, used the SetupFile function

# Problems

While the initial sudo code for the problems seem to have worked. 
The code did not due to multiple issues. 

Indexing
> As the code runs through the word, String 1 is constantly changing size so one of
> the biggest problems I encountered was indexing outside the string. Try excepts 
> were my solution. I was able to write code that attempted to check if a change
> needed to be made and if indexed outside, the Indexing error would be raised and 
> the code would attempt the next modification.
 
No simular letters
> I chose to design mine to look forward in the code to see if there are 
> any letters I could use to make the final word. I did not program a back-up of what
> to do if no letter was found as you might actualy need to delete or change instead
> of insert. So I wrote the brute force path. If no other modification paths are valid
> the code justs replaces the current letter with the corresponding letter in String2

Debugging and infinite loops
> I had a lot of issues throughout the program with indexing. 
> Sometimes the issue was passing the wrong index into the function, sometimes
> the issue was inserting or deleting the wrong index. Debugging was more an effort
> of spotting the issue wrather than fixing the issue.

Searching the sorted word
> The search ahead function searches for the entire word for a match to the next letter.
> This also searched through the beginning of the word. 
> 
> One solution was to just delete the beginning of the word. SIDE EFFECT: The index where
> the letter was found would be incorrect.
> 
> Solution two was to replace the letters in the sorted half of the word with a symbol.
> SIDE EFFECT: that symbol would not be able to be used in a word.
> 
> Solution three would be to start at the index and go to the ending. NO SIDE EFFECTS.
> 
> I chose solution two and accepted the side effect because when debugging Its very clear
> what character the function was working on. In future iterations you might want
> to use solution 3.

# Notes

When designing this code I started with just trying to make simple changes to a word.
After I moved on to trying to make the words more complicated. I cannot check every
word to every word at this moment so this code most defiantly has errors. Although
I believe the code work for most words.

I made the executive decision early on to break this problem up into sections. Begging
middle end. The beginning simply refers to the first letter. Middle refers to all the
letters until the end of either String1 or String2. End refers to what do after 
one end has been reached.

I wanted to add color to the output for legibility purposes and experimentation, 
can be removed.