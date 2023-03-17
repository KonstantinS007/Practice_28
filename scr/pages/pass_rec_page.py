from datetime import datetime
from .base import BasePage
from scr.settings import valid_email_confirm, valid_phone_confirm
from .locators import RTPassRecLocators


# тестовые методы для данных при восстановлении пароля
class PassRecRT(BasePage):
    def pass_rec_page(self):
        pass_rec_link = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_LINK)
        pass_rec_link.click()
        return pass_rec_link

    def pass_rec_type_phone(self):
        pass_rec_type_phone = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_TYPE_PHONE)
        pass_rec_type_phone.click()
        return pass_rec_type_phone

    def pass_rec_type_email(self):
        pass_rec_type_email = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_TYPE_EMAIL)
        pass_rec_type_email.click()
        return pass_rec_type_email

    def pass_rec_type_login(self):
        pass_rec_type_login = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_TYPE_LOGIN)
        pass_rec_type_login.click()
        return pass_rec_type_login

    def pass_rec_type_ls(self):
        pass_rec_type_ls = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_TYPE_LS)
        pass_rec_type_ls.click()
        return pass_rec_type_ls

    def pass_rec_login(self, login):
        pass_rec_login = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_LOGIN)
        pass_rec_login.click()
        pass_rec_login.clear()
        pass_rec_login.send_keys(login)
        return pass_rec_login


    def pass_rec_button_continue(self):
        pass_rec_button_continue = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_BUTTON_CONTINUE)
        pass_rec_button_continue.click()
        return pass_rec_button_continue

    def pass_rec_code_email(self):
        pass_rec_code_email = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_CODE_EMAIL)
        pass_rec_code_email.click()
        return pass_rec_code_email

    def pass_rec_code_phone(self):
        pass_rec_code_phone = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_CODE_PHONE)
        pass_rec_code_phone.click()
        return pass_rec_code_phone

    def pass_rec_button_continue_reset(self):
        pass_rec_button_continue_reset = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_BUTTON_CONTINUE_RESET)
        pass_rec_button_continue_reset.click()
        return pass_rec_button_continue_reset

    def pass_rec_code_input_invalid_code(self, email_code):
        pass_rec_code_input_invalid_code = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_CODE_INPUT)
        pass_rec_code_input_invalid_code.click()
        pass_rec_code_input_invalid_code.send_keys(email_code)
        return pass_rec_code_input_invalid_code

    def pass_rec_code_input_valid_code(self):
        pass_rec_code_input_valid_code = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_CODE_INPUT)
        pass_rec_code_input_valid_code.click()
        # ручной ввод кода, полученного на электронную почту или по смс
        return pass_rec_code_input_valid_code

    def pass_rec_new_password(self, password):
        pass_rec_form_new_password = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_NEW_PASSWORD)
        pass_rec_form_new_password.click()
        pass_rec_form_new_password.send_keys(password)
        return pass_rec_form_new_password

    def pass_rec_new_password_confirm(self, password_confirm):
        pass_rec_form_new_password_confirm = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_NEW_PASSWORD_CONFIRM)
        pass_rec_form_new_password_confirm.click()
        pass_rec_form_new_password_confirm.send_keys(password_confirm)
        return pass_rec_form_new_password_confirm

    def pass_rec_button_save_new_password(self):
        pass_rec_new_password_button_save = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_BUTTON_SAVE_NEW_PASSWORD)
        pass_rec_new_password_button_save.click()
        return pass_rec_new_password_button_save


# тестовые методы для проверки ожиданий и результатов при восстановлении пароля
class PassRecRTExpectations(BasePage):
    def pass_rec_expect_pass_rec_title(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_PASS_REC_TITLE)
        pass_rec_expect_pass_rec_title = pass_rec_expect.text == "Восстановление пароля"
        return pass_rec_expect_pass_rec_title

    def reg_expect_slogan(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_Pass_Rec_SLOGAN)
        pass_rec_expect_slogan = pass_rec_expect.text == "Персональный помощник в цифровом мире Ростелекома"
        return pass_rec_expect_slogan

    def pass_rec_expect_login(self):
        pass_rec_expect = None
        if pass_rec_expect == self.is_presented(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_LOGIN) is None:
            pass
        else:
            pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_LOGIN)
            pass_rec_expect_login = pass_rec_expect.text == "Введите номер телефона" or "Введите адрес, указанный при регистрации" \
                or "Введите логин, указанный при регистрации" or "Введите номер вашего лицевого счета" \
                or "Неверный формат телефона" or "Проверьте, пожалуйста, номер лицевого счета"
            return pass_rec_expect_login

    def pass_rec_expect_pass_rec_fail(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_PASS_REC_FAIL)
        pass_rec_expect_code_invalid = pass_rec_expect.text == "Неверный логин или текст с картинки"
        return pass_rec_expect_code_invalid

    def pass_rec_expect_code_title(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_CODE_TITLE)
        pass_rec_expect_code_title = pass_rec_expect.text == "Восстановление пароля"
        return pass_rec_expect_code_title

    def pass_rec_expect_code_send(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_CODE_SEND)
        pass_rec_expect_code_send = pass_rec_expect.text == \
            f"Код подтверждения отправлен на адрес {valid_email_confirm}"\
            or f"Код подтверждения отправлен на номер {valid_phone_confirm}"
        return pass_rec_expect_code_send

    def pass_rec_expect_code_invalid(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_CODE_INVALID)
        pass_rec_expect_code_invalid = pass_rec_expect.text == "Неверный код. Повторите попытку"
        return pass_rec_expect_code_invalid

    def pass_rec_expect_new_password_form(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD_FORM)
        pass_rec_expect_new_password_form = pass_rec_expect.text == "Новый пароль должен содержать от 8 до 20 знаков, " \
            "включать латинские, заглавные и строчные буквы, цифры или специальные символы"
        return pass_rec_expect_new_password_form

    def pass_rec_expect_new_password(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD)
        pass_rec_expect_new_password = pass_rec_expect.text == "Длина пароля должна быть не менее 8 символов" \
            or "Длина пароля должна быть не более 20 символов" or "Пароль должен содержать хотя бы одну заглавную букву"\
            or "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру" or "Пароли не совпадают" \
            or "Пароль должен содержать хотя бы одну прописную букву" or "Пароль должен содержать только латинские буквы"
        return pass_rec_expect_new_password

    def pass_rec_expect_new_password_is_old(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD_IS_OLD)
        pass_rec_expect_new_password_is_old = pass_rec_expect.text == "Этот пароль уже использовался, укажите другой пароль"
        return pass_rec_expect_new_password_is_old

    def auth_expect_auth_new(self):
        pass_rec_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_PASS_REC_EXPECT_AUTH_NEW)
        auth_expect_auth_new = pass_rec_expect.text == "Авторизация"
        return auth_expect_auth_new

    def auth_expect_captcha_fail(self):
        auth_expect = None
        if auth_expect == self.is_presented(RTPassRecLocators.LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL) is None:
            pass
        else:
            auth_expect = self.find_element(RTPassRecLocators.LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL)
            auth_expect_captcha_fail = auth_expect.text == "Неверно введен текст с картинки"
            return auth_expect_captcha_fail

    def timetest(self):
        now = datetime.now()
        timetest = f"{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}"
        return timetest

