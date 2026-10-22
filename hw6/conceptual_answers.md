# Conceptual Questions
### Question 1: What is refactoring? Give three examples of refactoring techniques.
Refactoring is the restructuring of working code for better clarity without changing it's functionality. You can change variable names to be more intuitive, re-express your algorithm implementation in a simpler/clearer way, or alter the function signature.

### Question 2: In a data science project, why does code naturally go through “phases” of messiness?
You might not know what is the best approach to finding the solution so you try different methods to see what works best. After finding the one that seems promising, the code is most likely messy as you were trying to quickly implement your idea without much planning. 

### Question 3: What are three techniques for creating more modular code?
1. If you find yourself copying and pasting the same snippet of code, it's a good indication that piece of code should be turn to a function that works for all your cases.
2. If a function is really long and/or difficult to read, consider splitting into multiple functions with intuitive names to make the main function compact and easy to understand.
3.  A function should only do exactly 1 task. If an algorithm has multiple steps to it, consider making multiple functions to do each step then have your main algorithm function call those helper functions.
