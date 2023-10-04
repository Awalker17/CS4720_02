# Resourses used during this assignmnet

[Combinations Code](https://www.geeksforgeeks.org/python-program-to-find-all-the-combinations-in-the-list-with-the-given-condition)

> 

[Bokeh](https://docs.bokeh.org)

>I decided to go with Bokeh due to matplotlib having issues.
Would not install despite using two different systems, reinstalled python and pycharm.
Updated both to latest version.
 

# Problems 

- Changes to Bokeh for ploting to replace matplotlib.
- Redid Exhaustive search as it was not working as intended, ses combinations code.
- Timer, forced to add a wait time that is then subtracted off. This was due to the 
    timer randomly truncating to 0 seconds. Adding .1 then subtracting it off seems to have
    fixed this issue.
- Chose to include a read from file option for debugging and testing.
    > To use this mode change `Max_weight, Objects = NumbGenerator(i)` in problem3.p to `Max_weight, Objects = setupFile(file_name, num_Items)`
    
    the File should be in the format
    ```
  int(Max_Weight)
  int(Weight) int(Value)
  int(Weight) int(Value)
  .
  v
  ```

# Notes

Logging disable and enable the logging print out by commenting out the logging.disable() line

FunctionTesting.py is used to test functions. Feel free to delete or add anycode you want as needed.
  