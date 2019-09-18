class text_to_change:

    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        by, value = self.locator
        actual_text = driver.find_element(by, value).text
        return actual_text != self.text
