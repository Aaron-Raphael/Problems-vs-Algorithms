def rotated_array_search(input_list, number):
    """
    Find the index by searcupper_indng in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    lower_ind = 0
    upper_ind = len(input_list) - 1
    
    while lower_ind <= upper_ind:

        mid_ind = (lower_ind + upper_ind)//2
        
        # Check if the mid_index_value = number
        if input_list[mid_ind] == number:
            return mid_ind
        
        # Case 1: lower_index_value <= mid_index_value
        if input_list[lower_ind] <= input_list[mid_ind]:

            # lower_index_value <= number < mid_index_value
            if input_list[lower_ind] <= number  and  number < input_list[mid_ind]:
                upper_ind = mid_ind - 1
            else:
                lower_ind = mid_ind + 1
        
        # Case 2: mid_index_value < upper_index_value
        elif input_list[mid_ind] < input_list[upper_ind]:

            # mid_index_value < number <= upper_index_value
            if input_list[mid_ind] < number and number <= input_list[upper_ind]:
                lower_ind = mid_ind + 1 
            else:
                upper_ind = mid_ind - 1

    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# egde test 1  empyt string
test_function([[], 1])
# Pass

# egde test 2  large list
test_list=[i for i in range (1011,10000)]+[i for i in range (0,1011)]
test_function([test_list, 6])
# Pass

# egde test 3  large list with negative numbers
test_list=[i for i in range (1011,10000)]+[i for i in range (-1000,1011)]
test_function([test_list, -60])
# Pass