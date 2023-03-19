#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import pytest
from scr.pages.auth_page import AuthRT, AuthRTExpectations
from scr.settings import *
# pytest test_auth.py > myoutput_auth.log


@pytest.mark.norm
def test_auth_page(browser, request):
    """Позитивный тест загрузки страницы Авторизации
       ТЕСТ 2-01 - загрузка страницы Авторизации и наличие корпоративного слогана"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_auth_page(), "Отсутствует название сайта"
    assert t_auth_page.auth_expect_auth_slogan(), "Отсутствует название слоган"


@pytest.mark.skip(reason="Требуется капча")
def test_auth_email_valid_form(browser, request):
    """Позитивные тесты входа в зарегистрированный ЛК разными способами (по доступности) с верными данными
       ТЕСТ 2-02 - вход через форму Авторизации с использованием E-mail"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_email()
    t_auth_page.auth_login(valid_email)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_name()\
           or t_auth_page.auth_expect_captcha_fail(), ""
    assert t_auth_page.auth_expect_surname(), ""


@pytest.mark.skip(reason="Требуется капча")
def test_auth_phone_valid_form(browser, request):
    """ТЕСТ 2-03 - вход через форму Авторизации с использованием номера телефона"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_phone()
    t_auth_page.auth_login(valid_phone)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_name(), ""
    assert t_auth_page.auth_expect_surname(), ""


@pytest.mark.norm
def test_auth_page_ok(browser, request):
    """Тест 2-04 на переход авторизации через соц.сеть ok"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_ok()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_auth_page_ok(), "Нет перехода на ok"


@pytest.mark.norm
def test_auth_page_mail(browser, request):
    """Тест 2-05 на переход авторизации через соц.сеть mail"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_mail()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_auth_page_mail(), "Нет перехода на mail"


@pytest.mark.skip(reason="Требуется капча")
def test_auth_phone_invalid_password(browser, request):
    """# Негативные тесты с вводом неверного пароля при валидном логине
       ТЕСТ 2-06 - вход через форму Авторизации по номеру телефона с использованием неверного пароля"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_phone()
    t_auth_page.auth_login(valid_phone)
    t_auth_page.auth_password(invalid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_auth_fail()\
           or t_auth_page.auth_expect_captcha_fail(), ""


@pytest.mark.skip(reason="Требуется капча")
def test_auth_email_invalid_password(browser, request):
    """# ТЕСТ 2-07 - вход через форму Авторизации по E-mail с использованием неверного пароля"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_email()
    t_auth_page.auth_login(valid_email)
    t_auth_page.auth_password(invalid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_auth_fail()\
           or t_auth_page.auth_expect_captcha_fail(), ""


@pytest.mark.skip(reason="Требуется капча")
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_phone_invalid_login(browser, login, request):
    """Негативные тесты с вводом несоответствующих типу поля данных / невалидных данных по каждому отдельному полю
       ТЕСТ 2-08 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
       для поля логин при выборе входа по номеру телефона"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_phone()
    t_auth_page.auth_login(login)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), ""


@pytest.mark.skip(reason="Требуется капча")
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_email_invalid_login(browser, login, request):
    """ТЕСТ 2-09 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
       для поля логин при выборе входа по E-mail"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_email()
    t_auth_page.auth_login(login)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), ""


@pytest.mark.skip(reason="Требуется капча")
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_login_invalid_login(browser, login, request):
    """ТЕСТ 2-10 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
       для поля логин при выборе входа по логину"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_login()
    t_auth_page.auth_login(login)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), ""


@pytest.mark.skip(reason="Требуется капча")
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_login_invalid_ls(browser, login, request):
    """ТЕСТ 2-11 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
       для поля логин при выборе входа по лицевому счету (ЛС)"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_ls()
    t_auth_page.auth_login(login)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), ""


@pytest.mark.norm
def test_auth_page_vk(browser, request):
    """Тест 2-12 - на переход авторизации через соц.сеть VK"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_vk()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_auth_page_vk(), "Нет перехода на vk"


@pytest.mark.norm
def test_auth_page_google(browser, request):
    """Тест 2-13 - на переход авторизации через соц.сеть google"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_google()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_auth_page_google(), "Нет перехода на google"


@pytest.mark.norm
def test_auth_page_yandex(browser, request):
    """Тест 2-14 - на переход авторизации через соц.сеть yandex"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    time.sleep(3)
    t_auth_page.auth_type_yandex()

    t_auth_page = AuthRTExpectations(browser)
    time_expect_screen = t_auth_page.timetest()
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_auth_page.auth_expect_auth_page_yandex(), "Не происходит переход на Yandex"
