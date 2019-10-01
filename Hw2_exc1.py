'''
Created on Sun Feb 24 2019
@author: Sara Ghandehari
'''

import string

def password_chek(*passwords):
    """
    password_chek gets a list of password and returns the list of eligible passwords that meet these criteria:
    At least 1 letter between [a-z], At least 1 number between [0-9],
    At least 1 letter between [A-Z],
    At least 1 character from [$#@], Minimum length of transaction password: 6
    :param passwords:
    :return: the list of eligible passwords
    """
    lower_case = set(string.ascii_lowercase)
    upper_case = set(string.ascii_uppercase)
    digits = set(string.digits)
    special_chars = {'$', '#', '@'}
    eligile_passwords = []
    for password in passwords:
        if any(char in lower_case for char in password) and any(char in upper_case for char in password) and any(
                char in digits for char in password) and any(char in special_chars for char in password) and len(
            password) >= 6 and len(password) <= 12:
            eligile_passwords.append(password)
    if not eligile_passwords:
        return ('No password is eligile')
    return eligile_passwords


words = ['AB1g23@41', 'aFS1#drg', '2w3E*', '2We3345']
print(password_chek(*words))
