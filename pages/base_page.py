class BasePage():
    def __init__(self, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
