def inner_plus(input_list):
    current_list = input_list
    
    # While loop to find the innermost list
    while any(isinstance(i, list) for i in current_list):
        for item in current_list:
            if isinstance(item, list):
                current_list = item
                break
    
    # Add 1 to each element in the innermost list
    return [x + 1 for x in current_list]

if __name__ == "__main__":
    # Example input
    input_list = [1, 2, 3, 4, [5, 6, 7, [8, 9]]]
    
    # Call the function and print the result
    result = inner_plus(input_list)
    print(result)  # Output will be [9, 10]
