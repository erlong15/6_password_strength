import re
import getpass


def read_worst_passwords():
    blacklist = []
    try:
        with open('500-worst-passwords.txt', 'r') as blacklist_file:
            blacklist = list(map(lambda x: x.strip(),
                                 tuple(blacklist_file.readlines())))
    except IOError:
        print("File '500-worst-passwords.txt' is not found")

    return blacklist


def get_dict_strength(password):
    blacklist = read_worst_passwords()
    dict_strength = 1

    if not blacklist:
        dict_strength = 0
    elif password in blacklist:
        dict_strength = -3
    elif any(len(word) > 3 and word in password for word in blacklist):
        dict_strength = -2

    return dict_strength


def get_base_strength(password):
    base_strength = (any(c.islower() for c in password) +
                     any(c.isupper() for c in password) +
                     any(c.isdigit() for c in password) +
                     any(c.isalpha() for c in password))
    base_strength += 1 if base_strength == 4 else 0

    return base_strength


def get_password_strength(password):
    strength = 1

    if len(password) > 6:
        strength = (strength +
                    get_base_strength(password) +
                    get_dict_strength(password) +
                    len(re.findall(r'[\,\.\!\@\#\&\$]', password)) +
                    (1 if len(password) > 10 else 0))

        if not 0 < strength < 11:
            strength = 10 if strength > 10 else 1

    return strength


if __name__ == '__main__':
    in_password = getpass.getpass("input your password for check:")
    print('Your password strength is %d' % get_password_strength(in_password))
