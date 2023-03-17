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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_auth_page(), f'Error bag - screenshot {request.node.name}'
    assert t_auth_page.auth_expect_auth_slogan(), f'Error bag - screenshot {request.node.name}'


@pytest.mark.norm
def test_auth_page_vk(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_vk()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_auth_page_vk(), f'Error bag - screenshot {request.node.name}'


@pytest.mark.norm
def test_auth_page_ok(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_ok()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_auth_page_ok(), f'Error bag - screenshot {request.node.name}'


@pytest.mark.norm
def test_auth_page_mail(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_mail()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_auth_page_mail(), f'Error bag - screenshot {request.node.name}'


@pytest.mark.norm
def test_auth_page_google(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_google()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_auth_page_google(), f'Error bag - screenshot {request.node.name}'


@pytest.mark.norm
def test_auth_page_yandex(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_yandex()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_auth_page_yandex(), f'Error bag - screenshot {request.node.name}'


# Позитивные тесты входа в зарегистрированный ЛК разными способами (по доступности) с верными данными
# ТЕСТ 2-02 - вход через форму Авторизации с использованием E-mail
@pytest.mark.skip(reason="Требуется капча")
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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_name()\
           or t_auth_page.auth_expect_captcha_fail(), f'Error bag - screenshot {request.node.name}'
    assert t_auth_page.auth_expect_surname(), f'Error bag - screenshot {request.node.name}'


# ТЕСТ 2-03 - вход через форму Авторизации с использованием номера телефона
@pytest.mark.skip(reason="Требуется капча")
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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_name(), f'Error bag - screenshot {request.node.name}'
    assert t_auth_page.auth_expect_surname(), f'Error bag - screenshot {request.node.name}'


# негативные тесты с вводом неверного пароля при валидном логине
# ТЕСТ 2-06 - вход через форму Авторизации по номеру телефона с использованием неверного пароля
@pytest.mark.skip(reason="Требуется капча")
def test_auth_phone_invalid_password(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_phone()
    t_auth_page.auth_login(valid_phone)
    t_auth_page.auth_password(invalid_password)
    time.sleep(20)  # captcha
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_auth_fail()\
           or t_auth_page.auth_expect_captcha_fail(), f'Error bag - screenshot {request.node.name}'


# ТЕСТ 2-07 - вход через форму Авторизации по E-mail с использованием неверного пароля
@pytest.mark.skip(reason="Требуется капча")
def test_auth_email_invalid_password(browser, request):
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_email()
    t_auth_page.auth_login(valid_email)
    t_auth_page.auth_password(invalid_password)
    time.sleep(20)  # captcha
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_auth_fail()\
           or t_auth_page.auth_expect_captcha_fail(), f'Error bag - screenshot {request.node.name}'


# негативные тесты с вводом несоответствующих типу поля данных / невалидных данных по каждому отдельному полю
# ТЕСТ 2-08 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по номеру телефона
@pytest.mark.skip(reason="Требуется капча")
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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), f'Error bag - screenshot {request.node.name}'


# ТЕСТ 2-09 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по E-mail
@pytest.mark.skip(reason="Требуется капча")
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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), f'Error bag - screenshot {request.node.name}'


# ТЕСТ 2-10 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по логину
@pytest.mark.skip(reason="Требуется капча")
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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), f'Error bag - screenshot {request.node.name}'


# ТЕСТ 2-11 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
# для поля логин при выборе входа по лицевому счету (ЛС)
@pytest.mark.skip(reason="Требуется капча")
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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}.png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), f'Error bag - screenshot {request.node.name}'

