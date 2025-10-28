def convert_name(first_name, last_name):
    return first_name + " " + last_name


def convert_gender(gender):
    if gender.value == 1:
        return "Male"
    elif gender.value == 2:
        return "Female"
    else:
        return "Other"


def convert_date_of_birth(birth_date):
    year = str(birth_date.year)
    month = birth_date.strftime('%B')
    day = str(birth_date.day)
    return f'{day} {month},{year}'


def convert_hobby(hobby):
    if hobby.value == 1:
        return "Sports"
    elif hobby.value == 2:
        return "Reading"
    else:
        return "Music"


def convert_state_city(state, city):
    return state + " " + city