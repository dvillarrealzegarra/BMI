# -*- coding: utf-8 -*-
"""
#%% the humble print statement
'''
# 1.a Using the print() function only, get the wrong_add_function to print out where it is making a mistake, given the expected output for ex, "we are making an error in the loop", which you would put near the loop. Structure the print() statement to show what the expected output ought to be via f-strings: ie "The correct answer is supposed to be: [...]".
# 1.b Then, changing as little as possible, modify the function, using the same general structure to output the correct answer. Call this new function correct_add_function() 
'''



def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]

   whereas the expected correct answer is, [2,3,4]

   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the ontents of arg2 added to it.

   '''
   arg1_index = 0
   expected_output = [a + b for a, b in zip(arg1, arg2)]
   while arg1_index < len(arg1):
      arg_2_sum = 0
      # Print statement to indicate where the error occurs and what the correct answer should be
      print(f"We are making an error in the loop at index {arg1_index}.")
      print(f"The correct answer is supposed to be: {expected_output}")
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index] + i for i in arg2])
      arg1[arg1_index] = arg_2_sum
      arg1_index += 1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]


# Run the modified function with print statements to debug
wrong_add_function(arg1, arg2)

# Correct version of the function (1.b)
def correct_add_function(arg1, arg2):
    '''
    Corrected version of the function.
    Takes in two lists of integers and adds each element of arg2 to the corresponding element of arg1.
    '''
    # Using a for loop to iterate over the indices and modify arg1 accordingly
    for i in range(len(arg1)):
        arg1[i] += arg2[i]
    return arg1

arg1 = [1, 2, 3]
arg2 = [1, 1, 1]

# Run the corrected function
correct_output = correct_add_function(arg1, arg2)
print(f"The correct output is: {correct_output}")






#%% try, except
'''
# 2.a Update the numeric section of the function with your changes from 1 for both 2.b and 2.c

# 2.b Without modifying the string section code itself or the input directly, write a try, except block that catches the issue with the input below and returns an error message to the user, in case users give invalid inputs, (for example an input of ["5","2", 5]): "Your input argument [1 or 2] at element [n] is not of the expected type. Please change this and rerun. Name this function exception_add_function()

# 2.c Without modifying the string section code itself or the input directly, write a try, except block that catches the issue with the input below and gets it to process via the string section. IE, do not, outside the function, change the values of arg_str_1 or arg_str_2. Name this function correction_add_function(), i.e you will not be updating the wrong_add_function, you will simply handle the error of wrong inputs in a seperate function, you want the wrong_add_function to output its current result you are only bolstering the function for edge cases.
'''

# Adding print statements to the wrong_add_function to identify the error and show the expected output

def wrong_add_function(arg1, arg2):
    arg1_index = 0
    expected_output = [a + b for a, b in zip(arg1, arg2)]
    while arg1_index < len(arg1):
        arg_2_sum = 0
        # Print statement to indicate where the error occurs and what the correct answer should be
        print(f"We are making an error in the loop at index {arg1_index}.")
        print(f"The correct answer is supposed to be: {expected_output}")
        arg_2_sum = arg1[arg1_index] + sum(arg2)  # Correcting the logic here to add all elements of arg2 to each element of arg1
        arg1[arg1_index] = arg_2_sum
        arg1_index += 1
    return arg1

arg1 = [1, 2, 3]
arg2 = [1, 1, 1]

# Run the modified function with print statements to debug
wrong_output = wrong_add_function(arg1[:], arg2)
print(f"Wrong function output: {wrong_output}")

# Correct version of the function (1.b)
def correct_add_function(arg1, arg2):
    # Using a for loop to iterate over the indices and modify arg1 accordingly
    for i in range(len(arg1)):
        arg1[i] += arg2[i]
    return arg1

arg1 = [1, 2, 3]
arg2 = [1, 1, 1]

# Run the corrected function
correct_output = correct_add_function(arg1[:], arg2)
print(f"The correct output is: {correct_output}")

# 2.a Update the numeric section of the function with changes
# Updated version of wrong_add_function to use correct logic for numeric addition
def wrong_add_function(arg1, arg2):
    '''
    The function takes in two lists of integers, then it adds all elements of arg2 to each item of arg1.
    
    Example:
       > wrong_add_function([1,2,3],[1,1,1])
       > [4,5,6]
    
    If the lists are lists of strings, concatenate them
    Example:
       > wrong_add_function(['1','2','3'],['1','1','1'])
       > ['1111','2111','3111']
    Parameters
    ----------
    arg1 : list
       list of integers.
    arg2 : list
       list of integers.

    Returns
    -------
    arg1 : list
       Elements of arg1, with each element having had the contents of 
       arg2 added to it.

    '''
    # Numeric section
    if all(isinstance(i, int) for i in arg1) and all(isinstance(i, int) for i in arg2):
        for i in range(len(arg1)):
            arg1[i] += arg2[i]
        return arg1
    # String section
    elif all(isinstance(i, str) for i in arg1) and all(isinstance(i, str) for i in arg2):
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = ''.join(arg2)
            arg1[arg1_index] = arg1[arg1_index] + arg_2_sum
            arg1_index += 1
        return arg1
    else:
        raise TypeError("Input lists must be either all integers or all strings.")

# 2.b exception_add_function with try-except block to handle invalid inputs def exception_add_function(arg1, arg2):
    try:
        # Attempt to run wrong_add_function
        return wrong_add_function(arg1, arg2)
    except TypeError as e:
        # Catch type errors and provide a meaningful message
        print(e)
        for i, val in enumerate(arg1):
            if not isinstance(val, (int, str)):
                print(f"Your input argument 1 at element {i} is not of the expected type. Please change this and rerun.")
        for i, val in enumerate(arg2):
            if not isinstance(val, (int, str)):
                print(f"Your input argument 2 at element {i} is not of the expected type. Please change this and rerun.")
        return None

arg_str_1 = ['1', '2', '3']
arg_str_2 = ['1', '1', 1]

# Run the exception function with invalid inputs
print("Running exception_add_function:")
exception_add_function(arg_str_1, arg_str_2)

# 2.c correction_add_function to handle and correct invalid inputs
def correction_add_function(arg1, arg2):
    try:
        # Attempt to run wrong_add_function
        return wrong_add_function(arg1, arg2)
    except TypeError:
        # If a TypeError occurs, convert all elements to strings and rerun
        print("Correcting input types to strings...")
        arg1 = [str(i) for i in arg1]
        arg2 = [str(i) for i in arg2]
        return wrong_add_function(arg1, arg2)

# Run the correction function with invalid inputs
print("Running correction_add_function:")
corrected_output = correction_add_function(arg_str_1, arg_str_2)
print(f"The corrected output is: {corrected_output}")




# %%
