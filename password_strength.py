import re
import getpass

def get_password_strength(password):
    with open('500-worst-passwords.txt', 'r') as blacklist_file:
        blacklist = list(map(lambda x: x.strip(),
                             tuple(blacklist_file.readlines())))

    strength = 1

    if len(password) > 6:
        base_strength = any(c.islower() for c in password) + \
                        any(c.isupper() for c in password) + \
                        any(c.isdigit() for c in password) + \
                        any(c.isalpha() for c in password)
        base_strength += 1 if base_strength == 4 else 0

        dict_strength = 1
        if password in blacklist:
            dict_strength = -3
        elif any(len(word)>3 and word in password for word in blacklist):
            dict_strength = -2

        strength = strength + base_strength + dict_strength + \
                   len(re.findall(r'[\,\.\!\@\#\&\$]', password)) + \
                   (1 if len(password) > 10 else 0)

        if not 0 < strength < 11:
            strength = 10 if strength > 10 else 1

    return strength


if __name__ == '__main__':
    password = getpass.getpass("input your password for check:")
    print('Your password strength is %d' % get_password_strength(password))
