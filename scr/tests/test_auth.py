# pytest test_auth.py > myoutput_auth.log
import time
import pytest
from scr.pages.auth_page import AuthRT, AuthRTExpectations
from scr.settings import *


# Позитивный тест загрузки страницы Авторизации
# ТЕСТ 2-01 - загрузка страницы Авторизации и наличие корпоративного слогана
@pytest.mark.norm
def test_auth_page(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()

    t_auth_page = AuthRTExpectations(browser)
    assert t_auth_page.auth_expect_auth_page()
    assert t_auth_page.auth_expect_auth_slogan()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')


# Позитивные тесты входа в зарегистрированный ЛК разными способами (по доступности) с верными данными
# ТЕСТ 2-02 - вход через форму Авторизации с использованием E-mail
@pytest.mark.norm
def test_auth_email_valid_form(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_email()
    t_auth_page.auth_login(valid_email)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    t_auth_page.auth_button()
    time.sleep(10)

    t_auth_page = AuthRTExpectations(browser)
    assert t_auth_page.auth_expect_name()\
           or t_auth_page.auth_expect_captcha_fail()
    assert t_auth_page.auth_expect_surname()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')


# ТЕСТ 2-03 - вход через форму Авторизации с использованием номера телефона
@pytest.mark.norm
def test_auth_phone_valid_form(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_phone()
    t_auth_page.auth_login(valid_phone)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    t_auth_page.auth_button()
    time.sleep(10)

    t_auth_page = AuthRTExpectations(browser)
    assert t_auth_page.auth_expect_name()
    assert t_auth_page.auth_expect_surname()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')


# негативные тесты с вводом неверного пароля при валидном логине
# ТЕСТ 2-06 - вход через форму Авторизации по номеру телефона с использованием неверного пароля
@pytest.mark.norm
def test_auth_phone_invalid_password(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_phone()
    t_auth_page.auth_login(valid_phone)
    t_auth_page.auth_password(invalid_password)
    time.sleep(20)  # captcha
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    assert t_auth_page.auth_expect_auth_fail()\
           or t_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')


# ТЕСТ 2-07 - вход через форму Авторизации по E-mail с использованием неверного пароля
@pytest.mark.norm
def test_auth_email_invalid_password(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_email()
    t_auth_page.auth_login(valid_email)
    t_auth_page.auth_password(invalid_password)
    time.sleep(20)  # captcha
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    assert t_auth_page.auth_expect_auth_fail()\
           or t_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')


# негативные тесты с вводом несоответствующих типу поля данных / невалидных данных по каждому отдельному полю
# ТЕСТ 2-08 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по номеру телефона
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_phone_invalid_login(browser, login, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_phone()
    t_auth_page.auth_login(login)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')


# ТЕСТ 2-09 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по E-mail
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_email_invalid_login(browser, login, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_email()
    t_auth_page.auth_login(login)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')


# ТЕСТ 2-10 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по логину
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_login_invalid_login(browser, login, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_login()
    t_auth_page.auth_login(login)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')


# ТЕСТ 2-11 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по лицевому счету (ЛС)
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_login_invalid_ls(browser, login, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_ls()
    t_auth_page.auth_login(login)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
