'''
Given a string of round, curly and square open and
closing brackets return whether the brackets are balanced.
For. e.g. if the given string is "([])[]({})", it should
return true. If the given string is "([)]" or "((()",
then it should return false.
'''
def str_chk(inp_str):

    # creating a dictionary for a closed bracket
    # corresponding to each open bracket
    dict_bkt = {'(':')',
                '{':'}',
                '[':']'}

    # Closed list acting as a stack to check for
    # next element to each open bracket or adding
    # a closed bracket in case of an open bracket
    closed_list = []

    # Initial check on the input, such that the string
    # has not length of 1 or the first element is an open
    # bracket
    if inp_str == '':
        return True
    elif len(inp_str) == 1 or inp_str[0] in dict_bkt.values():
        return False

    # Iterating over the string to do further processing
    for i in range(len(inp_str)):
        if inp_str[i] in dict_bkt.keys():
            closed_list.insert(0,dict_bkt[inp_str[i]])
        elif inp_str[i] == closed_list[0]:
            closed_list.pop(0)
        else:
            continue

    # Condition check on the closed list, such that if the
    # loop iteration is complete if the closed list is not
    # empty then return False.
    if not closed_list:
        return True
    else:
        return False


# Taking the input from the user
inp_str = input("Enter the bracket string: ")
print(str_chk(inp_str))
