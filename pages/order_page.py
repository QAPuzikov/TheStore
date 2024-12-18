from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Order_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    # Locators
    name = "//input[@name='ORDER_PROP_1']"              # Локатор поля name
    mail = "//input[@name='ORDER_PROP_2']"              # Локатор поля mail
    phone = "//input[@name='ORDER_PROP_3']"             # Локатор поля phone
    address = "//textarea[@name='ORDER_PROP_7']"        # Локатор поля address
    comment = "//textarea[@name='ORDER_DESCRIPTION']"   # Локатор поля comment

    # Getters
    """Метод получения поля name"""
    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    """Метод получения поля mail"""
    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    """Метод получения поля phone"""
    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    """Метод получения поля address"""
    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    """Метод получения поля comment"""
    def get_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment)))

    # Actions
    """Метод заполнения поля name"""
    def input_name(self):
        self.get_name().send_keys("Дмитрий")
        print("input name")

    """Метод заполнения поля mail"""
    def input_mail(self):
        self.get_mail().send_keys("example@post.ru")
        print("input mail")

    """Метод заполнения поля phone"""
    def input_phone(self):
        self.get_phone().send_keys("+7(900)-000-00-00")
        print("input phone")

    """Метод заполнения поля address"""
    def input_address(self):
        self.get_address().send_keys("г. Дудкино, ул. Пушкина, д. Калатушкина")
        print("input address")

    """Метод заполнения поля comment"""
    def input_comment(self):
        self.get_comment().send_keys("Очень интересное задание")
        print("input comment")

    # Methods
    """Метод покупки товара"""
    def make_order(self):
        self.driver.execute_script("window.scrollTo(0, 600);")
        self.input_name()
        self.input_mail()
        self.input_phone()
        self.input_address()
        self.input_comment()
        self.get_screenshot()

