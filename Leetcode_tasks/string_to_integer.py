def myAtoi(s: str) -> int:
    """
    This function reads source string and converts into integer number, which are hidden in the string
    :param s: some string contains characters (whitespaces, letters, numbers and characters (including '+' and '-')
    :return: the first integer is contained in the string (both positive and negative) or 0 if there is no number
    """
    result_number = ''  # create string for recording digits
    characters = ''  # to print negative number define string for character '-'
                    # character '+' or no character means positive number
    ind = 0  # the first element of the string
    # let's run to the string
    while ind < len(s):
        # all whitespaces at the beginning of the string are ignored
        if s[ind].isspace():
            ind += 1  # move on to the next element
        else:
            break  # we passed all leading whitespaces
    # the next symbol must be '-', '+' or digit
    k = ind + 1  # '-' or '+' must be alone. The next character should be digit
    while ind < k and ind < len(s):  # if we reached to the end we can't look next element
        if s[ind] == '-' or s[ind] == '+':
            characters += s[ind]  # add the element to 'characters' variable
            ind += 1  # move to next character
        else:
            break  # if current symbol is not '-' or '+' go out the cycle
    # make sure the current element is digit and write to the result if it is true
    while ind < len(s):
        if s[ind].isdigit():
            result_number += s[ind]  # add digit to the 'result_number' variable
            ind += 1  # move to next character
        else:
            break  # if current symbol is not digit break the cycle
    # we got some string containing number (the string maybe empty)
    # variable 'characters' describes number's type
    try:
        result_number = int(result_number)  # transform resulting string into number
        if characters == '-':
            result_number = -result_number  # negative number has character '-'
            # number must be in range [-2^31, 2^31 - 1]
            if result_number < -2 ** 31:
                return -2 ** 31  # else if number is less than -2^31 return -2^31
            return result_number
        # characters == '+' or '' means the number is positive
        else:
            # number must be in range [-2^31, 2^31 - 1]
            if result_number > 2 ** 31 - 1:
                return 2 ** 31 - 1  # else if number is more than 2^31 - 1 return 2^31 - 1
            return result_number
    # empty string can't be converted to integer
    # empty resulting string means there are no numbers in the string
    except ValueError:
        return 0  # if resulting string is empty return 0
