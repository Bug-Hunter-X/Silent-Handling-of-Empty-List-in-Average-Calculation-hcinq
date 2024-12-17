# Silent Handling of Empty List in Average Calculation

This repository demonstrates a subtle bug in Python code that silently handles an empty list when calculating the average.  The bug is in the `calculate_average` function. The function should raise an exception or return a special value indicating an error for empty list instead of returning 0.

The `bug.py` file contains the code with the bug.  The `bugSolution.py` file demonstrates how to improve the code to handle the situation more robustly. The improved code raises a ValueError when an empty list is provided. This is generally a more appropriate approach for error handling as it explicitly signals that the input is invalid. 
