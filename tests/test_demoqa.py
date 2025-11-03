import allure

from data import users
from pages.registration_page import RegistrationPage


@allure.title("Successful fill form")
def test_demo_qa_form(browser_setup):
    registration_page = RegistrationPage()
    student = users.student
    with allure.step("Open registrations form"):
        registration_page.open()
    with allure.step("Fill form"):
        registration_page.register(student)
    with allure.step("Check form results"):
        registration_page.should_have_registered_user(student)
