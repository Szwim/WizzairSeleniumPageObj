import unittest
from PageObejcts.registrationPage import RegistratonPage
from PageObejcts.HomePage import HomePage
from PageObejcts.loginPage import LoginPage
from faker import Faker
from base_test import BaseTest


#DANE TESTOWE
invalid_phone_number = "askldmaj"
invalid_mail = "kmsaliod.gmail.com"
invalid_name = "23234"
invalid_surname = "232321"
invalid_password = "sdKam232(("


class WizzairRegistration(BaseTest):

    @unittest.SkipTest
    def test_001_correct_registration(self):
        driver = self.driver
        fake = Faker()

        hp = HomePage(driver)
        hp.click_login()

        lp = LoginPage(driver)
        lp.click_register()

        rp = RegistratonPage(driver)
        rp.enter_name(fake.first_name_male())
        rp.enter_surname(fake.last_name_male())
        rp.click_empty_box()
        rp.chose_gender()
        rp.click_country_code()
        rp.input_country_code(fake.country_code())
        rp.fill_phone_number(fake.phone_number())
        rp.fill_mail_adress(fake.safe_email())
        rp.enter_password(fake.pystr(9,10)+str(fake.pyint()))
        rp.fill_country("Norwegia")
        rp.check_box()
        rp.wait_until()
        rp.register_account_button()
        rp.wait2_until()
        print("Utworzenie konto przebiegło pomyślnie")
        print("Zakończono test_001")

    @unittest.SkipTest
    def test_002_invalid_phone_number(self):
        driver = self.driver
        fake = Faker()

        hp = HomePage(driver)
        hp.click_login()

        lp = LoginPage(driver)
        lp.click_register()

        rp = RegistratonPage(driver)
        rp.enter_name(fake.first_name_male())
        rp.enter_surname(fake.last_name_male())
        rp.click_empty_box()
        rp.chose_gender()
        rp.click_country_code()
        rp.input_country_code(fake.country_code())
        rp.fill_phone_number(invalid_phone_number)
        rp.fill_mail_adress(fake.safe_email())
        rp.enter_password(fake.pystr(9,10)+str(fake.pyint()))
        rp.fill_country("Norwegia")
        rp.check_box()
        rp.wait_until()
        rp.register_account_button()
        rp.wait2_until()
        error_msg = rp.error_msg()
        expected_error_msg = "Wpisz prawidłowy numer telefonu komórkowego."
        self.assertEqual(expected_error_msg,error_msg,"Tytuły nie są takie same")
        print("Podano niepoprawny numer telefonu.")
        print("Zakończono test_002")

    @unittest.SkipTest
    def test003_invalid_mail_adress(self):
        driver = self.driver
        fake = Faker()

        hp = HomePage(driver)
        hp.click_login()

        lp = LoginPage(driver)
        lp.click_register()

        rp = RegistratonPage(driver)
        rp.enter_name(fake.first_name_male())
        rp.enter_surname(fake.last_name_male())
        rp.click_empty_box()
        rp.chose_gender()
        rp.click_country_code()
        rp.input_country_code(fake.country_code())
        rp.fill_phone_number(fake.phone_number())
        rp.fill_mail_adress(invalid_mail)
        rp.enter_password(fake.pystr(9, 10) + str(fake.pyint()))
        rp.fill_country("Norwegia")
        rp.check_box()
        rp.register_account_button()
        rp.wait2_until()
        error_msg = rp.error_msg2()
        expected_error_msg = "Nieprawidłowy adres e-mail"
        self.assertEqual(expected_error_msg,error_msg,"Tytuły nie są takie same")
        print("Podano niepoprawny adres e-mailowy")
        print("Zakończono test_003")

    @unittest.SkipTest
    #Poniższy test działa zarówno na pole "Name" jak i "Surname"
    def test004_invalid_name(self):
        driver = self.driver
        fake = Faker()

        hp = HomePage(driver)
        hp.click_login()

        lp = LoginPage(driver)
        lp.click_register()

        rp = RegistratonPage(driver)
        rp.enter_name(invalid_name)
        rp.enter_surname(fake.last_name_male())
        rp.click_empty_box()
        rp.chose_gender()
        rp.click_country_code()
        rp.input_country_code(fake.country_code())
        rp.fill_phone_number(fake.phone_number())
        rp.fill_mail_adress(fake.safe_email())
        rp.enter_password(fake.pystr(9, 10) + str(fake.pyint()))
        rp.fill_country("Norwegia")
        rp.check_box()
        rp.wait_until()
        rp.register_account_button()
        rp.wait2_until()
        error_msg = rp.error_msg3()
        expected_error_msg = "Nieprawidłowy znak"
        self.assertEqual(expected_error_msg,error_msg,"Tytuły różnią się od siebie")
        print("Pole 'Imię' oraz/bądź 'Nazwisko' zawiera niedozwolone znaki.")
        print("Zakończono test_004")

    @unittest.SkipTest
    def test005_invalid_password(self):
        driver = self.driver
        fake = Faker()

        hp = HomePage(driver)
        hp.click_login()

        lp = LoginPage(driver)
        lp.click_register()

        rp = RegistratonPage(driver)
        rp.enter_name(fake.first_name_male())
        rp.enter_surname(fake.last_name_male())
        rp.click_empty_box()
        rp.chose_gender()
        rp.click_country_code()
        rp.input_country_code(fake.country_code())
        rp.fill_phone_number(fake.phone_number())
        rp.fill_mail_adress(fake.safe_email())
        rp.enter_password(invalid_password)
        rp.fill_country("Norwegia")
        rp.check_box()
        rp.wait_until()
        rp.register_account_button()
        rp.wait2_until()
        error_msg = rp.error_msgs_for_invalid_password()
        expected_error = "min. 7, maks. 16 znaków, należy użyć zarówno liter, jak i cyfr, dozwolone są małe i wielkie litery, cyfry, oraz znaki specjalne."
        self.assertEqual(expected_error,error_msg,"Tytuły różnią się od siebie")
        print("Pole 'Hasło' zostało wypełnione błędnie.")
        print("Zakończono test_005")


if __name__ == "__main__":
    unittest.main(verbosity=2)