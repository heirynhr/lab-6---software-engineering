
def encode(user_password):
    encoded_password = ""
    # for every character in the orginal password
    for character in user_password:
        # make each character an integer
        char = int(character)
        # if it is 9 change it so when it adds 3 it fits the structure
        if char == 9:
            char = -1
        else:
            # otherwise just add 3 to every number
            char += 3
        # make every character into a string again and make it into the password
        encoded_password += str(char)
    return encoded_password

def decode(encoded_password):

def menu():
    print("Menu \n -------------")
    print("1. Encode \n2. Decode \n3. Quit")
    # menu
def main():
    user_continues = True
    while user_continues == True:
        menu()
        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            user_password = input("Please enter your password to encode: ")
            encoded_password = encode(user_password)
            print("Your password has been encoded and stored!")

        if user_option == 2:
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}')
        if user_option == 3:
            user_continues = False

if __name__ == '__main__':
    main()