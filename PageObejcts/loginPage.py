from Locators.locators import Locators
from PageObejcts.BasePage import BasePage


class LoginPage(BasePage):

    def click_register(self):
        self.driver.find_element_by_xpath(Locators.register_textbox_xpath).click()