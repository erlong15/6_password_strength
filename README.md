# Вычисление сложности пароля

Скрипт для вычисления сложности пароля.
Используются проверки разнообразия символов, длины пароля, проверки по словарю худших паролей.
Файл с худшими паролями идет в комплекте

Ввод пароля не отображается

# Как запустить
```
python3 password_strength.py  -h
usage: password_strength.py [-h] [-f BLACKFILE]

Password strength checker.

optional arguments:
  -h, --help            show this help message and exit
  -f BLACKFILE, --blackfile BLACKFILE
                        file with blacklist`s passwords, default 500-worst-
                        passwords.txt

```

# Пример запуска
```
python3 password_strength.py 
input your password for check:
Your password strength is 9
```

# Цели проекта

Тестовый код для образовательного проекта - [DEVMAN.org](https://devman.org)
