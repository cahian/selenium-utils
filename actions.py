from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class SafeActionChains:
    def __init__(self, driver, wait, pause=0.1):
        self.action_chains = ActionChains(driver)
        self.driver = driver
        self.wait = wait
        self.pause = pause

    def send_keys_to(self, mark, *keys_to_send):
        if not isinstance(mark, WebElement):
            mark = self.wait.until(EC.presence_of_element_located(mark))
            # self.wait.until(EC.element_to_be_clickable(mark))
        self.action_chains\
            .move_to_element(mark)\
            .pause(self.pause)\
            .send_keys_to_element(mark, *keys_to_send)\
            .pause(self.pause)
        return self

    def click(self, mark):
        if not isinstance(mark, WebElement):
            mark = self.wait.until(EC.presence_of_element_located(mark))
            # self.wait.until(EC.element_to_be_clickable(mark))
        self.action_chains\
            .move_to_element(mark)\
            .pause(self.pause)\
            .click(mark)\
            .pause(self.pause)
        return self

    def perform(self):
        self.action_chains.perform()


def safeclick(driver, wait, mark):
    SafeActionChains(driver, wait).click(mark).perform()
