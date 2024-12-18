from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.the_store_after_search import TheStoreAfterSearch
from pages.the_store_before_search import TheStoreBeforeSearch
from pages.product_page import Product_Page
from pages.cart_page import Cart_Page
from pages.order_page import Order_Page

"""Тест покупки смартфона"""
def test_buy_smartphone(pre_set):

    ChromeDriverManager().install()
    driver = webdriver.Chrome()

    tsas = TheStoreAfterSearch(driver)
    tsas.go_to_smartphones()

    tsbs = TheStoreBeforeSearch(driver)
    tsbs.select_test_smartphone()

    pp = Product_Page(driver)
    pp.add_to_cart()

    cp = Cart_Page(driver)
    cp.checkout_product()

    op = Order_Page(driver)
    op.make_order()

"""Тест покупки телевизора"""
def test_buy_tv(pre_set):

    ChromeDriverManager().install()
    driver = webdriver.Chrome()

    tsas = TheStoreAfterSearch(driver)
    tsas.go_to_tv()

    tsbs = TheStoreBeforeSearch(driver)
    tsbs.select_test_tv()

    pp = Product_Page(driver)
    pp.add_to_cart()

    cp = Cart_Page(driver)
    cp.checkout_product()

    op = Order_Page(driver)
    op.make_order()

