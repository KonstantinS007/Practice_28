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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_auth_page(), "Отсутствует название сайта"
    assert t_auth_page.auth_expect_auth_slogan(), "Отсутствует слоган"


@pytest.mark.norm
def test_page_document(browser, request):
    """Переход на страницу пользовательского соглашения открытием новой вкладки"""
    t_auth_document = AuthRT(browser)
    t_auth_document.go_to_site()
    t_auth_document.auth_type_document()
    # Открытие элемента в контейнере
    t_page_document = AuthRTExpectations(browser)

    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_document.timetest()}(expect).png')
    assert t_page_document.auth_expect_document_page(), "Не тот документ"


def test_elements_registration(browser, request):
    """ТЕСТ 2-02 Проверка Формы "Авторизации" на наличие основных элементов."""

    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    time.sleep(4)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_type_phone(), "Отсуствует элемент выбора авторизации 'Телефон'"
    assert t_auth_page.auth_type_email(), "Отсуствует элемент выбора авторизации 'Почта'"
    assert t_auth_page.auth_type_login(), "Отсуствует элемент выбора авторизации 'Логин'"
    assert t_auth_page.auth_type_ls(), "Отсуствует элемент выбора авторизации 'Лицевой счёт'"
    assert t_auth_page.auth_login(""), "Отсуствует элемент поля логина"
    assert t_auth_page.auth_password(""), "Отсуствует элемент поля пароль"
    assert t_auth_page.auth_button(), "Отсуствует элемент кнопка 'Авторизация'"


def test_menu_type_autoriz(browser, request):
    """ТЕСТ 2-03 Проверка названия табов в меню выбора типа авторизации."""

    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_type_phone(), 'Ошибка в имени таба Меню "Телефон"'
    assert t_auth_page.auth_expect_type_email(), 'Ошибка в имени таба Меню "Почта"'
    assert t_auth_page.auth_expect_type_login(), 'Ошибка в имени таба Меню "Логин"'
    assert t_auth_page.auth_expect_type_ls(), 'Ошибка в имени таба Меню "Лицевой счет"'


@pytest.mark.norm
def test_auth_page_ok(browser, request):
    """Тест 2-04 на переход авторизации через соц.сеть ok"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_ok()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_auth_page_ok(), "Нет перехода на ok"


@pytest.mark.norm
def test_auth_page_mail(browser, request):
    """Тест 2-05 на переход авторизации через соц.сеть mail"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_mail()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_auth_page_mail(), "Нет перехода на mail"


@pytest.mark.norm
def test_auth_page_vk(browser, request):
    """Тест 2-06- на переход авторизации через соц.сеть VK"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_vk()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_auth_page_vk(), "Нет перехода на vk"


@pytest.mark.norm
def test_auth_page_google(browser, request):
    """Тест 2-07 - на переход авторизации через соц.сеть google"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_google()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_auth_page_google(), "Нет перехода на google"


@pytest.mark.norm
def test_auth_page_yandex(browser, request):
    """Тест 2-08 - на переход авторизации через соц.сеть yandex"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    time.sleep(3)
    t_auth_page.auth_type_yandex()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_auth_page_yandex(), "Не происходит переход на Yandex"



@pytest.mark.skip(reason="Требуется капча")
def test_auth_email_valid_form(browser, request):
    """Позитивные тесты входа в зарегистрированный ЛК разными способами (по доступности) с верными данными
       ТЕСТ 2-12 - вход через форму Авторизации с использованием E-mail"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_email()
    t_auth_page.auth_login(valid_email)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_name()\
           or t_auth_page.auth_expect_captcha_fail(), ""
    assert t_auth_page.auth_expect_surname(), ""


@pytest.mark.skip(reason="Требуется капча")
def test_auth_phone_valid_form(browser, request):
    """ТЕСТ 2-13 - вход через форму Авторизации с использованием номера телефона"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_phone()
    t_auth_page.auth_login(valid_phone)
    t_auth_page.auth_password(valid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_name(), ""
    assert t_auth_page.auth_expect_surname(), ""




@pytest.mark.skip(reason="Требуется капча")
def test_auth_phone_invalid_password(browser, request):
    """# Негативные тесты с вводом неверного пароля при валидном логине
       ТЕСТ 2-16 - вход через форму Авторизации по номеру телефона с использованием неверного пароля"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_phone()
    t_auth_page.auth_login(valid_phone)
    t_auth_page.auth_password(invalid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_auth_fail()\
           or t_auth_page.auth_expect_captcha_fail(), ""


@pytest.mark.skip(reason="Требуется капча")
def test_auth_email_invalid_password(browser, request):
    """# ТЕСТ 2-17 - вход через форму Авторизации по E-mail с использованием неверного пароля"""
    t_auth_page = AuthRT(browser)
    t_auth_page.go_to_site()
    t_auth_page.auth_type_email()
    t_auth_page.auth_login(valid_email)
    t_auth_page.auth_password(invalid_password)
    time.sleep(20)  # captcha
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(test).png')
    t_auth_page.auth_button()

    t_auth_page = AuthRTExpectations(browser)
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_auth_fail()\
           or t_auth_page.auth_expect_captcha_fail(), ""


@pytest.mark.skip(reason="Требуется капча")
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_phone_invalid_login(browser, login, request):
    """Негативные тесты с вводом несоответствующих типу поля данных / невалидных данных по каждому отдельному полю
       ТЕСТ 2-18 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), ""


@pytest.mark.skip(reason="Требуется капча")
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_email_invalid_login(browser, login, request):
    """ТЕСТ 2-19 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), ""


@pytest.mark.skip(reason="Требуется капча")
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_login_invalid_login(browser, login, request):
    """ТЕСТ 2-20 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), ""


@pytest.mark.skip(reason="Требуется капча")
@pytest.mark.parametrize("login", [invalid_email, non_reg_email, invalid_phone, non_reg_phone, non_reg_login,
                                   non_reg_ls, empty_form, digit_valid_email, invalid_ls, invalid_phone_2])
def test_auth_login_invalid_ls(browser, login, request):
    """ТЕСТ 2-21 (x10 параметров) - вход через форму Авторизации с использованием несоответствующего типа данных
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
    browser.save_screenshot(f'screenshots_auth/{request.node.name}_{t_auth_page.timetest()}(expect).png')
    assert t_auth_page.auth_expect_login() or t_auth_page.auth_expect_auth_fail() \
           or t_auth_page.auth_expect_captcha_fail(), ""


