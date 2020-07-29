def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    # The variables min_value and max_value are set to first element of input list
    min_value , max_value = (ints[0] , ints[0])

    for value in ints:

        # Check value < min_value and updte min_value 
        if value < min_value:
            min_value = value

        # Check value >= max_value and updte max_value
        if value >= max_value:
            max_value = value

    return min_value, max_value

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

li = [i for i in range(-15 , -5)]  # a list containing -15 - -6
random.shuffle(li)

print ("Pass" if ((-15, -6) == get_min_max(li)) else "Fail")