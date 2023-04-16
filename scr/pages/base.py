
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# функции, описывающие операции, проводимые на сайте РТ
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru/"

    # переход на сайт
    def go_to_site(self):
        return self.driver.get(self.base_url)

    def screenshot(self, file_name='screenshot.png'):
        self.driver.save_screenshot(file_name)

    # поиск локатора на странице
    def find_element(self, locator, time=10):  # self.driver.find_element(*locator)
        return WebDriverWait(self.driver, time).\
          until(EC.presence_of_element_located(locator), message=f"Not find {locator}")

    # проверка присутствия локатора на странице
    def is_presented(self, locator, time=10):
        element = None
        try:
            element = WebDriverWait(self.driver, time).\
                until(EC.presence_of_element_located(locator), message=f"Not find {locator}")
        except:
            pass
        return element

    # переключатель вкладок
    def switch_to_numer_window(self, numer):
        return self.driver.switch_to.window(self.driver.window_handles[numer])

    # открывашка скрытых элементов
    def display_container(self, element):
        return self.driver.execute_script("arguments[0].style.display = 'block';", element)
