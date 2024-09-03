###############
#  Question 1 (Booleans)
# boolean True + boolean True - boolean False = ?
###############

# True is equivalent to 1; and False is equivalent to 0
# Perform the operation
question1 = True + True - False

# Print the result
print("The result of boolean True + boolean True - boolean False is:", question1)

# The expected output is 2, because:
# True + True - False = 1 + 1 - 0 = 2
# Reply: 2




###############
# Question 2 (Booleans 2),
###############

# logical_tracker has a value of “True”.
logical_tracker = True

# Perform a logical AND operation between logical_tracker and logical_tracker
# True & True results in True
logical_tracker = logical_tracker & logical_tracker

# Perform a subtraction operation first: logical_tracker - logical_tracker
# True is treated as 1, so 1 - 1 results in 0 (False)
# Then perform a logical OR operation between logical_tracker and False
# True | False results in True
logical_tracker = logical_tracker | (logical_tracker - logical_tracker)

# Print the final value of logical_tracker
# The value of logical_tracker is True
print("The final value of logical_tracker is:", logical_tracker)
# Reply: TRUE



###############
# Question 5 (Strings)
###############

# string has a value of "E. Coli"
string = "E. Coli"

# Access the character at index 2
# Remember that string indices in Python start from 0
# Index 2 corresponds to the third character in the string
question5 = string[2]

# The value is a space or " ".
print("The character at index 2 in the string is:", question5)
# Reply: " "





###############
# Question 6 (Strings 2)
# Oh no! My string has a typo!
#string = "I Bove python"
# No worries though. I'll just fix that.
# string[2]="L"
###############


# string with the typo
string = "I Bove python"

# You cannot correct the error by changing the character at index 2, since strings are immutable in Python. Therefore, it will generate the following “TypeError” error.
# string[2] = “L”

# To fix the string, you need to create a new string with the correction. 
# Answer: No, it won't work at all.
# Reply: No it won't work at all.









###############
# Question 7
# Jack has been prescribed 5 medications, write a variable named "Medication", and store in it the number of medications he has. Print the type of the variable ''Medication". Submit your code either here as a text entry, or on your GitHub page in a new repository and past the link here. We encourage you to use GitHub. Don't forget to add comments to your code.
###############



# Reply:
# Medication: number of medications Jack has been prescribed
Medication = 5  

# Print of "Medication"
print(type(Medication))

#  Print with explanation about the variable type of “Medication”.
print("The type of the variable 'Medication' is:", type(Medication))







###############
# Question 8
# Susan has a weight of 60 kilograms and a height of 1.58 meters. Write Code to Calculate and Print Susan’s Body Mass Index as float. Note: Body Mass Index is a person’s weight in kilograms divided by the square of height in meters. Reference: https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.htmlLinks to an external site.. Submit your code either here as a text entry, or on your GitHub page in a new repository and past the link here. We encourage you to use GitHub. Don't forget to add comments to your code.
###############


# Reply:
# Susan's values
weight = 60
height = 1.58

# Susan's Body Mass Index
BMI = weight / (height ** 2)

# Print Susan's BMI as a float
print("Susan's Body Mass Index (BMI) is:", BMI)






###############
# Question 9 (Operators 2)
# Explain how the "+", addition operation works differently for integers and strings.
###############
#The addition operation "+" works differently for integers and strings in Python. 
#In the case of integer values, the “+” operator performs an arithmetic addition. For example:
question9_a = 3
question9_b = 3
print (question9_a+question9_b)


#In the case of strings, the "+" operator performs a concatenation of the strings. That is, it joins the two strings together. For example: 
question9_string1 = "Hello "
question9_string2 = "World "
question9_merge = question9_string1 + question9_string2

print(question9_merge) 
#"Hello World"










###############
# Question 10 (String 3)
# Type the output if the strings "7" and "3" are added.
###############

string1 = "7"
string2 = "3"

# Adds (concatenates) the strings
merge = string1 + string2

# Print the merge
print(merge)

# Print explained
print("The result of adding the strings '7' and '3' is:", merge)









