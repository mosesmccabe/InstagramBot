from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# ---- Optional - add options to keep the webpage open ----
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)

    def login(self, user_ID, pwd):
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        sleep(2)
        try:
            user_name = self.driver.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input')
        except NoSuchElementException:
            print("user_name element not found")
        else:
            user_name.send_keys(user_ID, Keys.TAB)

        sleep(2)
        try:
            user_pwd = self.driver.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input')
        except NoSuchElementException:
            print("password element not found")
        else:
            user_pwd.send_keys(pwd, Keys.ENTER)

        sleep(5)
        try:
            notification_off = self.driver.find_elements('css selector', 'button')
        except NoSuchElementException:
            print("notification element not found")
        else:
            not_off = [item for item in notification_off if item.text == "Not Now"]
            not_off[0].click()

    def find_followers(self):
        sleep(2)
        self.driver.get(url="https://www.instagram.com/shittywinememes/")

        sleep(10)
        try:
            followers_botton = self.driver.find_element('partial link text', "followers")
        except NoSuchElementException:
            print("followers element not found")
        else:
            followers_botton.click()
        # find all li elements in list
        sleep(10)
        try:
            fBody = self.driver.find_element('css selector', 'div ._aano div div')
            #fBody = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_NN"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div')
        except NoSuchElementException:
            print("scroll element not found")
        else:
            # fBody.send_keys(Keys.END)
            scroll = 0
            while scroll < 5:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", fBody)
                sleep(2)
                scroll += 1

            # scroll = 0
            # while scroll < 5:  # scroll 5 times
            #     self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
            #                                fBody)
            #     sleep(3)
            #     scroll += 1
            #
            # fList = self.driver.find_elements('xpath', '//*[@id="mount_0_0_NN"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]')
            # print("fList len is {}".format(len(fList)))
        #
        # print("ended")

    def follow(self):
        pass
