from Locators.locators import Locators
from PageObejcts.BasePage import BasePage


class HomePage(BasePage):

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.login_textbox_xpath).click()