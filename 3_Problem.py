# Quick sort algorithm

def sort(items, begin_index, end_index):    
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1
    
    return pivot_index

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return
    
    pivot_index = sort(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)
    
def quicksort(items):
    sort_all(items, 0, len(items) - 1)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        print('Provide input list with length greater than 2')
        return input_list

    quicksort(input_list)

    num_1 = ''
    num_2 = ''

    for ind in range(len(input_list) - 1, -1, -2):
        num_1 += str(input_list[ind])

        if ind - 1 >= 0:
            num_2 += str(input_list[ind - 1])

    # Return the two numbers as list
    return [int(num_1), int(num_2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
# Pass

test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Pass

test_function([[], []])
# Provide input list with length greater than 2
# Pass

# edge case : large set and large numbers
test_function([[i for i in range(0,101)], [int("".join(map(str,range(100,-1,-2)))), int("".join(map(str,range(99,-1,-2))))]])
# Pass