from data import users
from pages.registration_page import RegistrationPage


def test_demo_qa_form(browser_setup):
    registration_page = RegistrationPage()
    student = users.student

    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered_user(student)