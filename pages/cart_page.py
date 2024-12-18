from selenium.webdriver.common.by import By
from base.base_class import Base
from utilites.utilites import Utils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    # Locators
    assert_product = "//a[@class='intec-cl-text-hover']"            # Локатор для проверки продукта
    checkout = "//button[@data-entity='basket-checkout-button']"    # Локатор для кнопки checkout

    # Getters
    """Метод получения продукта"""
    def get_assert_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_product)))

    """Метод получения кнопки checkout"""
    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout)))

    # Actions
    """Метод нажатия кнопки checkout"""
    def click_checkout(self):
        self.get_checkout().click()
        print("Click checkout")

    # Methods
    """Метод для перехода на оформление товара"""
    def checkout_product(self):
        ut = Utils(self.driver)
        ut.write_in_text_file(self.get_assert_product().text)
        ut.assert_products()
        ut.clear_text_file()
        self.click_checkout()
