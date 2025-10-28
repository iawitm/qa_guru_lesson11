from dataclasses import dataclass
from datetime import date
from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3


class Hobby(Enum):
    SPORTS = 1
    READING = 2
    MUSIC = 3


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    date_of_birth: date
    subjects: str
    hobbies: Hobby
    picture: str
    current_address: str
    state: str
    city: str


student = User("Frog",
               "Green",
               "greenfrog@frog.com",
               Gender.OTHER,
               "1234567890",
               date(2024, 4, 24),
               "Arts",
               Hobby.MUSIC,
               "cute_frog.jpg",
               "North Forest, Great Swamp, Reed #1",
               "Haryana",
               "Karnal")