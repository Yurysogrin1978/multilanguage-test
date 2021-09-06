import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

try:
    def test_button_add_to_cart_is_visible(browser):
        browser.get(link)
        button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
        print(f"Button 'Add to cart ({button.text})' is present")
        assert button, "Button 'Add to cart' not found!"
finally:
    time.sleep(30)
