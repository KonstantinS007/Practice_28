
from selenium.webdriver.common.by import By


# локаторы сайта для страницы авторизации
class RTAuthLocators:
    LOCATOR_RT_AUTH_TYPE_PHONE = (By.ID, "t-btn-tab-phone")  # Кнопка телефон
    LOCATOR_RT_AUTH_TYPE_EMAIL = (By.ID, "t-btn-tab-mail")  # Кнопка почта
    LOCATOR_RT_AUTH_TYPE_LOGIN = (By.ID, "t-btn-tab-login")  # Кнопка логин
    LOCATOR_RT_AUTH_TYPE_LS = (By.ID, "t-btn-tab-ls")  # Кнопка лицевой счёт
    LOCATOR_RT_AUTH_LOGIN = (By.ID, "username")  # Поле ввода логина(тел.поч.счёт)
    LOCATOR_RT_AUTH_PASSWORD = (By.ID, "password")  # Поле ввода пароля
    LOCATOR_RT_AUTH_BUTTON = (By.ID, "kc-login")  # Кнопка войти
    LOCATOR_RT_AUTH_CAPTCHA_IMG = (By.XPATH, "//img[@alt='Captcha']")  # Картинка капчи
    LOCATOR_RT_AUTH_CAPTCHA_ANSWER = (By.ID, "captcha")  # Поле ввода капчи
    LOCATOR_RT_AUTH_VK_TYPE = (By.ID, "oidc_vk")  # Ссылка на вход через VK
    LOCATOR_RT_AUTH_YANDEX_TYPE = (By.ID, "oidc_ya")  # Ссылка на вход через Yandex
    LOCATOR_RT_AUTH_OK_TYPE = (By.ID, "oidc_ok")  # Ссылка на вход через OK
    LOCATOR_RT_AUTH_GOOGLE_TYPE = (By.ID, "oidc_google")  # Ссылка на вход через Google
    LOCATOR_RT_AUTH_MAIL_TYPE = (By.ID, "oidc_mail")  # Ссылка на вход через Mail
    # локаторы сайта для проверки ожиданий со страницы авторизации
    LOCATOR_RT_AUTH_EXPECT_PHONE_DEFOLT_LOGIN = (By.XPATH, "//span[contains(text(),'Мобильный телефон')]")  # Элемент по умолчанию в поле вода на Мобильный телефон
    LOCATOR_RT_AUTH_EXPECT_SLOGAN = (By.CSS_SELECTOR, ".what-is__desc")  # Элемент Слоган РТ
    LOCATOR_RT_AUTH_EXPECT_TITLE = (By.CSS_SELECTOR, ".card-container__title")  # Элемент Авторизация
    LOCATOR_RT_AUTH_EXPECT_LOGIN = (By.CSS_SELECTOR, ".rt-input-container__meta.rt-input-container__meta--error")
    # Предупреждение об неверном значения в поле ввода логина(тел.поч.счёт)
    LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL = (By.ID, "form-error-message")  # Предупреждение о неверном вводе капчи
    LOCATOR_RT_AUTH_EXPECT_AUTH_FAIL = (By.ID, "form-error-message")  # Предупреждение о неверном вводе авторизации
    LOCATOR_RT_AUTH_EXPECT_AUTH_NAME = (By.CSS_SELECTOR, ".user-name__first-patronymic")  # Элемент user-name при авторизации
    LOCATOR_RT_AUTH_EXPECT_AUTH_SURNAME = (By.CSS_SELECTOR, ".user-name__last-name")  # Элемент last-name при авторизации
    # локаторы сайтов соц.сетей на авторизацию
    LOCATOR_RT_AUTH_EXPECT_MAIL_TITLE = (By.XPATH, "//span[contains(text(),'Мой Мир@Mail.Ru')]")  # Элемент страницы Mail
    LOCATOR_RT_AUTH_EXPECT_GOOGLE_TITLE = (By.XPATH, "//div[contains(text(),'Войдите в аккаунт Google')]")  # Элемент страницы Google
    LOCATOR_RT_AUTH_EXPECT_OK_TITLE = (By.XPATH, "//div[contains(text(),'Одноклассники')]")  # Элемент страницы OK
    LOCATOR_RT_AUTH_EXPECT_YANDEX_TITLE = (By.CLASS_NAME, "Logo Logo_ya")  # Элемент страницы Yandex
    LOCATOR_RT_AUTH_EXPECT_VK_TITLE = (By.XPATH, "//b[contains(text(),'ВКонтакте')]")  # Элемент страницы VK

