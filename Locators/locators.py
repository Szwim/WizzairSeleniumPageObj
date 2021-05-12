class Locators():
    # HomePage objects
    login_textbox_xpath = '//button[@class="navigation__button navigation__button--simple" and @data-test="navigation-menu-signin"]'

    # loginPage objects
    register_textbox_xpath = '//button[@data-test="registration"]'

    # registration page

    name_textbox_name = 'firstName'
    surname_textbox_name = 'lastName'
    empty_box_name = 'email'
    gender_textbox_xpath = '//label[@data-test="register-gendermale"]'
    country_code_textbox_xpath = '//div[@data-test="booking-register-country-code"]'
    country_code_input_list_xpath = '//input[@name="phone-number-country-code"]'
    phone_number_textbox_name = 'phoneNumberValidDigits'
    mail_textbox_name = 'email'
    password_textbox_xpath = '//input[@data-test="booking-register-password"]'
    chose_country_textbox_xpath = '//input[@data-test="booking-register-country"]'
    check_box_click_css_selector = "div#app>span>article>div>div>div>form>div:nth-of-type(11)>div>label"
    check_box2_click_css_selector = "div#app>span>article>div>div>div>form>div:nth-of-type(9)>div>label"
    check_box3_click_selector = "div#app>span>article>div>div>div>form>div:nth-of-type(10)>div>label"
    wait_xpath = "//span[text()='Nieprawidłowy adres e-mail']"
    registration_check_box_click_xpath = "//button[@data-test='booking-register-submit']"
    wait2_class_name = "heading heading--2 base-heading base-heading--2"
    error_msg_xpath = "//span[text()='Wpisz prawidłowy numer telefonu komórkowego.']"
    error_msg2_xpath = "//span[text()='Nieprawidłowy adres e-mail']"
    error_msg3_xpath = "//span[text()='Nieprawidłowy znak']"
    error_msg4_xpath = "(//p[text()=' min. 7, maks. 16 znaków, '])[2]"
    error_msg5_xpath = "(//p[text()=' należy użyć zarówno liter, jak i cyfr, '])[2]"
    error_msg6_xpath = "(//p[text()=' dozwolone są małe i wielkie litery, cyfry, oraz znaki specjalne. '])[2]"


