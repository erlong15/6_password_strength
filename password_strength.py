import re


def get_password_strength(password):
    blacklist = list(map(lambda x: x.strip(),
                         tuple(open('500-worst-passwords.txt', 'r'))))
    strength = 1

    if len(password) > 6:
        base_strength = any(c.islower() for c in password) + \
                        any(c.isupper() for c in password) + \
                        any(c.isdigit() for c in password) + \
                        any(c.isalpha() for c in password)
        base_strength += 1 if base_strength == 4 else 0
        rpass = re.compile(password)

        dict_strength = 1
        if password in blacklist:
            dict_strength = -3
        elif any(re.search(word, password) is not None for word in blacklist):
            dict_strength = -2

        strength = strength + base_strength + dict_strength + \
                   len(re.findall(r'\,\.\!\@\#\&\$', password)) + \
                   (1 if len(password) > 10 else 0)

        if strength > 10:
            strength = 10
        if strength <= 0:
            strength = 1

    return strength


if __name__ == '__main__':
    password = input("input your password for check:")
    print(get_password_strength(password))
