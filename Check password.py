# The program checks the password strength

def check_password(password):
    count_digit = 0
    count_upper = 0
    count_special = 0

    for i in password:
        if i.isdigit():
            count_digit += 1
        if i.isupper():
            count_upper += 1
        if i in '!@#$%*':
            count_special += 1

    if len(password) >= 10 and count_digit >= 3 and count_upper >= 1 and count_special >= 1:
        print('Your password is good.')
    else:
        print('Your password is weak.')


print('Enter your password to check its strength: ')

checkpass = input()

check_password(checkpass)
