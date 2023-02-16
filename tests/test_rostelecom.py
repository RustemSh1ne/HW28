
from page.registration_form_page import RegistrationFormPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page.rostelecom_authorization_page import RostelecomAuthorizationPage
from page.email_confirmation_page import SubmitEmail
from test import functions
from page.policy_privacy_page import PolicyPrivacy
from fixtures.fixtures import open_rostelecom_page


# TC-01
def test_auth_valid_mail_valid_pass(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    email_tab = functions.find(driver, RostelecomAuthorizationPage.EMAIL_TAB)
    email_tab.click()

    # шаг 2
    email_input = functions.find(driver, RostelecomAuthorizationPage.EMAIL)
    email_input.send_keys('rustemshtest@mail.ru')

    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('ZxAsQw!2')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    assert "https://b2c.passport.rt.ru/account_b2c/page?state=" in driver.current_url


# TC-02
def test_auth_valid_email_invalid_pass(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    email_tab = functions.find(driver, RostelecomAuthorizationPage.EMAIL_TAB)
    email_tab.click()

    # шаг 2
    email = functions.find(driver, RostelecomAuthorizationPage.EMAIL)
    email.send_keys('rustemshtest@mail.ru')

    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('ZxAsQw!@')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert error_message.text == "Неверный логин или пароль"


# TC-03
def test_auth_invalid_email_valid_pass(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    email_tab = functions.find(driver, RostelecomAuthorizationPage.EMAIL_TAB)
    email_tab.click()

    # шаг 2
    email = functions.find(driver, RostelecomAuthorizationPage.EMAIL)
    email.send_keys('rustemshtes1@mail.ru')

    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('ZxAsQw!2')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert error_message.text == "Неверный логин или пароль"


# TC-04
def test_auth_valid_phone_valid_pass(open_rostelecom_page):
    driver = open_rostelecom_page
    # шаг 1
    telephone_tab = functions.find(driver, RostelecomAuthorizationPage.TELEPHONE_NUMBER_TAB)
    telephone_tab.click()

    # шаг 2
    telephone_number = functions.find(driver, RostelecomAuthorizationPage.TELEPHONE_NUMBER)
    telephone_number.send_keys('+79177856410')

    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('ZxAsQw!2')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    assert "https://b2c.passport.rt.ru/account_b2c/page?state=" in driver.current_url


# TC-05
def test_auth_invalid_phone_valid_pass(open_rostelecom_page):
    driver = open_rostelecom_page
    # шаг 1
    telephone_tab = functions.find(driver, RostelecomAuthorizationPage.TELEPHONE_NUMBER_TAB)
    telephone_tab.click()

    # шаг 2
    telephone_number = functions.find(driver, RostelecomAuthorizationPage.TELEPHONE_NUMBER)
    telephone_number.send_keys('+79177856411')

    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('ZxAsQw!2')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert error_message.text == "Неверный логин или пароль"


# TC-06
def test_auth_valid_phone_invalid_pass(open_rostelecom_page):
    driver = open_rostelecom_page
    # шаг 1
    telephone_tab = functions.find(driver, RostelecomAuthorizationPage.TELEPHONE_NUMBER_TAB)
    telephone_tab.click()

    # шаг 2
    telephone_number = functions.find(driver, RostelecomAuthorizationPage.TELEPHONE_NUMBER)
    telephone_number.send_keys('+79177856410')

    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('ZxAsQw!@')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert error_message.text == "Неверный логин или пароль"


# TC-07
def test_auth_valid_login_valid_pass(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    login_tab = functions.find(driver, RostelecomAuthorizationPage.LOGIN_TAB)
    login_tab.click()

    # шаг 2
    login_input = functions.find(driver, RostelecomAuthorizationPage.LOGIN_)
    login_input.send_keys('rtkid_1676559807109')

    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('ZxAsQw!2')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    assert "https://b2c.passport.rt.ru/account_b2c/page?state=" in driver.current_url


# TC-08
def test_auth_valid_login_invalid_pass(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    login_tab = functions.find(driver, RostelecomAuthorizationPage.LOGIN_TAB)
    login_tab.click()

    # шаг 2
    login_input = functions.find(driver, RostelecomAuthorizationPage.LOGIN_)
    login_input.send_keys('rtkid_1676559807109')


    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('ZxAsQw!@')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert error_message.text == "Неверный логин или пароль"


# TC-09
def test_auth_invalid_login_valid_pass(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    login_tab = functions.find(driver, RostelecomAuthorizationPage.LOGIN_TAB)
    login_tab.click()

    # шаг 2
    login_input = functions.find(driver, RostelecomAuthorizationPage.LOGIN_)
    login_input.send_keys('rtkid_1676559807100')


    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('ZxAsQw!2')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert error_message.text == "Неверный логин или пароль"


# TC-10
def test_registration_name_2_characters(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    # шаг 2
    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Ру")

    # шаг 3
    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Шайдуллин')

    # шаг 4
    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Москва г")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    # шаг 5
    email = functions.get_random_string(8) + '@gmail.com'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    # шаг 6
    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    # шаг 7
    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    # шаг 8
    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# TC-11
def test_registration_name_1_character(open_rostelecom_page):
    driver = open_rostelecom_page
    # шаг 1
    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    # шаг 2
    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Р")

    # шаг 3
    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Шайдуллин')

    # шаг 4
    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Москва г")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    # шаг 5
    email = functions.get_random_string(8) + '@gmail.com'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    # шаг 6
    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    # шаг 7
    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    # шаг 8
    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_error_message = functions.find(driver, RegistrationFormPage.NAME_ERROR_MESSAGE)
    assert check_error_message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# TC-12
def test_registration_password_8_characters(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    # шаг 2
    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Рустэм")

    # шаг 3
    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Шайдуллин')

    # шаг 4
    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Москва г")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    # шаг 5
    email = functions.get_random_string(8) + '@gmail.com'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    # шаг 6
    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    # шаг 7
    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    # шаг 8
    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# TC-13
def test_registration_password_4_characters(open_rostelecom_page):
    driver = open_rostelecom_page
    # шаг 1
    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    # шаг 2
    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Рустэм")

    # шаг 3
    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Шайдуллин')

    # шаг 4
    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Москва г")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    # шаг 5
    email = functions.get_random_string(8) + '@gmail.com'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    # шаг 6
    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(4)
    password.send_keys(password_generation)

    # шаг 7
    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)
    check_error_message = functions.find(driver, RegistrationFormPage.INVALID_ACCOUNT_NUMBER_ERROR_MESSAGE)
    assert check_error_message.text == "Длина пароля должна быть не менее 8 символов"


# TC-14
def test_registration_name_29_characterss(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    # шаг 2
    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Абвгдеёжзиабвгдеёжзиабвгдеёжз")

    # шаг 3
    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Абвгде')

    # шаг 4
    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Москва г")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    # шаг 5
    email = functions.get_random_string(8) + '@gmail.com'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)
    # шаг 6
    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(14)
    password.send_keys(password_generation)

    # шаг 7
    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    # шаг 8
    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_email_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_email_text.text == "Подтверждение email"


# TC-15
def test_redirect_policy_privacy(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    policy_privacy_link = functions.find(driver, RostelecomAuthorizationPage.POLICY_PRIVACY)
    policy_privacy_link.click()
    current_url = driver.switch_to.window(driver.window_handles[1])
    check_redirect_to_policy_privacy = functions.find(driver, PolicyPrivacy.POLICY_PRIVACY)
    assert driver.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"


