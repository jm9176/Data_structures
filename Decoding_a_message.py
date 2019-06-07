'''
Decoding a message where each numerical element
of the string corresponds to a alphabetical character
For e.g. 1->a, 2->b,..etc

if the input is '111',
then the output will be aaa, ak, ka

----REQUIRED OPTIMIZATION----
'''

# Decoding the message
def decode(message, k, decd_msg):

    # Condition to end the recursion in case
    # the value of k is more than the length
    # of the message
    if k >= len(message):
        print(decd_msg)
        return ''

    # Invalid input in case the message has a 0
    # at index 0
    if message[0] == '0' or message[k:k+2] == '00':
        raise ValueError("Input cannot have a 0 or 00")

    # Condition to check for single element
    if int(message[k]) >= 1 and int(message[k]) <= 9:
        decd_msg = decd_msg + chr(96 + int(message[k]))
        decode(message, k + 1, decd_msg)

    # Condition to check for combined element
    if int(message[k:k + 2]) >= 10 and int(message[k:k + 2]) <= 26:

        # Count variable to check if there is a character whose
        # integer value is greater than 10
        count = 0
        if k >= 2:
            for var in decd_msg[:k]:
                if ord(var) - 96 >= 9:
                    count += 1

            decd_msg = decd_msg[:k - count] + chr(96 + int(message[k:k + 2]))
        else:
            decd_msg = decd_msg[:k] + chr(96 + int(message[k:k + 2]))

        return decode(message, k + 2, decd_msg)

# Taking the input from the user
# Initializing the decoding function
# with the message and Initial index
message = '111111'
decd_msg = ''
initial_index = 0
decode(message, initial_index, decd_msg)

'''
Output of this input will be:
aaaaaa
aaaak
aaaka
aakaa
aakk
akaaa
akak
akka
kaaaa
kaak
kaka
kkaa
kkk
'''

