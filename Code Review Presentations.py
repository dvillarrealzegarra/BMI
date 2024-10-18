# Question 4:
# Recursive functions v iterated functions run in different directions. Match the implementation with the direction.
# I.e. given [1,2,[3,4,[5,6]]]
# Does it go:
# 1,2,3,4,5,6 
# Or:
# 5,6,3,4,1,2

# Reply:
# Iterated functions 
# Outside->in
# Iterative functions, such as those using for or while loops, tend to process the elements in the order in which they appear, starting with the outermost elements and moving towards the innermost elements. This means that in a list such as [1, 2, [3, 4, [5, 6]]], an iterative loop will first process the elements at the outermost levels and then proceed to the innermost levels. 

# Reply: 
# Recursive functions 
# Inside->Out
# Recursive functions decompose the problem into smaller subproblems until a base problem is reached, and then solve these subproblems from the inside out as the recursive calls are solved. This means that, when processing nested structures, recursive functions usually solve the deepest elements first and then the outer elements.




# Question 5
# It is possible to write any recursive function with a while loop. 

# Reply: False 
# Because not all recursive functions can be easily implemented with a simple while loop.