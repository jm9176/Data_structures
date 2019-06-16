'''
Given a sequence of words and an integer line length k, return 
a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in 
each line. There should be at least one space between each word. 
Pad extra spaces when necessary so that each line has exactly length
k. Spaces should be distributed as equally as possible, with the 
extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the 
right-hand side with spaces. Each word is guaranteed not to be longer
than k.

For example, given the list of words ["the", "quick", "brown", "fox", 
"jumps", "over", "the", "lazy", "dog"] and k = 16, you should return 
the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

....................RAW APPROACH......................

'''

# Function returning the required string output, and takes an input 
# string and a required string length
def ret_sen(inp_str, sub_len):
    # list storing the sub strings of required length
    temp_len = 0
    temp_list = []
    list = []

    # Initial iteration storing the list of possible word index with 
    # minimum one added space and total no. of characters at the end
    # of the sub list. For e.g. if k = 10, then the output list
    # i.e. temp_list = [[inp_str[0],inp_str[1],8],...]
    for i in range(len(inp_str)):

        # Condition to check if the total length of words including the 
        # min. one space is more than the required length, then append 
        # the word to the temp_list and subtract the length of spaces.
        # Length per substring will be length of total num of characters 
        # combining the words in each sub list
        if temp_len + len(inp_str[i]) > sub_len:
            temp_len -= len(list)
            list.append(temp_len)
            temp_list.append(list)
            list = [inp_str[i]]
            temp_len = len(inp_str[i]) + len(' ')
        else:
            temp_len += len(inp_str[i]) + len(' ')
            list.append(inp_str[i])

    list.append(temp_len - len(list))
    temp_list.append(list)

    # List storing the desired output
    req_str = ''
    out_str = []

    # Performing iteration to count the no. of additional spaces required
    # for the desired output
    for i in range(len(temp_list)):
        spaces = sub_len - temp_list[i][-1]
        num_spaces = [0] * (len(temp_list[i]) - 2)

        # temporary variable used as an index while counting the num of 
        # spaces in line 57
        j = 0

        # If there is only one word then add the required spaces at the end
        if len(temp_list[i]) - 1 == 1:
            req_str += temp_list[i][0] + (' ' * spaces)

        else:
            # Iterating over the no. of spaces required to create a list spaces
            # required after each word to add to temp_list

            while spaces != 0:
                num_spaces[j] += 1
                j += 1
                spaces -= 1

                # Iterating over the same loop, in case the no. of spaces are more 
                # than 2, For e.g, if spaces are 5 and no. of words fitting our 
                # requirement are 3 then the out will return num_spaces = [3,2]
                if j == len(temp_list[i]) - 2:
                    j = 0

            # Creating a new string by adding the counted spaces with each word in
            # the temp_list
            for k in range(len(temp_list[i]) - 1):
                if k < len(num_spaces):
                    req_str += temp_list[i][k] + (' ' * num_spaces[k])
                else:
                    req_str += temp_list[i][k]

        # Appending the newly formed string to the output list
        out_str.append(req_str)
        req_str = ''

    return out_str


# Taking the raw input string from the user and the length of required sub-string
inp_str = ["the", "quick", "brown", "fox",
           "jumps", "over", "the", "lazy", "dog"]

sub_len = int(input("Enter the required str length: "))
print(ret_sen(inp_str, sub_len))
