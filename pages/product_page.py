from selenium.webdriver.common.by import By
from base.base_class import Base
from utilites.utilites import Utils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Product_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product = "//h1[@id='pagetitle']"                                # Локатор продукта
    add_cart = "(//div[@data-basket-action='add'])[3]"               # Локатор  кнопка добавления в корзину
    basket = "(//span[@class='sale-basket-small-tab-wrapper'])[2]"   # Локатор корзины

    # Getters
    """Метод получения продукта"""
    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    """Метод получения кнопки добавления в корзину"""
    def get_add_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_cart)))

    """Метод получения корзины"""
    def get_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket)))

    # Actions
    """Метод нажатия на кнопку добавления в корзину"""
    def click_add_cart(self):
        self.get_add_cart().click()
        print("Click add cart")

    """Метод нажатия на кнопку корзины"""
    def click_basket(self):
        self.get_basket().click()
        print("Click basket")

    # Methods
    """Метод перехода в корзину"""
    def add_to_cart(self):
        ut = Utils(self.driver)
        ut.write_in_text_file(self.get_product().text)
        self.click_add_cart()
        self.click_basket()