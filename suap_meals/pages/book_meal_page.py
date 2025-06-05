from selenium.webdriver.common.by import By
from suap_meals.utils import wait_for_element


class SuapBookMealPage:
    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.url = "https://suap.ifpi.edu.br/ae/refeicoes-do-dia/"
        self.book_meal_button_xpath = "//a[contains(@href, '/ae/reservar-refeicao/')]"

    def book_meal(self):
        self.web_driver.get(self.url)

        book_meal_button = wait_for_element(
            self.web_driver, By.XPATH, self.book_meal_button_xpath
        )
        book_meal_button.click()