# локаторы сайта для страницы регистрации
class RTRegLocators:
    LOCATOR_RT_REG_CONTEINER = (By.CSS_SELECTOR, "#page-right > div > div > div > form > div.rt-select.rt-select--search.register-form__dropdown > div > div > span.rt-input__mask")
    LOCATOR_RT_REG_SLOGAN = (By.CSS_SELECTOR, ".what-is__desc")  # Элемент Слоган РТ
    LOCATOR_RT_REG_LINK = (By.ID, "kc-register")  # Элемент Зарегистрироваться
    LOCATOR_RT_REG_FIRST_NAME = (By.XPATH, "//input[@name='firstName']")  # Поле ввода Имя
    LOCATOR_RT_REG_LAST_NAME = (By.XPATH, "//input[@name='lastName']")  # Поле ввода Фамилия
    LOCATOR_RT_REG_REGION_TEXT = (By.CSS_SELECTOR, "#page-right > div > div > div > form > div.rt-select.rt-select--search.register-form__dropdown > div > div > span.rt-input__mask > span.rt-input__mask-start")
    LOCATOR_RT_REG_REGION = (By.XPATH, "//div[@class='rt-input-container rt-select__input']//input[@type='text']")  # Поле ввода региона
    LOCATOR_RT_REG_ADDRESS = (By.XPATH, "//input[@id='address']")  # Поле ввода почты и телефона
    LOCATOR_RT_REG_PASSWORD = (By.ID, "password")  # Поле ввода пароля
    LOCATOR_RT_REG_PASSWORD_CONFIRM = (By.ID, "password-confirm")  # Поле ввода повтора пароля
    LOCATOR_RT_REG_BUTTON = (By.XPATH, "//button[@name='register']")  # Кнопка Зарегистрироваться
    LOCATOR_RT_REG_EMAIL_CODE = (By.XPATH, "//input[@id='rt-code-0']")  # Поле ввода смс регистрации

    # локаторы сайта для проверки ожиданий со страницы регистрации
    LOCATOR_RT_REG_EXPECT_REG_TITLE = (By.CSS_SELECTOR, ".card-container__title")  # Элемент Регистрация
    LOCATOR_RT_REG_EXPECT_VALID_CODE = (By.CSS_SELECTOR, ".register-confirm-form-container__desc")  # элемент с веденой почтой регистрации
    LOCATOR_RT_REG_EXPECT_NAME = (By.CSS_SELECTOR, ".rt-input-container__meta, .rt-input-container__meta--error")  # Предупреждение об ошибке в поле ввода Имя
    LOCATOR_RT_REG_EXPECT_SURNAME = (By.CSS_SELECTOR, ".rt-input-container__meta, .rt-input-container__meta--error")  # Предупреждение об ошибке в поле ввода Фамилия
    LOCATOR_RT_REG_EXPECT_ADDRESS = (By.CSS_SELECTOR, ".rt-input-container__meta, .rt-input-container__meta--error")  # Предупреждение об ошибке в поле ввода адресс
    LOCATOR_RT_REG_EXPECT_PASSWORD = (
    By.CSS_SELECTOR, ".rt-input-container__meta, .rt-input-container__meta--error")  # Предупреждение об ошибке в поле ввода пароля
    LOCATOR_RT_REG_EXPECT_PASSWORD_CONFIRM = \
        (By.CSS_SELECTOR, ".rt-input-container__meta.rt-input-container__meta--error")  # Предупреждение об ошибке в поле ввода повтора пароля
    LOCATOR_RT_REG_EXPECT_CODE_SEND = (By.CSS_SELECTOR, ".register-confirm-form-container__desc")   # Поле ввода кода
    LOCATOR_RT_REG_EXPECT_CODE_INVALID = (By.XPATH, "//span[@id='form-error-message']")  # Предупреждение об ошибке в поле ввода кода
    LOCATOR_RT_REG_EXPECT_ADDRESS_REG = (By.CSS_SELECTOR, ".card-modal__title")  # Предупреждение об ошибке в поле ввода адресс
    LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL = (By.ID, "form-error-message")  # Предупреждение об ошибке в поле капчи

