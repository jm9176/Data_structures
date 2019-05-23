# Initialising the dictionary
dict={}

# Extracting the words from a text file
# and storing in a dictionary
with open('file.txt','r') as fp:
    for line in fp:
        word_list = line.split(' ')

        # removing the newline characters
        if '\n' in word_list[-1]:
            word_list[-1]=word_list[-1].replace('\n','')
  
        for word in word_list:
            # Ignoring the spaces
            if word != '':

                # Increment the counter
                # for each multiple occurrence
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1

    # Finding the word with maximum repetition
    temp_val = 0

    for var in dict:
        if dict[var] > temp_val:
            temp_val = dict[var]
            word = var
            
    print('The word with {} (max) repetition is dict[{}]'.format(temp_val, word))
