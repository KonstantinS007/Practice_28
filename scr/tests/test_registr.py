import pytest
from scr.pages.registr_page import RegRT, RegRTExpectations
from scr.settings import *
#  pytest test_registr.py > myoutput_registr.log
#  pytest -m norm > myoutput_norm.log


@pytest.mark.norm
def test_reg_page(browser, request):
    """Позитивный тест загрузки страницы и перехода в раздел Регистрация
       ТЕСТ 1-01 - переход на страницу Регистрации со страницы Авторизации"""
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()

    t_reg_page = RegRTExpectations(browser)

    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_expect_reg_title(), "Нет перехода на страницу Регистрация"


def test_elements_registration(browser, request):
    """ТЕСТ 1-02 Проверка Формы "Регистрация" на наличие основных элементов."""

    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_first_name(""), "Отсутствует поле Имя"
    assert t_reg_page.reg_last_name(""), "Отсутствует поле Фамилия"
    assert t_reg_page.reg_address(""), "Отсутствует поле Почта или Телефон"
    assert t_reg_page.reg_password(""), "Отсутствует поле Пароль"
    assert t_reg_page.reg_password_confirm(""), "Отсутствует поле Повтор пароля"
    assert t_reg_page.reg_button(), "Отсутствует кнопка Зарегистрироваться"

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
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_expect_valid_code(), ""

    t_reg_page = RegRT(browser)
    t_reg_page.reg_code(valid_code)

    t_reg_page = RegRTExpectations(browser)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_expect_surname(), ""


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
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_expect_name(), "Произошла перенаправление на получение кода регистрации с некорректными данными"


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
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_expect_surname(), "Произошла перенаправление на получение кода регистрации с некорректными данными"


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
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_expect_address(), "Произошла перенаправление на получение кода с некорректными данными"


@pytest.mark.norm
@pytest.mark.parametrize("password", [unicode_password, short_password, long_password, empty_form,
                                      only_letter_password, lower_password, upper_password, cyrillic_password],
                         ids=["unicode_password", "short_password", "long_password", "empty_form",
                                      "only_letter_password", "lower_password", "upper_password", "cyrillic_password"])
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
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_expect_password(), "Произошла перенаправление на получение кода с некорректными данными"


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
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_expect_password_confirm(), "Произошла перенаправление на регистрацию с некорректными данными"


@pytest.mark.norm
def test_reg_slogan(browser, request):
    """ТЕСТ 1-08 на наличие слогана РТ"""
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()

    t_reg_page = RegRTExpectations(browser)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_expect_slogan(), "Отсутствие слогана РТ"


@pytest.mark.skip(reason="Требуется зарегистрированный аккаунт")
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
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_expect_address_reg(), "Ошибка с регистрацией одинаковых данных"


@pytest.mark.norm
@pytest.mark.parametrize("invalid_first_name",
                         [
                             (russian_generate_string) * 1
                             , (russian_generate_string) * 100
                             , (russian_generate_string) * 256
                             , (empty), (numbers)
                             , (latin_generate_string)
                             , (chinese_chars), (special_chars)
                         ],
                         ids=
                         [
                             'russ_symbols=1', 'russ_symbols=100', 'russ_symbols=256',
                             'empty', 'numbers', 'latin_symbols', 'chinese_symbols', 'special_symbols'
                         ])
def test_first_name_invalid_data(browser, invalid_first_name, request):
    """Тест 1-09 ввод в поля "Имя" формы "Регистрация" невалидными значениями:
    пустое значение;
    буквы кириллицы в количестве 1 ; 100 ; 256 ;
    латиницы буквы; китайские иероглифы; спецсимволы; числа."""
    t_reg_page = RegRT(browser)
    t_reg_page.go_to_site()
    t_reg_page.reg_page()
    t_reg_page.reg_first_name(invalid_first_name)
    t_reg_page.reg_last_name(valid_last_name)
    t_reg_page.reg_address(valid_email)
    t_reg_page.reg_password(valid_password)
    t_reg_page.reg_password_confirm(valid_password_confirm)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(test).png')
    t_reg_page.reg_button()

    t_reg_page = RegRTExpectations(browser)
    browser.save_screenshot(f'screenshots_registr/{request.node.name}_{t_reg_page.timetest()}(expect).png')
    assert t_reg_page.reg_expect_name(), "Произошла перенаправление на получение кода регистрации с некорректными данными"


