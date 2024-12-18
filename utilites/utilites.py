from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utils():
    def __init__(self, driver):
        self.driver = driver
    """Метод наведения мыши на элемент"""
    def move_to_element_on_page(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, element)))
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH,element)
        actions.move_to_element(element).perform()

    """Метод записи в текстовый файл"""
    def write_in_text_file(self, element_product):
        with open("product.txt", "a+", encoding= "utf-8") as file:
            file.write(element_product + "\n")

    """Метод очистки текстового файла"""
    def clear_text_file(self):
        with open("product.txt", "w+", encoding= "utf-8") as file:
            file.write("")

    """Метод сравнения названия продуктов из текстового файла"""
    def assert_products(self):
        with open("product.txt", 'r', encoding= "utf-8") as file:
            line1 = file.readline().replace("\n","")
            print(line1.replace("\n",""))
            line2 = file.readline().replace("\n","")
            print(line2.replace("\n",""))
        if line1 == line2:
            print("Products compare")
        else:
            assert False, "Products no compare"


