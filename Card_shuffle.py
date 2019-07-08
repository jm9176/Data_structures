'''
Given a function that generates perfectly random numbers between 1
and k (inclusive), where k is an input, write a function that shuffles
a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is
equally likely.
'''
import random

# function returning the shuffle for the deck of cards
def ret_cardShuffle(inp_arr):

    # Iterating using the length of the input. If the list size is 2
    # then there will be 1 shuffle, if 3 then 2 and so on...
    # so the iteration will occur for N-1
    for i in range(len(inp_arr)-1):

        # Using Durstenfeld's method for the perfect random selection
        # of the num from the list. Using the num to swap with the end
        # element in the list. That's why randint(0,len(inp_arr)-2-i)
        # is used and using the swap later for the selection
        temp = random.randint(0,len(inp_arr)-2-i)
        inp_arr[temp], inp_arr[-1-i] = inp_arr[-1-i], inp_arr[temp]

    return inp_arr

# Taking the input from the user. Initializing the deck of 52 cards
# in the form of a list of 52 integers
given_inp = range(1,53)
print(ret_cardShuffle(given_inp))
