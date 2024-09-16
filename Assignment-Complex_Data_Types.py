print("Assignment 3")

#######################################
# Problem 1: Lists, Sets and Coercion
#######################################

# 1.a Create a list of integers no fewer than 10 items from 0 to 9.
one_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("one_a = " + str(one_a)) 

# 1.b Add 3 to the 5th indexed element
one_b = one_a.copy()  
one_b[5] = one_b[5] + 3
print("one_b = " + str(one_b))

# 1.c Coerce all elements in the list to floats using list comprehension
one_c = [float(i) for i in one_a]
print("one_c = " + str(one_c))

# 1.d Coerce the list to a set
one_d = set(one_a)
print("one_d = " + str(one_d))

# 1.e Using a method, append int 10 to the set
one_e = set(one_a)
one_e.add(10)
print("one_e = " + str(one_e))

# 1.f Using a method, pop an item from the set
one_f = set(one_a)
one_f_popped_item = one_f.pop()
print("one_f = " + str(one_f))

# 1.g Using a length counting function, count the number of items in the set
one_g = len(set(one_a))
print("one_g = " + str(one_g))

# 1.h Check if the number of items in the set is the same as the number of items in the list
one_h = len(set(one_a)) == len(one_a) # set =/= list
print("one_f = " + str(one_h ))

# 1.i Coerce the set to a list and use the "+" operator to combine the list with the list from 1.a
one_i = list(one_f) + one_a
print("one_i = " + str(one_i))

# 1.j Coerce 1.i to a set
one_j = set(one_i)
print("one_j = " + str(one_j))

# 1.k Count the number of elements in the 1.j
one_k = len(one_j)
print("one_k = " + str(one_k))








#######################################
# Problem 2: Dictionary woes
#######################################

two_patient_dictionary_kinoko = {
    "name": "Kinoko",
    "year": 2021
}

two_patient_dictionary_dango = {
    "name": "Dango",
    "year": 2019
}

two_patient_dictionary_mochi = {
    "name": "Mochi",
    "year": 2020
}

# 2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
# two_a, ensure the key names are the same as the dictionary names.
two_a = {
    "kinoko": two_patient_dictionary_kinoko,
    "dango": two_patient_dictionary_dango,
    "mochi": two_patient_dictionary_mochi
}
print("two_a = " + str(two_a))

# 2.b Using keys, retrieve the Dango's name from 2.a
two_b = two_a["dango"]["name"]
print("two_b = " + two_b)

# 2.c Using keys, update the value of Mochi's year to 2018. This should not be a variable
# and should simply update 2.a.
two_a["mochi"]["year"] = 2018
print("two_c = " + str(two_a["mochi"]))

# 2.d Manually create a dictionary that has a single level and contains each patient as the key
# and the year as the value. Set Mochi's year to 2019.
# Note: Are Dango and Mochi patients? XD
two_d = {
    "Kinoko": 2021,
    "Dango": 2019,
    "Mochi": 2019  # Manually set to 2019
}
print("two_d = " + str(two_d))

# 2.e Coerce the keys of 2.d into a list
two_e = list(two_d.keys())
print("two_e  = " + str(two_e))

# 2.f Coerce the values of 2.d into a list
two_f = list(two_d.values())
print("two_f = " + str(two_f))

# 2.g Use the zip function to combine 2.e and 2.f into a dictionary again
two_g = dict(zip(two_e, two_f))
print("two_g = " + str(two_g))












#######################################
# Problem 3: Set combinations
#######################################

three_setA = {1, 2, 3, 4, 5}
three_setB = {2, 3, 4, 5, 6}
three_setC = {3, 5, 7, 9}
three_setD = {2, 4, 6, 8}
three_setE = {1, 2, 3, 4}

# 3.a Is set E a subset of set A
three_a = three_setE.issubset(three_setA)
print("three_a = Is set E a subset of set A?: " + str(three_a))

# 3.b Is set E a strict subset of set A (proper subset)
three_b = three_setE < three_setA
print("three_b = Is set E a strict subset of set A?: " + str(three_b))

# 3.c Create a set that is the intersection of set A and set B
three_c = three_setA.intersection(three_setB)
print("three_c = Intersection of set A and set B: " + str(three_c))

# 3.d Create a set that is the union of sets C, D and E
three_d = three_setC.union(three_setD).union(three_setE)
print("three_d = Union of sets C, D, and E: " + str(three_d))

# 3.e Add 9 to the set
three_d.add(9)
print("three_e = Set after adding 9: " + str(three_d))

# Lista one_a (asumimos que es la siguiente según los problemas anteriores)
#one_a = [0, 1, 2, 3, 4, 8, 6, 7, 8, 9]

# 3.f Using == compare this set to the list in one_a
three_f = (three_d == set(one_a))
print("three_f = Is the set equal to one_a?: " + str(three_f))

# 3.g Explain why they are not the same. 
# What would you need to change if you wanted this to be True?
# one_a to a set and ensure the elements match exactly to make this comparison True.
print("three_g = They are not the same because the list one_a has a 0, which is not in the set.")













#######################################
# Problem 4: Changing variable types
#######################################


# 4.a Create a variable of type int with the value of 8
four_a = 8
print("four_a = " + str(four_a))

# 4.b Create an empty list
four_b = []
print("four_b = " + str(four_b))

# 4.c Using type(), add the type of 4.a to this list
four_b.append(type(four_a))
print("four_c = "+ str(four_b))

# 4.d Add 0.39 to 4.c
four_d = 0.39
four_b.append(four_d)
print("four_d = " + str(four_b))

# 4.e Append the type of 0.39 to the list
four_b.append(type(four_d))
print("four_e = " + str(four_b))

# 4.f Exponentiate to the -10, i.e., 4.d^-10, round it to no decimal places, and append to list
four_f = round(four_d ** -10)
four_b.append(four_f)
print("four_f = " + str(four_b))

# 4.g Append the type of the result from 4.f to the list
four_b.append(type(four_f))
print("four_g = " + str(four_b))

















#######################################
# Problem 5: More variable type changes
#######################################

# Continue from where you left off in Problem 4 (four_b)

# 5.a Manually create a dictionary where the values are items in the list from where we left in problem 4,
# and the keys should be their index in the list. Print the dictionary.
five_a = {index: value for index, value in enumerate(four_b)}
print("five_a = Dictionary created from list: " + str(five_a))

# 5.b Add 300 and coerce it into a string
five_b = str(300)
print("five_b =: " + five_b)

# 5.c Append the type to the list
four_b.append(type(five_b))
print("five_c = " + str(four_b))

# 5.d Slice the string up to the 2nd element
five_d = five_b[:2]
print("five_d = Sliced string up to 2nd element = " + five_d)

# 5.e Append the type to the list
four_b.append(type(five_d))
print("five_e = " + str(four_b))

# 5.f Use list comprehension to convert this into a new list of integers
five_f = [int(char) for char in five_d] 
print("five_f = New list of integers: " + str(five_f))

# 5.g Append the type of this new list to the list
four_b.append(type(five_f))
print("five_g = " + str(four_b)) # Type of new list of integers appended to list

# 5.h Append the type of three_setA to the list
four_b.append(type(three_setA))
print("five_h = " + str(four_b)) # Type of three_setA appended to list












