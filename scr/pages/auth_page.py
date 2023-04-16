
from datetime import datetime
from .base import BasePage
from scr.settings import valid_first_name, valid_last_name
from .locators import RTAuthLocators


# тестовые методы для данных при авторизации
class AuthRT(BasePage):


    def auth_type_phone(self):
        auth_type_phone = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_PHONE)
        auth_type_phone.click()
        return auth_type_phone

    def auth_type_document(self):
        auth_type_document = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_DOCUMENT)
        auth_type_document.click()
        self.switch_to_numer_window(1)
        return auth_type_document

    def auth_type_email(self):
        auth_type_email = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_EMAIL)
        auth_type_email.click()
        return auth_type_email

    def auth_type_login(self):
        auth_type_login = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_LOGIN)
        auth_type_login.click()
        return auth_type_login

    def auth_type_ls(self):
        auth_type_ls = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_LS)
        auth_type_ls.click()
        return auth_type_ls

    def auth_login(self, login):
        auth_form_name = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_LOGIN)
        auth_form_name.click()
        auth_form_name.clear()
        auth_form_name.send_keys(login)
        return auth_form_name

    def auth_password(self, password):
        auth_form_name = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_PASSWORD)
        auth_form_name.click()
        auth_form_name.send_keys(password)
        return auth_form_name

    def auth_button(self):
        auth_form_button = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_BUTTON)
        auth_form_button.click()
        return auth_form_button

    def auth_type_vk(self):
        auth_type_phone = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_VK_TYPE)
        auth_type_phone.click()
        return auth_type_phone

    def auth_type_ok(self):
        auth_type_phone = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_OK_TYPE)
        auth_type_phone.click()
        return auth_type_phone

    def auth_type_google(self):
        auth_type_phone = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_GOOGLE_TYPE)
        auth_type_phone.click()
        return auth_type_phone

    def auth_type_mail(self):
        auth_type_phone = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_MAIL_TYPE)
        auth_type_phone.click()
        return auth_type_phone

    def auth_type_yandex(self):
        auth_type_phone = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_YANDEX_TYPE)
        auth_type_phone.click()
        return auth_type_phone


    def timetest(self):
        now = datetime.now()
        timetest = f"{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}"
        return timetest


# тестовые методы для проверки ожиданий и результатов при авторизации
class AuthRTExpectations(BasePage):

    def auth_expect_auth_page(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_TITLE)
        auth_expect_title = auth_expect.text == "Авторизация"
        return auth_expect_title

    def auth_expect_document_page(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_TYPE_DOCUMENT)
        auth_expect_document = auth_expect.text == "Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»"
        return auth_expect_document

    def auth_expect_type_phone(self):
        auth_type_phone = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_PHONE)
        auth_type_phone = auth_type_phone.text == "Телефон"
        return auth_type_phone

    def auth_expect_type_email(self):
        auth_type_email = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_EMAIL)
        auth_type_email = auth_type_email.text == "Почта"
        return auth_type_email

    def auth_expect_type_login(self):
        auth_type_login = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_LOGIN)
        auth_type_login = auth_type_login.text == "Логин"
        return auth_type_login

    def auth_expect_type_ls(self):
        auth_type_ls = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_TYPE_LS)
        auth_type_ls = auth_type_ls.text == "Лицевой счёт"
        return auth_type_ls

    def auth_expect_auth_slogan(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_SLOGAN)
        auth_expect_slogan = auth_expect.text == "Персональный помощник в цифровом мире Ростелекома"
        return auth_expect_slogan

    def auth_expect_login(self):
        auth_expect = None
        if auth_expect == self.is_presented(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_LOGIN) is None:
            pass
        else:
            auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_LOGIN)
            auth_expect_login = auth_expect.text == "Введите номер телефона" or "Введите адрес, указанный при регистрации" \
                or "Введите логин, указанный при регистрации" or "Введите номер вашего лицевого счета" \
                or "Неверный формат телефона" or "Проверьте, пожалуйста, номер лицевого счета"
            return auth_expect_login

    def auth_expect_captcha_fail(self):
        auth_expect = None
        if auth_expect == self.is_presented(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL) is None:
            pass
        else:
            auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL)
            auth_expect_captcha_fail = auth_expect.text == "Неверно введен текст с картинки"
            return auth_expect_captcha_fail

    def auth_expect_auth_fail(self):
        auth_expect = None
        if auth_expect == self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_AUTH_FAIL) is None:
            pass
        else:
            auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_AUTH_FAIL)
            auth_expect_auth_fail = auth_expect.text == "Неверный логин или пароль"
            return auth_expect_auth_fail

    def auth_expect_name(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_AUTH_NAME)
        auth_expect_name = auth_expect.text == valid_first_name
        return auth_expect_name

    def auth_expect_surname(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_AUTH_SURNAME)
        auth_expect_surname = auth_expect.text == valid_last_name
        return auth_expect_surname

    def timetest(self):
        now = datetime.now()
        timetest = f"{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}"
        return timetest

    def auth_expect_auth_page_vk(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_VK_TITLE)
        auth_expect_title = auth_expect.text == "ВКонтакте"
        return auth_expect_title

    def auth_expect_auth_page_ok(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_OK_TITLE)
        auth_expect_title = auth_expect.text == "Одноклассники"
        return auth_expect_title

    def auth_expect_auth_page_google(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_GOOGLE_TITLE)
        auth_expect_title = auth_expect.text == "Войдите в аккаунт Google"
        return auth_expect_title

    def auth_expect_auth_page_yandex(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_YANDEX_TITLE)
        auth_expect_title = auth_expect.text == "Logo Logo_ya"
        return auth_expect_title

    def auth_expect_auth_page_mail(self):
        auth_expect = self.find_element(RTAuthLocators.LOCATOR_RT_AUTH_EXPECT_MAIL_TITLE)
        auth_expect_title = auth_expect.text == "Мой Мир@Mail.Ru"
        return auth_expect_title



