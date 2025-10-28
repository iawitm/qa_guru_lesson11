import os
from selene import browser, command, have
from pages import helpers

from data.users import User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.mobile = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.subjects = browser.element('#subjectsInput')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.submit_button = browser.element('#submit')
        self.result_table = browser.element('.table-responsive').all('tr')

    def open(self):
        browser.open("/automation-practice-form")

    def register(self, user: User):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_email(user.email)
        self._choose_gender(user.gender)
        self._fill_mobile(user.mobile)
        self._fill_date_of_birth(user.date_of_birth)
        self._fill_subjects(user.subjects)
        self._choose_hobby(user.hobbies)
        self._upload_picture(user.picture)
        self._fill_current_address(user.current_address)
        self._select_state(user.state)
        self._select_city(user.city)
        self._submit_form()

    def should_have_registered_user(self, user: User):
        self.result_table.should(
            have.exact_texts(
                'Label Values',
                'Student Name ' + helpers.convert_name(user.first_name, user.last_name),
                'Student Email ' + user.email,
                'Gender ' + helpers.convert_gender(user.gender),
                'Mobile ' + user.mobile,
                'Date of Birth ' + helpers.convert_date_of_birth(user.date_of_birth),
                'Subjects ' + user.subjects,
                'Hobbies ' + helpers.convert_hobby(user.hobbies),
                'Picture ' + user.picture,
                'Address ' + user.current_address,
                'State and City ' + helpers.convert_state_city(user.state, user.city),
            )
        )

    def _fill_first_name(self, value):
        self.first_name.type(value)

    def _fill_last_name(self, value):
        self.last_name.type(value)

    def _fill_email(self, value):
        self.email.type(value)

    def _choose_gender(self, enum_value):
        browser.element(f'[for=gender-radio-{str(enum_value.value)}]').click()

    def _fill_mobile(self, value):
        self.mobile.type(value)

    def _fill_date_of_birth(self, value):
        year = str(value.year)
        month = str(value.month - 1)
        day = "0" + str(value.day)

        self.date_of_birth.click()
        browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').element(f'[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--{day}').click()

    def _fill_subjects(self, value):
        self.subjects.type(value).press_enter()

    def _choose_hobby(self, enum_value):
        browser.element(f'[for=hobbies-checkbox-{str(enum_value.value)}]').click()

    def _upload_picture(self, file):
        file_path = "tests/resources/" + file
        self.picture.send_keys(os.path.abspath(str(file_path)))

    def _fill_current_address(self, value):
        self.current_address.type(value)

    def _select_state(self, value):
        self.state.type(value).press_enter()

    def _select_city(self, value):
        self.city.type(value).press_enter()

    def _submit_form(self):
        self.submit_button.perform(command.js.scroll_into_view).click()