from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TheStoreBeforeSearch(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    price_from = "//input[@id='arrFilter_P3_MIN']"                              # Локатор поля цены от
    price_after = "//input[@id='arrFilter_P3_MAX']"                             # Локатор поля цены до
    select_manufacturer_smartphone = "(//a[@class='detail-link'])[6]"           # Локатор выбора производителя смартфонов
    select_manufacturer_tv = "(//a[@class='detail-link'])[9]"                   # Локатор выбора производителя телевизоров
    select_product = "(//a[@class='section-item-name intec-cl-text-hover'])[1]" # Локатор выбора продукта

    # Getters
    """Метод получения поля цены от"""
    def get_price_from(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_from)))

    """Метод получения поля цены до"""
    def get_price_after(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_after)))

    """Метод получения выбора производителя смартфонов"""
    def get_select_manufacturer_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_manufacturer_smartphone)))

    """Метод получения выбора производителя телевизоров"""
    def get_select_manufacturer_tv(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_manufacturer_tv)))

    """Метод получения выбора продукта"""
    def get_select_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product)))

    # Actions
    """Метод выбора поля цены от"""
    def select_price_from(self):
        self.get_price_from().send_keys("10000")
        print("Select price from")

    """Метод выбора поля цены до"""
    def select_price_after(self):
        self.get_price_after().send_keys("40000")
        print("Select price after")

    """Метод выбора производителя смартфонов"""
    def click_select_manufacturer_smartphone(self):
        self.get_select_manufacturer_smartphone().click()
        print("Click select manufacturer smartphone")

    """Метод выбора производителя телевизоров"""
    def click_select_manufacturer_tv(self):
        self.get_select_manufacturer_tv().click()
        print("Click select manufacturer tv")

    """Метод выбора продукта"""
    def click_select_product(self):
        self.get_select_product().click()
        print("Click select product")

    # Methods
    """Метод выбора смартфона"""
    def select_test_smartphone(self):
        self.click_select_manufacturer_smartphone()
        self.select_price_from()
        self.select_price_after()
        self.click_select_product()

    """Метод выбора телевизора"""
    def select_test_tv(self):
        self.click_select_manufacturer_tv()
        self.select_price_from()
        self.select_price_after()
        self.click_select_product()
