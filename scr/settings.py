#!/usr/bin/python3
# -*- encoding=utf8 -*-
# данные для тестов регистрации, авторизации и восстановления пароля, а также параметризованных тестов

# Исходные валидные значения заменены после прохождения регистрации и всех проверок.
# Вы можете заменить значения на свои (валидные) и запустить тесты


    # валидные данные

  # КАПЧА вручную (число время ввода) либо код от разработчиков с записью по локатору
valid_first_name = "Студент"
valid_last_name = "Тестер"
valid_email = "intqap@skillfactory.ru"
valid_phone = "+7900000001"
valid_password = "Qwerty123"
valid_password_confirm = valid_password
valid_code = "77777"  # код подтверждения, высылаемый на телефон/почту, вводится вручную

new_valid_password = "PASSword123"
new_valid_password_confirm = new_valid_password
valid_email_confirm = "1******@list.ru"
valid_phone_confirm = "+7 ••• •••-64-11"
old_valid_password = "Password123"
old_valid_password_confirm = old_valid_password


    # невалидные/неверные данные
double_first_name = "Анна Мария"
double_last_name = "Маркес Санчес"
one_letter_first_name = "Ю"
one_letter_last_name = "Я"
double_dash_first_name = "Абу-аль-Хасан"
double_dash_last_name = "Абу-ибн-Хасан"
apostrophe_first_name = "О'Лири"
apostrophe_last_name = "О'Коннор"
latin_first_name = "Vladimir"
latin_last_name = "Ivanov"
long_first_name = "Оченьоченьдлинноерусскоенародноеимя"
long_last_name = "Оченьдлиннаярусскаянароднаяфамилия"

valid_email_reg = valid_email
digit_valid_email = "123456@email.ru"
invalid_email = "123pochta@.emailru"
non_reg_email = "clientname@email.ru"

invalid_phone = "+790012345678"
invalid_phone_2 = "+7900123456"
non_reg_phone = "+79001234567"
non_reg_login = "RTpassportlogin123!"
non_reg_ls = "810293847566"
invalid_ls = "81293847566"

unicode_password = "ASDfgh123東のعไδ①¾"  # 東のعไδ①¾
short_password = "ASfgh1"
long_password = "ASDFGHJKLzxcvbnm12345"
only_letter_password = "ASDFGHJKLzxcvbnm"
lower_password = "zxcvbnm12345"
upper_password = "ASDFGHJKL12345"
cyrillic_password = "ФЫВАПячсми12345"
invalid_password = "ASDzxc123!"
invalid_password_confirm = "ASDFGzxcvb12345"

empty_form = ""
invalid_code = "123456"
invalid_captcha = "A1s2D3QWE4"

