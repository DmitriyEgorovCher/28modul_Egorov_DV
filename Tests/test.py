# python -m pytest -v --driver Chrome --driver-path chromedriver.exe Tests/test.py
import pytest
from pages.Classes import AuthPage
from pages.Classes import RegPage

from pages.locators import AuthLocators
from pages.locators import RegLocators
from settings import *



def test_elements_of_auth(driver):
    """RT-001 Проверка Формы "Авторизация" на наличие основных элементов."""
    page = AuthPage(driver)

    assert page.tub_menu.text in page.card_of_auth.text
    assert page.mail.text in page.card_of_auth.text
    assert page.auth_pass.text in page.card_of_auth.text
    assert page.btn_enter.text in page.card_of_auth.text
    assert page.forgot_password_link.text in page.card_of_auth.text
    assert page.register_link.text in page.card_of_auth.text

def test_menu_type_auth(selenium):
    """RT-002 Проверка названий способов авторизации в меню выбора."""
    try:
        page = AuthPage(selenium)
        menu = [page.tub_phone.text, page.tub_email.text, page.tub_login.text, page.tub_ls.text]
        for i in range(len(menu)):
            assert "Номер" in menu
            assert 'Почта' in menu
            assert 'Логин' in menu
            assert 'Лицевой счёт' in menu
    except AssertionError:
        print('Ошибка в имени таба Меню типа аутентификации')

def test_auth_valid_email_pass(selenium):
    """RT-003 Тест авторизации с валидными значениями e-mail и паролем."""
    page = AuthPage(selenium)
    page.mail.send_keys(Settings.valid_email)
    page.mail.clear()
    page.auth_pass.send_keys(Settings.valid_password)
    page.auth_pass.clear()
    page.btn_enter.click()

    try:
        assert page.get_relative_link() == '/account_b2c/page'
    except AssertionError:
        assert 'Неверный логин или пароль' in page.find_other_element(*AuthLocators.ERROR_MESSAGE).text

@pytest.mark.parametrize("incor_email", [Settings.invalid_email, Settings.empty_email],
                         ids=['invalid_email', 'empty'])
@pytest.mark.parametrize("incor_pass", [Settings.invalid_password, Settings.empty_password],
                         ids=['invalid_password', 'empty'])

def test_auth_invalid_email_pass(selenium, incor_email, incor_pass):
    """RT-004, RT-005 "Проверка аутентификации пользователя с невалидным email и паролем:
    связка Почта+Пароль корректны, но пользователь с такими данными не зарегистрирован в системе;
    пустые значения."""
    page = AuthPage(selenium)
    page.mail.send_keys(incor_email)
    page.mail.clear()
    page.auth_pass.send_keys(incor_pass)
    page.auth_pass.clear()
    page.btn_enter.click()

    assert page.get_relative_link() != '/account_b2c/page'

def test_click_vk(driver):
    """RT-006 "Кнопка "VK" кликабельна и открывает форму для регистрации через аккаунт VK."""
    page = AuthPage(driver)

    page.btn_vk.click()
    window_title = page.get_main_link()
    assert window_title == Settings.url_id_vk

def test_click_ok(driver):
    """RT-007 "Кнопка "OK" кликабельна и открывает форму для регистрации через аккаунт OK."""
    page = AuthPage(driver)

    page.btn_ok.click()
    window_title = page.get_main_link()
    assert window_title == Settings.url_id_ok

def test_click_mail(driver):
    """RT-008 "Кнопка "@" кликабельна и открывает форму для регистрации через аккаунт Mail."""
    page = AuthPage(driver)

    page.btn_ma.click()
    window_title = page.get_main_link()
    assert window_title == Settings.url_id_ma

def test_click_ya(driver):
    """RT-009 "Кнопка "Я" кликабельна и открывает форму для регистрации через аккаунт Yandex"""
    page = AuthPage(driver)

    page.btn_ya.click()
    window_title = page.get_main_link()
    assert window_title == Settings.url_id_ya

def test_forgot_password_link(selenium):
    """RT-010 Тест перехода к форме "восстановление пароля."""
    page = AuthPage(selenium)
    page.driver.execute_script("arguments[0].click();", page.forgot_password_link)

    assert page.find_other_element(*AuthLocators.PASS_RECOVERY).text == 'Восстановление пароля'

def test_registration_link(selenium):
    """RT-011 Тест перехода к форме "Регистрация"."""
    page = AuthPage(selenium)
    page.register_link.click()

    assert page.get_relative_link() == Settings.url_reg

def test_elements_registration(selenium):
    """RT-012 Проверка Формы "Регистрация" на наличие основных элементов."""
    try:
        page = RegPage(selenium)
        card_of_reg = [page.first_name, page.last_name, page.adr_reg,
                       page.mail_reg, page.pass_reg,
                       page.pass_reg_confirm, page.btn_reg, page.user_agreement]

        for i in range(len(card_of_reg)):
            assert page.first_name in card_of_reg
            assert page.last_name in card_of_reg
            assert page.mail_reg in card_of_reg
            assert page.adr_reg in card_of_reg
            assert page.pass_reg in card_of_reg
            assert page.pass_reg_confirm in card_of_reg
            assert page.btn_reg.text in card_of_reg
            assert page.user_agreement in card_of_reg
    except AssertionError:
        print('В форме «Регистрация» отсутствует обязательный элемент')

