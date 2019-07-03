'''
Given a tree in form of a list, print out the tree structure

For e.g.

['a',['b', 'c', ['d', 'i'], 'e'], 'f', ['g', 'h', ['j', 'k', 'l', 'm']]]

REFERENCE:

https://stackoverflow.com/questions/30521991/python-recursively-printing-a-tree-from-a-list-structure

'''
# Function returning the structure of the given input
def ret_struct(inp_list, level):

    print('    '*(level-1) + '+---'*(level>0) + inp_list[0])

    # Iterating over the given input
    for var in inp_list[1:]:

        # to check if the next element is a list or a string
        if type(var) is list:
            ret_struct(var, level+1)
        else:
            print('    '*level + '+---' + var)
            
# Taking the input from the user
given_list = ['a',['b', 'c', ['d', 'i'], 'e'], 'f']
init_level = 0
ret_struct(given_list, init_level)
