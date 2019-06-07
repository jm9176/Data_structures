'''
Decoding a message where each numerical element
of the string corresponds to a alphabetical character
For e.g. 1->a, 2->b,..etc

if the input is '111',
then the output will be aaa, ak, ka

----REQUIRED OPTIMIZATION----
but works without errors
'''

msg = ''

# Decoding the message
def decd_msg(message, k):

    global msg

    # Condition to end the recursion in case
    # the value of k is more than the length
    # of the message
    if k >= len(message):
        print(msg)
        return ''

    # Condition to check for single element
    if int(message[k]) >= 1 and int(message[k]) <= 9:
        msg = msg + chr(96 + int(message[k]))
        decd_msg(message, k + 1)

    # Condition to check for combined element
    if int(message[k:k + 2]) >= 10 and int(message[k:k + 2]) <= 26:

        # Count variable to check if there is a character whose
        # integer value is greater than 10
        count = 0
        if k >= 2:
            for var in msg[:k]:
                if ord(var) - 96 >= 9:
                    count += 1

            msg = msg[:k - count] + chr(96 + int(message[k:k + 2]))
        else:
            msg = msg[:k] + chr(96 + int(message[k:k + 2]))

        return decd_msg(message, k + 2)

# Taking the input from the user
# Initializing the decoding function
# with the message and Initial index
message = '111111'
decd_msg(message, 0)
