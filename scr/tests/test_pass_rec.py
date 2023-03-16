#  pytest test_pass_rec.py > myoutput_pass_rec.log
import time
import pytest
from scr.pages.pass_rec_page import PassRecRT, PassRecRTExpectations
from scr.settings import *


# Позитивный тест загрузки страницы и перехода в раздел Восстановления пароля
# ТЕСТ 3-01 - переход на страницу Восстановления пароля со страницы Авторизации
@pytest.mark.norm
def test_pass_rec_page(browser, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.pass_rec_expect_pass_rec_title()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')


# Позитивные тесты способов восстановления пароля по зарегистрированным данных
# ТЕСТ 3-02 - ввод данных в форму Восстановления пароля - по номеру телефона и по смс-коду
def test_pass_rec_valid_phone_phone(browser, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()
    t_pass_rec_page.pass_rec_type_phone()
    t_pass_rec_page.pass_rec_login(valid_phone)
    time.sleep(20)  # captcha
    t_pass_rec_page.pass_rec_button_continue()
    t_pass_rec_page.pass_rec_code_phone()
    t_pass_rec_page.pass_rec_button_continue_reset()
    t_pass_rec_page.pass_rec_code_input_valid_code()
    # ручной ввод кода, полученного на электронную почту или по смс
    time.sleep(10)
    t_pass_rec_page.pass_rec_new_password(new_valid_password)
    t_pass_rec_page.pass_rec_new_password_confirm(new_valid_password_confirm)
    t_pass_rec_page.pass_rec_button_save_new_password()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.auth_expect_auth_new()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')


# ТЕСТ 3-03 - ввод данных в форму Восстановления пароля - по номеру телефона и по коду на E-mail
def test_pass_rec_valid_phone_email(browser, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()
    t_pass_rec_page.pass_rec_type_phone()
    t_pass_rec_page.pass_rec_login(valid_phone)
    time.sleep(20)  # captcha
    t_pass_rec_page.pass_rec_button_continue()
    t_pass_rec_page.pass_rec_code_email()
    t_pass_rec_page.pass_rec_button_continue_reset()
    t_pass_rec_page.pass_rec_code_input_valid_code()
    # ручной ввод кода, полученного на электронную почту или по смс
    time.sleep(10)
    t_pass_rec_page.pass_rec_new_password(new_valid_password)
    t_pass_rec_page.pass_rec_new_password_confirm(new_valid_password_confirm)
    t_pass_rec_page.pass_rec_button_save_new_password()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.auth_expect_auth_new()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')


# ТЕСТ 3-04 - ввод данных в форму Восстановления пароля - по E-mail и по смс-коду
def test_pass_rec_valid_email_phone(browser, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()
    t_pass_rec_page.pass_rec_type_email()
    t_pass_rec_page.pass_rec_login(valid_email)
    time.sleep(20)  # captcha
    t_pass_rec_page.pass_rec_button_continue()
    t_pass_rec_page.pass_rec_code_phone()
    t_pass_rec_page.pass_rec_button_continue_reset()
    t_pass_rec_page.pass_rec_code_input_valid_code()
    # ручной ввод кода, полученного на электронную почту или по смс
    time.sleep(10)
    t_pass_rec_page.pass_rec_new_password(new_valid_password)
    t_pass_rec_page.pass_rec_new_password_confirm(new_valid_password_confirm)
    t_pass_rec_page.pass_rec_button_save_new_password()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.auth_expect_auth_new()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')


# ТЕСТ 3-05 - ввод данных в форму Восстановления пароля - по E-mail и по коду на E-mail
def test_pass_rec_valid_email_email(browser, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()
    t_pass_rec_page.pass_rec_type_email()
    t_pass_rec_page.pass_rec_login(valid_email)
    time.sleep(20)  # captcha
    t_pass_rec_page.pass_rec_button_continue()
    t_pass_rec_page.pass_rec_code_email()
    t_pass_rec_page.pass_rec_button_continue_reset()
    t_pass_rec_page.pass_rec_code_input_valid_code()
    # ручной ввод кода, полученного на электронную почту или по смс
    time.sleep(10)
    t_pass_rec_page.pass_rec_new_password(new_valid_password)
    t_pass_rec_page.pass_rec_new_password_confirm(new_valid_password_confirm)
    t_pass_rec_page.pass_rec_button_save_new_password()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.auth_expect_auth_new()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')


# негативные тесты ввода невалидных данных по каждому отдельному полю
# ТЕСТ 3-06 (x10 параметров) - ввод данных в форму Восстановления пароля - по номеру телефона, поле "Логин"
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_pass_rec_form_valid_login_phone(browser, login, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()
    t_pass_rec_page.pass_rec_type_phone()
    t_pass_rec_page.pass_rec_login(login)
    time.sleep(20)  # captcha
    t_pass_rec_page.pass_rec_button_continue()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.pass_rec_expect_login or t_pass_rec_page.pass_rec_expect_pass_rec_fail()\
           or t_pass_rec_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')


# ТЕСТ 3-07 (x10 параметров) - ввод данных в форму Восстановления пароля - по E-mail, поле "Логин"
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_pass_rec_form_valid_login_email(browser, login, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()
    t_pass_rec_page.pass_rec_type_email()
    t_pass_rec_page.pass_rec_login(login)
    time.sleep(20)  # captcha
    t_pass_rec_page.pass_rec_button_continue()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.pass_rec_expect_login or t_pass_rec_page.pass_rec_expect_pass_rec_fail()\
           or t_pass_rec_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')


# ТЕСТ 3-08 (x10 параметров) - ввод данных в форму Восстановления пароля - по Логину, поле "Логин"
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_pass_rec_form_valid_login_login(browser, login, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()
    t_pass_rec_page.pass_rec_type_login()
    t_pass_rec_page.pass_rec_login(login)
    time.sleep(20)  # captcha
    t_pass_rec_page.pass_rec_button_continue()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.pass_rec_expect_login or t_pass_rec_page.pass_rec_expect_pass_rec_fail()\
           or t_pass_rec_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')


# ТЕСТ 3-09 (x10 параметров) - ввод данных в форму Восстановления пароля - по лицевому счету, поле "Логин"
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_pass_rec_form_valid_login_ls(browser, login, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()
    t_pass_rec_page.pass_rec_type_ls()
    t_pass_rec_page.pass_rec_login(login)
    time.sleep(20)  # captcha
    t_pass_rec_page.pass_rec_button_continue()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.pass_rec_expect_login or t_pass_rec_page.pass_rec_expect_pass_rec_fail()\
           or t_pass_rec_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')


# ТЕСТ 3-10 - ввод данных в форму Восстановления пароля - без выбора варианта получения кода
@pytest.mark.norm
def test_pass_rec_form_valid_login_by_none(browser, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()
    t_pass_rec_page.pass_rec_type_email()
    t_pass_rec_page.pass_rec_login(valid_email)
    time.sleep(20)  # captcha
    t_pass_rec_page.pass_rec_button_continue()
    t_pass_rec_page.pass_rec_button_continue_reset()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.pass_rec_expect_code_send()\
           or t_pass_rec_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')


# ТЕСТ 3-11 - ввод данных в форму Восстановления пароля
# выбор получения кода по E-mail, ввод неверного кода
@pytest.mark.norm
def test_pass_rec_form_valid_login_by_code(browser, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()
    t_pass_rec_page.pass_rec_type_email()
    t_pass_rec_page.pass_rec_login(valid_email)
    time.sleep(20)  # captcha
    t_pass_rec_page.pass_rec_button_continue()
    t_pass_rec_page.pass_rec_code_email()
    t_pass_rec_page.pass_rec_button_continue_reset()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.pass_rec_expect_code_send()\
           or t_pass_rec_page.auth_expect_captcha_fail()

    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.pass_rec_code_input_invalid_code(invalid_code)

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.pass_rec_expect_code_send()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')


# ТЕСТ 3-12 - ввод данных в форму Восстановления пароля
# выбор получения кода по смс, ввод неверного кода
@pytest.mark.norm
def test_pass_rec_form_valid_login_by_sms(browser, request):
    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.go_to_site()
    t_pass_rec_page.pass_rec_page()
    t_pass_rec_page.pass_rec_type_email()
    t_pass_rec_page.pass_rec_login(valid_email)
    time.sleep(20)  # captcha
    t_pass_rec_page.pass_rec_button_continue()
    t_pass_rec_page.pass_rec_code_phone()
    t_pass_rec_page.pass_rec_button_continue_reset()

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.pass_rec_expect_code_send()\
           or t_pass_rec_page.auth_expect_captcha_fail()

    t_pass_rec_page = PassRecRT(browser)
    t_pass_rec_page.pass_rec_code_input_invalid_code(invalid_code)

    t_pass_rec_page = PassRecRTExpectations(browser)
    assert t_pass_rec_page.pass_rec_expect_code_send()
    browser.save_screenshot(f'screenshots_pass_rec/{request.node.name}_{t_pass_rec_page.timetest()}.png')
