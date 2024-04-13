def check_password_strength(password):
    upper_char = False
    lower_char = False
    special_char = False
    digit_char = False
    special_char_list = ['!', '@', '#', '$', '%']
    if len(password) < 8:
        return False

    for letter in password:
        # check for Upper character in password
        if letter.isupper():
            upper_char = True
        # check for lower character in password
        if letter.islower():
            lower_char = True
        # check for digit i password
        if letter.isdigit():
            digit_char = True
        # check for special character in password
        if letter in special_char_list:
            special_char = True
    # check if password contain an upper character, lower character, digit and special character
    if upper_char and lower_char and special_char and digit_char:
        return True
    else:
        return False


if __name__ == "__main__":
    # Prompt the user to enter their password
    user_password = input("Please enter your password: ")

    # check password strength
    password_response = check_password_strength(user_password)

    # give feedback to user for entered password
    if password_response:
        print("The entered password is strong")
    else:
        print("Please enter a strong Password")
