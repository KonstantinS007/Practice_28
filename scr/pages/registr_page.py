#!python
# coding: utf8
import pytest
import selenium
from datetime import datetime
from .base import BasePage
from scr.settings import valid_email
from .locators import RTRegLocators


# тестовые методы для данных при регистрации
class RegRT(BasePage):
    def reg_page(self):
        reg_link = self.find_element(RTRegLocators.LOCATOR_RT_REG_LINK)
        reg_link.click()
        return reg_link

    def reg_first_name(self, first_name):
        reg_form_name = self.find_element(RTRegLocators.LOCATOR_RT_REG_FIRST_NAME)
        reg_form_name.click()
        reg_form_name.send_keys(first_name)
        return reg_form_name

    def reg_last_name(self, last_name):
        reg_form_name = self.find_element(RTRegLocators.LOCATOR_RT_REG_LAST_NAME)
        reg_form_name.click()
        reg_form_name.send_keys(last_name)
        return reg_form_name

    def reg_address(self, address):
        reg_form_address = self.find_element(RTRegLocators.LOCATOR_RT_REG_ADDRESS)
        reg_form_address.click()
        reg_form_address.send_keys(address)
        return reg_form_address

    def reg_password(self, password):
        reg_form_password = self.find_element(RTRegLocators.LOCATOR_RT_REG_PASSWORD)
        reg_form_password.click()
        reg_form_password.send_keys(password)
        return reg_form_password

    def reg_password_confirm(self, password_confirm):
        reg_form_password_confirm = self.find_element(RTRegLocators.LOCATOR_RT_REG_PASSWORD_CONFIRM)
        reg_form_password_confirm.click()
        reg_form_password_confirm.send_keys(password_confirm)
        return reg_form_password_confirm

    def reg_button(self):
        reg_form_button = self.find_element(RTRegLocators.LOCATOR_RT_REG_BUTTON)
        reg_form_button.click()
        return reg_form_button

    def reg_code(self, email_code):
        reg_email_code = self.find_element(RTRegLocators.LOCATOR_RT_REG_EMAIL_CODE)
        reg_email_code.click()
        reg_email_code.send_keys(email_code)
        return reg_email_code
        # ручной ввод кода, полученного на электронную почту

    def timetest(self):
        now = datetime.now()
        timetest = f"{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}"
        return timetest


# тестовые методы для проверки ожиданий и результатов при регистрации
class RegRTExpectations(BasePage):
    def reg_expect_reg_title(self):
        reg_expect = self.find_element(RTRegLocators.LOCATOR_RT_REG_EXPECT_REG_TITLE)
        reg_expect_reg_title = reg_expect.text == "Регистрация"
        return reg_expect_reg_title

    def reg_expect_slogan(self):
        reg_expect = self.find_element(RTRegLocators.LOCATOR_RT_REG_SLOGAN)
        reg_expect_slogan = reg_expect.text == "Персональный помощник в цифровом мире Ростелекома"
        return reg_expect_slogan

    def reg_expect_valid_code(self):
        reg_expect = self.find_element(RTRegLocators.LOCATOR_RT_REG_EXPECT_VALID_CODE)
        reg_expect_code = reg_expect.text == f"Kод подтверждения отправлен на адрес {valid_email}"
        return reg_expect_code

    def reg_expect_name(self):
        reg_expect = self.find_element(RTRegLocators.LOCATOR_RT_REG_EXPECT_NAME)
        reg_expect_name = reg_expect.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
        return reg_expect_name

    def reg_expect_surname(self):
        reg_expect = self.find_element(RTRegLocators.LOCATOR_RT_REG_EXPECT_SURNAME)
        reg_expect_surname = reg_expect.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
        return reg_expect_surname

    def reg_expect_address(self):
        reg_expect = self.find_element(RTRegLocators.LOCATOR_RT_REG_EXPECT_ADDRESS)
        reg_expect_address = reg_expect.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, " \
                                                "или email в формате example@email.ru"
        return reg_expect_address

    def reg_expect_password(self):
        reg_expect = self.find_element(RTRegLocators.LOCATOR_RT_REG_EXPECT_PASSWORD)
        reg_expect_password = reg_expect.text == "Длина пароля должна быть не менее 8 символов" \
            or "Длина пароля должна быть не более 20 символов" or "Пароль должен содержать хотя бы одну заглавную букву"\
            or "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру" \
            or "Пароль должен содержать хотя бы одну прописную букву" or "Пароль должен содержать только латинские буквы" \

        return reg_expect_password

    def reg_expect_password_confirm(self):
        reg_expect = self.find_element(RTRegLocators.LOCATOR_RT_REG_EXPECT_PASSWORD_CONFIRM)
        reg_expect_password_confirm = reg_expect.text == "Пароли не совпадают"\
            or "Длина пароля должна быть не менее 8 символов"
        return reg_expect_password_confirm

    def reg_expect_code_send(self):
        reg_expect = self.find_element(RTRegLocators.LOCATOR_RT_REG_EXPECT_CODE_SEND)
        reg_expect_code_send = reg_expect.text == f"Kод подтверждения отправлен на адрес {valid_email}"
        return reg_expect_code_send

    def reg_expect_code_invalid(self):
        reg_expect = self.find_element(RTRegLocators.LOCATOR_RT_REG_EXPECT_CODE_INVALID)
        reg_expect_code_invalid = reg_expect.text == "Неверный код. Повторите попытку"
        return reg_expect_code_invalid

    def reg_expect_address_reg(self):
        reg_expect = self.find_element(RTRegLocators.LOCATOR_RT_REG_EXPECT_ADDRESS_REG)
        reg_expect_address_reg = reg_expect.text == "Учётная запись уже существует"
        return reg_expect_address_reg

    def auth_expect_captcha_fail(self):
        auth_expect = None
        if auth_expect == self.is_presented(RTRegLocators.LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL) is None:
            pass
        else:
            auth_expect = self.find_element(RTRegLocators.LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL)
            auth_expect_captcha_fail = auth_expect.text == "Неверно введен текст с картинки"
            return auth_expect_captcha_fail

    def timetest(self):
        now = datetime.now()
        timetest = f"{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}"
        return timetest
