from selenium.webdriver.common.keys import Keys
from Locators.locators import Locators
from PageObejcts.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegistratonPage(BasePage):

    def enter_name(self, name):
        self.driver.find_element_by_name(Locators.name_textbox_name).clear()
        self.driver.find_element_by_name(Locators.name_textbox_name).send_keys(name)

    def enter_surname(self, surname):
        self.driver.find_element_by_name(Locators.surname_textbox_name).clear()
        self.driver.find_element_by_name(Locators.surname_textbox_name).send_keys(surname)

    def click_empty_box(self):
        self.driver.find_element_by_name(Locators.empty_box_name).click()

    def chose_gender(self):
        self.driver.find_element_by_xpath(Locators.gender_textbox_xpath).click()

    def click_country_code(self):
        self.driver.find_element_by_xpath(Locators.country_code_textbox_xpath).click()

    def input_country_code(self, country_code):
        self.driver.find_element_by_xpath(Locators.country_code_input_list_xpath).clear()
        self.driver.find_element_by_xpath(Locators.country_code_input_list_xpath).send_keys(country_code, Keys.ENTER)

    def fill_phone_number(self, phone_number):
        self.driver.find_element_by_name(Locators.phone_number_textbox_name).clear()
        self.driver.find_element_by_name(Locators.phone_number_textbox_name).send_keys(phone_number)

    def fill_mail_adress(self, email):
        self.driver.find_element_by_name(Locators.mail_textbox_name).clear()
        self.driver.find_element_by_name(Locators.mail_textbox_name).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(Locators.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(Locators.password_textbox_xpath).send_keys(password)

    def fill_country(self, country):
        self.driver.find_element_by_xpath(Locators.chose_country_textbox_xpath).clear()
        self.driver.find_element_by_xpath(Locators.chose_country_textbox_xpath).send_keys(country, Keys.ENTER)

    def check_box(self):
        self.driver.find_element_by_css_selector(Locators.check_box_click_css_selector).click()
        self.driver.find_element_by_css_selector(Locators.check_box2_click_css_selector).click()
        self.driver.find_element_by_css_selector(Locators.check_box3_click_selector).click()

    def register_account_button(self):
        self.driver.find_element_by_xpath(Locators.registration_check_box_click_xpath).click()

    def wait_until(self):
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.wait_xpath)))

    def wait2_until(self):
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, Locators.wait2_class_name)))

    def error_msg(self):
        error = self.driver.find_element_by_xpath(Locators.error_msg_xpath).text
        return error

    def error_msg2(self):
        error = self.driver.find_element_by_xpath(Locators.error_msg2_xpath).text
        return error

    def error_msg3(self):
        error = self.driver.find_element_by_xpath(Locators.error_msg3_xpath).text
        return error

    def error_msgs_for_invalid_password(self):
        error1 = self.driver.find_element_by_xpath(Locators.error_msg4_xpath).text
        error2 = self.driver.find_element_by_xpath(Locators.error_msg5_xpath).text
        error3 = self.driver.find_element_by_xpath(Locators.error_msg6_xpath).text
        error = error1 + " " + error2 + " " + error3
        return error
