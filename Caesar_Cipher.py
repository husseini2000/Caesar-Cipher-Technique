# Reference
# https://likegeeks.com/python-caesar-cipher/
"""
import string

# encryption-decryption algorithm using a lookup table
# it's reducing the computation power
# notice that we make encryption-decryption for lowercase
# but we can improve that by put the whole character set using this line
# character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + " "+ string.punctuation

def cipher_cipher_using_lookup(text,  key, characters = string.ascii_lowercase, decrypt=False):

    if key < 0:

        print("key cannot be negative")

        return None

    n = len(characters)

    if decrypt==True:

        key = n - key

    table = str.maketrans(characters, characters[key:]+characters[:key])

    translated_text = text.translate(table)

    return translated_text
"""

"""
import string

# the result of a left shift in encryption and a right shift in the decryption process

def cipher_cipher_using_lookup(text, key, characters = string.ascii_lowercase, decrypt=False, shift_type="right"):

    if key < 0:

        print("key cannot be negative")

        return None

    n = len(characters)

    if decrypt==True:

        key = n - key

    if shift_type=="left":

        # if left shift is desired, we simply inverse they sign of the key
        key = -key

    table = str.maketrans(characters, characters[key:]+characters[:key])

    translated_text = text.translate(table)

    return translated_text
"""


def get_message():
    """ Get data from the user and
        check on apart of this data if it's valid """
    msg = input("Enter your message: ")
    msg = msg.lower()
    input_ok = False
    num = 0
    while not input_ok:
        num = int(input("Enter a number (1 - 26): "))
        if num in range(1, 27):
            input_ok = True
        else:
            print('Invalid Input (must be 1 - 26)')
    print('-----------------')
    return msg, num


def encode_message(msg, shift_num):
    """ Encoding message by shift
        each character by specific number """
    new_word = ""
    for x in msg:
        # check if character is an uppercase letter
        if x.isupper():
            # find the position in 0-25
            x_index = ord(x) - ord("A")

            # shift the current character by shift_num positions
            x_shifted = (x_index + shift_num) % 26 + ord("A")

            new_character = chr(x_shifted)

            # append to encrypted string
            new_word += new_character
        elif x.islower():  # check if its a lowercase character

            # subtract the unicode of 'a' to get index in [0-25) range
            x_index = ord(x) - ord('a')

            x_shifted = (x_index + shift_num) % 26 + ord('a')

            x_new = chr(x_shifted)

            new_word += x_new

        elif x.isdigit():

            # if it's a number,shift its actual value
            x_new = (int(x) + shift_num) % 10

            new_word += str(x_new)

        else:
            new_word += x
    print(new_word)
    print()


def decode_message(msg, shift_num):
    """ Decoding message by shift
        each character by specific number """
    new_word = ""
    for x in msg:
        # check if character is an uppercase letter
        if x.isupper():
            # find the position in 0-25
            x_index = ord(x) - ord("A")

            # shift the current character to left by shift_num positions to get its original position
            x_shifted = (x_index - shift_num) % 26 + ord("A")

            new_character = chr(x_shifted)

            # append to encrypted string
            new_word += new_character
        elif x.islower():  # check if its a lowercase character

            # subtract the unicode of 'a' to get index in [0-25) range
            x_index = ord(x) - ord('a')

            x_shifted = (x_index - shift_num) % 26 + ord('a')

            x_new = chr(x_shifted)

            new_word += x_new

        elif x.isdigit():

            # if it's a number,shift its actual value
            x_new = (int(x) - shift_num) % 10

            new_word += str(x_new)

        else:
            new_word += x
    print(new_word)
    print()


def get_operation_choice():
    """
        Show menu of operations user can select from them.
        Performs some verifications of the input."""
    input_ok = False
    user_selection = 0
    while not input_ok:
        print('Menu Options are:')
        print('\t1. Make a code')
        print('\t2. Decode a message')
        print('\t3. Quit')
        print('-----------------')
        user_selection = input('Please make a selection: ')
        if user_selection in ('1', '2', '3'):
            input_ok = True
        else:
            print('Invalid Input (must be 1 - 3)')
    print('-----------------')
    return user_selection


def main():
    """ Call specific operation for user,
        if the operation not exists print error message"""
    flag = False
    while not flag:
        menu_choice = get_operation_choice()
        if menu_choice == '1':
            message, num = get_message()
            encode_message(message, num)
        elif menu_choice == '2':
            message, num = get_message()
            decode_message(message, num)
        elif menu_choice == '3':
            flag = True
        else:
            print("Incorrect option!")
    print('=================')


main()
