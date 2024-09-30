def filter_below_threshold(input_list, threshold):
    # Filter elements from the list that are less than or equal to the threshold
    return [x for x in input_list if x <= threshold]

if __name__ == "__main__":
    # Example input
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    threshold = 6
    
    # Call the function and print the result
    result = filter_below_threshold(input_list, threshold)
    print(result)  # Expected output: [1, 2, 3, 4, 5, 6]