# локаторы сайта для страницы восстановления пароля
class RTPassRecLocators:
    LOCATOR_RT_Pass_Rec_SLOGAN = (By.CSS_SELECTOR, ".what-is__desc")  # Элемент Слоган РТ
    LOCATOR_RT_PASS_REC_LINK = (By.ID, "forgot_password")  # Кнопка забыл пароль
    LOCATOR_RT_PASS_REC_TYPE_PHONE = (By.ID, "t-btn-tab-phone")  # Кнопка телефон
    LOCATOR_RT_PASS_REC_TYPE_EMAIL = (By.ID, "t-btn-tab-mail")  # Кнопка почта
    LOCATOR_RT_PASS_REC_TYPE_LOGIN = (By.ID, "t-btn-tab-login")  # Кнопка логин
    LOCATOR_RT_PASS_REC_TYPE_LS = (By.ID, "t-btn-tab-ls")  # Кнопка лиц. счёт
    LOCATOR_RT_PASS_REC_LOGIN = (By.ID, "username")  # Поле ввода логина(тел.поч.счёт)
    LOCATOR_RT_PASS_REC_LOGIN_TEXT = (By.CSS_SELECTOR, "#page-right > div > div > div > form > div.tabs-input-container > div.rt-input-container.tabs-input-container__login > div > span.rt-input__placeholder")
    LOCATOR_RT_PASS_REC_CAPTCHA_IMG = (By.XPATH, "//img[@alt='Captcha']")  # Картинка капчи
    LOCATOR_RT_PASS_REC_CAPTCHA_ANSWER = (By.ID, "captcha")  # Поле ввода капчи

    LOCATOR_RT_PASS_REC_BUTTON_CONTINUE = (By.ID, "reset")  # Кнопка Продолжить
    LOCATOR_RT_PASS_REC_CODE_EMAIL = (By.XPATH, "//input[@value='email']//ancestor::label//span[@class='rt-radio__circle']")  # Переключатель по почте восстановление
    LOCATOR_RT_PASS_REC_CODE_PHONE = (By.XPATH, "//input[@value='sms']//ancestor::label//span[@class='rt-radio__circle']")  # Переключатель по смс восстановление
    LOCATOR_RT_PASS_REC_BUTTON_CONTINUE_RESET = \
        (By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded reset-choice-form__reset-btn']")  # Кнопка Продолжить
    LOCATOR_RT_PASS_REC_CODE_INPUT = (By.XPATH, "//input[@id='rt-code-0']")   # Поле ввода кода
    LOCATOR_RT_PASS_REC_NEW_PASSWORD = (By.ID, "password-new")   # Поле ввода нового пароля
    LOCATOR_RT_PASS_REC_NEW_PASSWORD_CONFIRM = (By.ID, "password-confirm")   # Поле ввода повтора нового пароля
    LOCATOR_RT_PASS_REC_BUTTON_SAVE_NEW_PASSWORD = (By.ID, "t-btn-reset-pass")  # Кнопка Продолжить
    LOCATOR_RT_PASS_REC_BUTTON_RESET_BACK = (By.XPATH, "//button[@id='reset-back']")

# локаторы сайта для проверки ожиданий со страницы восстановления пароля
    LOCATOR_RT_PASS_REC_EXPECT_PASS_REC_TITLE = (By.CSS_SELECTOR, ".card-container__title")  # Элемент Восстановление пароля
    LOCATOR_RT_PASS_REC_EXPECT_LOGIN = (By.CSS_SELECTOR, ".rt-input-container__meta.rt-input-container__meta--error")  # Предупреждение об ошибке в поле ввода некорректные
    LOCATOR_RT_PASS_REC_EXPECT_PASS_REC_FAIL = (By.ID, "form-error-message")# Предупреждение об ошибке в поле ввода невалидные
    LOCATOR_RT_PASS_REC_EXPECT_CODE_TITLE = (By.CSS_SELECTOR, "#page-right > div > div > div > form > div.rt-select.rt-select--search.register-form__dropdown > div > div > span.rt-input__mask > span.rt-input__mask-start")  # Элемент Восстановление пароля страницы ввода кода.card-container__title
    LOCATOR_RT_PASS_REC_EXPECT_CODE_SEND = (By.CSS_SELECTOR, ".card-container__desc")   # Поле ввода кода
    LOCATOR_RT_PASS_REC_EXPECT_CODE_INVALID = (By.ID, "form-error-message")  # Предупреждение об ошибке в поле ввода кода
    LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD_FORM = (By.CSS_SELECTOR, ".card-container__desc")  # Элемент Правила востановления пароля
    LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD_IS_OLD = (By.ID, "form-error-message")  # Предупреждение об ошибке в поле ввода пароля похожего на старый
    LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD_CONFIRM = (By.ID, "form-error-message")  # Предупреждение об ошибке в поле ввода пароля
    LOCATOR_RT_PASS_REC_EXPECT_NEW_PASSWORD = (By.CSS_SELECTOR, ".rt-input-container__meta.rt-input-container__meta--error")  # Предупреждение об ошибке в поле ввода пароля Пароли не совпадают
    LOCATOR_RT_PASS_REC_EXPECT_AUTH_NEW = (By.CSS_SELECTOR, ".card-container__title")  # Элемент Восстановление пароля страницы изменеия пароля
    LOCATOR_RT_AUTH_EXPECT_CAPTCHA_FAIL = (By.ID, "form-error-message")  # Предупреждение об ошибке в поле капчи
