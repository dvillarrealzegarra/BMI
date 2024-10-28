# 1. Import numpy as np and print the version number. (5 Points)
import numpy as np
print("NumPy version:", np.__version__)




# 2. Create a 1D array of numbers from 0 to 9. Desired output:
#> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
#(10 Points)
array_1d = np.arange(10)
print("array:", array_1d)




# 3. Import a dataset with numbers and texts keeping the text intact in python numpy. Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data (20 Points)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# Load the dataset while keeping the text
data = np.genfromtxt(url, delimiter=',', dtype=None, encoding='utf-8')
# Show the loaded dataset
print(data)




# 4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset. Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data (20 Points)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# Load the dataset while keeping the text
data = np.genfromtxt(url, delimiter=',', dtype=None, encoding='utf-8')
# Select the fourth column (petal width), skipping any rows with missing values
try:
    # Convert the fourth column to float values
    petal_width_column = np.array([float(row[3]) for row in data if row[3] != ''])
    
    # Find the position of the first occurrence of a value greater than 1.0
    position = np.argmax(petal_width_column > 1.0)
    
    # Show the position
    print("Question 4:", position)
except Exception as e:
    print("An error occurred:", e)





# 5. From the array a, replace all values greater than 30 to 30 and less than 10 to 10.
# Input:
np.random.seed(100)
a = np.random.uniform(1,50, 20)

# Replace values greater than 30 with 30 and values less than 10 with 10
a = np.where(a > 30, 30, a)  # Replaces values greater than 30 with 30
a = np.where(a < 10, 10, a)  # Replace values less than 10 with 10

# Mostrar el array modificado
print("Question 5:", a)