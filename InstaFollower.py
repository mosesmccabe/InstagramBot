from selenium import webdriver

# ---- Optional - add options to keep the webpage open ----
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get(url="https://www.instagram.com/accounts/login/")

    def find_followers(self):
        pass

    def follow(self):
        pass