def test_name_elements_registration(selenium):
    """RT-013 Проверка Формы "Регистрация" на соответствие названий элементов требованиям."""
    try:
        page = RegPage(selenium)
        assert 'Имя' in page.card_of_reg.text
        assert 'Фамилия' in page.card_of_reg.text
        assert 'Регион' in page.card_of_reg.text
        assert 'E-mail или мобильный телефон' in page.card_of_reg.text
        assert 'Пароль' in page.card_of_reg.text
        assert 'Подтверждение пароля' in page.card_of_reg.text
        assert 'Продолжить' in page.card_of_reg.text
    except AssertionError:
        print('Название элемента в форме «Регистрация» не соответствует Требованиям')

def test_reg_new_user(selenium):
    """RT-014 Регистрация нового пользователя с валидными данными."""

    page = RegPage(selenium)
    page.first_name.send_keys(Settings.first_name)
    page.first_name.clear()
    page.last_name.send_keys(Settings.last_name)
    page.last_name.clear()
    page.mail_reg.send_keys(Settings.valid_reg_mail)
    page.mail_reg.clear()
    page.pass_reg.send_keys(Settings.valid_reg_pass)
    page.pass_reg.clear()
    page.pass_reg_confirm.send_keys(Settings.valid_reg_pass)
    page.pass_reg_confirm.clear()
    page.btn_reg.click()

    assert page.find_other_element(*RegLocators.MAIL_CONFIRM).text == 'Подтверждение email'


@pytest.mark.parametrize("valid_first_name",
                         [
                             (Settings.russian_string) * 2
                             , (Settings.russian_string) * 3
                             , (Settings.russian_string) * 30
                         ],
                         ids=
                         [
                             'russ_symbols=2', 'russ_symbols=3', 'russ_symbols=30'
                         ])
def test_first_name_valid_data(selenium, valid_first_name):
    """RT-015 Тест поля ввода "Имя" формы "Регистрация" допустимыми валидными значениями:
    буквы кириллицы в количестве 2 ; 3; 30 ."""
    page = RegPage(selenium)
    page.first_name.send_keys(valid_first_name)
    page.first_name.clear()
    page.btn_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' \
           not in page.find_other_element(*RegLocators.CONTAINER_FIRST_NAME).text

@pytest.mark.parametrize("invalid_first_name",
                         [
                             (Settings.russian_string) * 1
                             , (Settings.russian_string) * 31
                             , (Settings.empty)
                             , (Settings.numbers)
                             , (Settings.latin_string)
                             , (Settings.chinese_chars)
                             , (Settings.special_chars)
                         ],
                         ids=
                         [
                             'russ_symbols=1', 'russ_symbols=31','empty'
                             , 'numbers', 'latin_symbols', 'chinese_symbols', 'special_symbols'
                         ])

def test_first_name_invalid_data(selenium, invalid_first_name):
    """RT-016 Тест поля ввода "Имя" формы "Регистрация" невалидными значениями:
    пустое значение;
    кириллица в количестве 1 ; 31 ; латиница; китайские иероглифы; спецсимволы; числа."""
    page = RegPage(selenium)
    page.first_name.send_keys(invalid_first_name)
    page.first_name.clear()
    page.btn_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'\
           in page.find_other_element(*RegLocators.MASSAGE_FIRST_NAME).text


@pytest.mark.parametrize("valid_last_name",
                         [
                             (Settings.russian_string) * 2
                             , (Settings.russian_string) * 3
                             , (Settings.russian_string) * 30
                         ],
                         ids=
                         [
                             'russ_symbols=2', 'russ_symbols=3', 'russ_symbols=30'
                         ])
def test_last_name_valid_data(selenium, valid_last_name):
    """RT-017 Тест поля ввода "Фамилия" формы "Регистрация" допустимыми валидными значениями:
    буквы кириллицы в количестве 2 ; 3; 30 ."""
    page = RegPage(selenium)
    page.last_name.send_keys(valid_last_name)
    page.last_name.clear()
    page.btn_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' \
           not in page.find_other_element(*RegLocators.CONTAINER_LAST_NAME).text

@pytest.mark.parametrize("invalid_last_name",
                         [
                             (Settings.russian_string) * 1
                             , (Settings.russian_string) * 31
                             , (Settings.empty)
                             , (Settings.numbers)
                             , (Settings.latin_string)
                             , (Settings.chinese_chars)
                             , (Settings.special_chars)
                         ],
                         ids=
                         [
                             'russ_symbols=1', 'russ_symbols=31','empty'
                             , 'numbers', 'latin_symbols', 'chinese_symbols', 'special_symbols'
                         ])

def test_last_name_invalid_data(selenium, invalid_last_name):
    """RT-018 Тест поля ввода "Фамилия" формы "Регистрация" невалидными значениями:
    пустое значение;
    кириллица в количестве 1 ; 31 ; латиница; китайские иероглифы; спецсимволы; числа."""
    page = RegPage(selenium)
    page.last_name.send_keys(invalid_last_name)
    page.last_name.clear()
    page.btn_reg.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'\
           in page.find_other_element(*RegLocators.MASSAGE_LAST_NAME).text