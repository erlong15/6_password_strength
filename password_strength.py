import re
import getpass
import argparse
import string


def read_worst_passwords():
    try:
        with open('500-worst-passwords.txt', 'r') as blacklist_file:
            black_list = list(map(lambda x: x.strip(),
                                  tuple(blacklist_file.readlines())))
    except IOError:
        black_list = []

    return black_list


def get_blacklist_check_points(password, in_blacklist):
    check_points = 1

    if not in_blacklist:
        check_points = 0
    elif password in in_blacklist:
        check_points = -3
    elif any(len(word) > 3 and word in password for word in in_blacklist):
        check_points = -2

    return check_points


def get_alphanum_check_points(password):
    check_points = (any(c.islower() for c in password) +
                    any(c.isupper() for c in password) +
                    any(c.isdigit() for c in password) +
                    any(c.isalpha() for c in password))
    check_points += 1 if check_points == 4 else 0

    return check_points


def get_password_strength(password, in_blacklist):
    strength = 1
    symbol_regexp = re.compile("[%s]" % string.punctuation)
    min_length = 6
    good_length = 10
    min_points = 1
    max_points = 10

    if len(password) > min_length:
        strength = (strength +
                    get_alphanum_check_points(password) +
                    get_blacklist_check_points(password, in_blacklist) +
                    len(symbol_regexp.findall(password)) +
                    (1 if len(password) > good_length else 0))

        if not min_points <= strength <= max_points:
            strength = max_points if strength > max_points else min_points

    return strength


def get_args():
    parser = argparse.ArgumentParser(description='Password strength checker.')
    parser.add_argument('-f', '--blackfile',
                        help='file with blacklist`s passwords, '
                             'default 500-worst-passwords.txt',
                        required=False,
                        default='500-worst-passwords.txt')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    input_password = getpass.getpass("input your password for check:")
    blacklist = read_worst_passwords()
    if not blacklist:
        print("File %s is not found or empty" % args.blackfile)

    password_strength = get_password_strength(input_password, blacklist)
    print('Your password strength is %d' % password_strength)
