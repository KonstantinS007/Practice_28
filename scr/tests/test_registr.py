#  pytest test_registr.py > myoutput_registr.log
#  pytest -m norm > myoutput_norm.log
import pytest
from scr.pages.registr_page import RegRT, RegRTExpectations
from scr.settings import *



@pytest.mark.norm
def test_reg_page(browser, request):
    """Позитивный тест загрузки страницы и перехода в раздел Регистрация
       ТЕСТ 1-01 - переход на страницу Регистрации со страницы Авторизации"""
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()

    t_reg_page = RegRTExpectations(browser)
    time_expect_screen = t_reg_page.timetest()
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_reg_page.reg_expect_reg_title(), f'Error bag - screenshots_registr/{request.node.name}_{time_expect_screen}.png'


@pytest.mark.norm
def test_reg_slogan(browser, request):
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()

    t_reg_page = RegRTExpectations(browser)
    time_expect_screen = t_reg_page.timetest()
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_reg_page.reg_expect_slogan(), f'Error bag - screenshots_registr/{request.node.name}_{time_expect_screen}.png'


@pytest.mark.skip(reason="Требуется регистрация и ввод кода")
def test_reg_form_valid(browser, request):
    """Позитивный тест ввода всех валидных данных по каждому полю
       ТЕСТ 1-02 - ввод данных в форму Регистрации"""
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()
    t_reg_page.reg_first_name(valid_first_name)
    t_reg_page.reg_last_name(valid_last_name)
    t_reg_page.reg_address(valid_email)
    t_reg_page.reg_password(valid_password)
    t_reg_page.reg_password_confirm(valid_password_confirm)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(test).png')
    t_reg_page.reg_button()

    t_reg_page = RegRTExpectations(browser)
    time_expect_screen = t_reg_page.timetest()
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_reg_page.reg_expect_valid_code(), f'Error bag - {request.node.name}_{time_expect_screen}.png'

    t_reg_page = RegRT(browser)
    t_reg_page.reg_code(valid_code)

    t_reg_page = RegRTExpectations(browser)
    time_expect_screen = t_reg_page.timetest()
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_reg_page.reg_expect_surname(), f'Error bag - {request.node.name}_{time_expect_screen}.png'


@pytest.mark.norm
@pytest.mark.parametrize("first_name", [double_first_name, one_letter_first_name, empty_form, double_dash_first_name,
                                        apostrophe_first_name, latin_first_name, long_first_name])
def test_reg_form_name(browser, first_name, request):
    """Негативные тесты ввода невалидных данных по каждому отдельному полю
       ТЕСТ 1-03 (x7 параметров) - ввод данных в форму Регистрации - Поле 'Имя'"""
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()
    t_reg_page.reg_first_name(first_name)
    t_reg_page.reg_last_name(valid_last_name)
    t_reg_page.reg_address(valid_email)
    t_reg_page.reg_password(valid_password)
    t_reg_page.reg_password_confirm(valid_password_confirm)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(test).png')
    t_reg_page.reg_button()

    t_reg_page = RegRTExpectations(browser)
    time_expect_screen = t_reg_page.timetest()
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_reg_page.reg_expect_name(), f'Error bag - {request.node.name}_{time_expect_screen}.png'


@pytest.mark.norm
@pytest.mark.parametrize("last_name", [double_last_name, one_letter_last_name, double_dash_last_name,
                                       apostrophe_last_name, latin_last_name, long_last_name, empty_form])
def test_reg_form_surname(browser, last_name, request):
    """ТЕСТ 1-04 (x7 параметров) - ввод данных в форму Регистрации - Поле 'Фамилия'"""
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()
    t_reg_page.reg_first_name(valid_first_name)
    t_reg_page.reg_last_name(last_name)
    t_reg_page.reg_address(valid_email)
    t_reg_page.reg_password(valid_password)
    t_reg_page.reg_password_confirm(valid_password_confirm)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(test).png')
    t_reg_page.reg_button()

    t_reg_page = RegRTExpectations(browser)
    time_expect_screen = t_reg_page.timetest()
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_reg_page.reg_expect_surname(), f'Error bag - {request.node.name}_{time_expect_screen}.png'


@pytest.mark.norm
@pytest.mark.parametrize("address", [invalid_email, empty_form, invalid_phone, invalid_phone_2])
def test_reg_form_address(browser, address, request):
    """ТЕСТ 1-05 (x4 параметра) - ввод данных в форму Регистрации - Поле 'E-mail или мобильный телефон'"""
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()
    t_reg_page.reg_first_name(valid_first_name)
    t_reg_page.reg_last_name(valid_last_name)
    t_reg_page.reg_address(address)
    t_reg_page.reg_password(valid_password)
    t_reg_page.reg_password_confirm(valid_password_confirm)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(test).png')
    t_reg_page.reg_button()

    t_reg_page = RegRTExpectations(browser)
    time_expect_screen = t_reg_page.timetest()
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_reg_page.reg_expect_address(), f'Error bag - {request.node.name}_{time_expect_screen}.png'


@pytest.mark.norm
@pytest.mark.parametrize("password", [unicode_password, short_password, long_password, empty_form,
                                      only_letter_password, lower_password, upper_password, cyrillic_password])
def test_reg_form_password(browser, password, request):
    """ТЕСТ 1-06 (x8 параметров) - ввод данных в форму Регистрации - Поле 'Пароль'"""
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()
    t_reg_page.reg_first_name(valid_first_name)
    t_reg_page.reg_last_name(valid_last_name)
    t_reg_page.reg_address(valid_email)
    t_reg_page.reg_password(password)
    t_reg_page.reg_password_confirm(password)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(test).png')
    t_reg_page.reg_button()

    t_reg_page = RegRTExpectations(browser)
    time_expect_screen = t_reg_page.timetest()
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_reg_page.reg_expect_password(), f'Error bag - {request.node.name}_{time_expect_screen}.png'


@pytest.mark.norm
@pytest.mark.parametrize("password_confirm", [invalid_password_confirm, empty_form],
                         ids=["invalid_password_confirm", "empty_form"])
def test_reg_form_password_confirm(browser, password_confirm, request):
    """ТЕСТ 1-07 (x2 параметра) - ввод данных в форму Регистрации - Поле 'Подтверждение пароля'"""
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()
    t_reg_page.reg_first_name(valid_first_name)
    t_reg_page.reg_last_name(valid_last_name)
    t_reg_page.reg_address(valid_email)
    t_reg_page.reg_password(valid_password)
    t_reg_page.reg_password_confirm(password_confirm)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(test).png')
    t_reg_page.reg_button()

    t_reg_page = RegRTExpectations(browser)
    time_expect_screen = t_reg_page.timetest()
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_reg_page.reg_expect_password_confirm(), f'Error bag - {request.node.name}_{time_expect_screen}.png'




@pytest.mark.norm
def test_reg_address_reg(browser, request):
    """ТЕСТ 1-09 - ввод данных в форму Регистрации - Зарегистрированный ранее 'E-mail или мобильный телефон'"""
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()
    t_reg_page.reg_first_name(valid_first_name)
    t_reg_page.reg_last_name(valid_last_name)
    t_reg_page.reg_address(valid_email_reg)
    t_reg_page.reg_password(valid_password)
    t_reg_page.reg_password_confirm(valid_password_confirm)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(test).png')
    t_reg_page.reg_button()

    t_reg_page = RegRTExpectations(browser)
    time_expect_screen = t_reg_page.timetest()
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{time_expect_screen}(expect).png')
    assert t_reg_page.reg_expect_address_reg(), f'Error bag - {request.node.name}_{time_expect_screen}.png'

