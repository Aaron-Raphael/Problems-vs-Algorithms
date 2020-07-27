def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    try:
        number = int(number)
        # check for +ve integer
        print
        if number < 0:
            return None

        # sqrt of 0 is 0 & sqrt of 1 is 1
        if (number == 0) or (number == 1):
            return number

        upper_val = 0
        lower_val = number // 2

        while upper_val <= lower_val:
            mid_val = (lower_val + upper_val) // 2
            mid_square = mid_val ** 2

            if mid_square == number:
                return mid_val
            elif mid_square < number:
                upper_val = mid_val + 1
                result = mid_val
            else:
                lower_val = mid_val - 1

        return result

    except ValueError:
      print ("This is not a number. Please enter a valid number")


# Test cases

print ("Pass" if  (3 == sqrt(9)) else "Fail")
# Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")
# Pass

print ("Pass" if  (4 == sqrt(16)) else "Fail")
# Pass

print ("Pass" if  (1 == sqrt(1)) else "Fail")
# Pass

print ("Pass" if  (5 == sqrt(27)) else "Fail")
# Pass

print ("Pass" if  (5 == sqrt('27')) else "Fail")
# Pass

print ("Pass" if  (None == sqrt('a')) else "Fail")
# This is not a number. Please enter a valid number
# Pass