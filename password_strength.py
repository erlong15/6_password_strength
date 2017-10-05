import re
import getpass


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

    if len(password) > 6:
        strength = (strength +
                    get_alphanum_check_points(password) +
                    get_blacklist_check_points(password, in_blacklist) +
                    len(re.findall(r'[\,\.\!\@\#\&\$]', password)) +
                    (1 if len(password) > 10 else 0))

        if not 0 < strength < 11:
            strength = 10 if strength > 10 else 1

    return strength


if __name__ == '__main__':
    in_password = getpass.getpass("input your password for check:")
    blacklist = read_worst_passwords()
    if not blacklist:
        print("File '500-worst-passwords.txt' is not found or empty")

    print('Your password strength is %d' % get_password_strength(in_password,
                                                                 blacklist))
