from selenium.webdriver.common.by import By
from base.base_class import Base
from utilites.utilites import Utils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TheStoreAfterSearch(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    url = "https://masterbel.ru/"                                                                       # Адрес сайта
    catalog = "//i[@class='far fa-bars']"                                                               # Локатор каталога
    close_banner = "//button[@class='cookie-notification__accept-btn']"                                 # Локатор кнопки закрытия баннера
    category_smartphones = "(//a[@class='menu-submenu-section-item-wrapper intec-cl-text-hover'])[1]"   # Локатор категории смартфоны
    category_tv = "(//a[@class='menu-submenu-section-image intec-image-effect'])[4]"                    # Локатор категории телевизоры

    # Getters
    """Метод получения кнопки каталог"""
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    """Метод получения кнопки закрытия баннера"""
    def get_close_banner(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_banner)))

    """Метод получения категории смартфоны"""
    def get_category_smartphones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_smartphones)))

    """Метод получения категории телевизоры"""
    def get_category_tv(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_tv)))

    # Actions
    """Метод нажатия кнопки каталог"""
    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click Category Button")

    """Метод нажатия кнопки закрытия баннера"""
    def click_close_banner(self):
        self.get_close_banner().click()
        print("Click Close Banner")

    """Метод нажатия категории смартфоны"""
    def click_category_smartphones(self):
        self.get_category_smartphones().click()
        print("Click Category Smartphones")

    """Метод нажатия категории телевизоры"""
    def click_category_tv(self):
        self.get_category_tv().click()
        print("Click Category TV")

    # Methods
    """Метод перехода в категорию смартфоны"""
    def go_to_smartphones(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.get_current_url()
        self.click_close_banner()
        ut = Utils(self.driver)
        ut.move_to_element_on_page(self.catalog)
        self.click_category_smartphones()
        print("Вы перешли в раздел 'Смартфоны и планшеты + гаджеты'")

    """Метод перехода в категорию телевизоры"""
    def go_to_tv(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.get_current_url()
        self.click_close_banner()
        ut = Utils(self.driver)
        ut.move_to_element_on_page(self.catalog)
        self.click_category_tv()
        print("Вы перешли в раздел 'Телевизоры'")

