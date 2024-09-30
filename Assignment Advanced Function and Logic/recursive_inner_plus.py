def inner_plus_recursive(input_list):
    # Base case: if there are no more lists, we are at the innermost list
    for item in input_list:
        if isinstance(item, list):
            return inner_plus_recursive(item)
    
    # Add 1 to each element in the innermost list
    return [x + 1 for x in input_list]

if __name__ == "__main__":
    # Example input
    input_list = [1, 2, 3, 4, [5, 6, 7, [8, 9]]]
    
    # Call the function and print the result
    result = inner_plus_recursive(input_list)
    print(result)  # Expected output: [9, 10]
