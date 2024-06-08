from datetime import datetime
import faker
from random import randint, choice
import sqlite3
from connection import database

GOALS = [('lose weights',), ('gain weights',), ('growth muscles',)]
ACTIONS = [{'running': 8}, {'training': 9}, {'swimming': 7}, {'shopping': 1.3}, {'football': 7.5}, {'dancing': 6.5},
           {'walking': 4}]
LEVELS = {'low': {'male': 2000, 'female': 1600}, 'medium': {'male': 2200, 'female': 1800},
          'high': {'male': 2400, 'female': 2000}}


# def generate_fake_data(number_companies, number_employees, number_post) -> tuple():
#     fake_companies = []  # тут зберігатимемо компанії
#     fake_employees = []  # тут зберігатимемо співробітників
#     fake_posts = []  # тут зберігатимемо посади
#     '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
#     fake_data = faker.Faker()
#
#     # Створимо набір компаній у кількості number_companies
#     for _ in range(number_companies):
#         fake_companies.append(fake_data.company())
#
#     # Згенеруємо тепер number_employees кількість співробітників'''
#     for _ in range(number_employees):
#         fake_employees.append(fake_data.name())
#
#     # Та number_post набір посад
#     for _ in range(number_post):
#         fake_posts.append(fake_data.job())
#
#     return fake_companies, fake_employees, fake_posts
#
#
# def prepare_data(companies, employees, posts) -> tuple():
#     for_companies = []
#     # готуємо список кортежів назв компаній
#     for company in companies:
#         for_companies.append((company, ))
#
#     for_employees = []  # для таблиці employees
#
#     for emp in employees:
#         '''
#         Для записів у таблицю співробітників нам потрібно додати посаду та id компанії. Компаній у нас було за замовчуванням
#         NUMBER_COMPANIES, при створенні таблиці companies для поля id ми вказували INTEGER AUTOINCREMENT - тому кожен
#         запис отримуватиме послідовне число збільшене на 1, починаючи з 1. Тому компанію вибираємо випадково
#         у цьому діапазоні
#         '''
#         for_employees.append((emp, choice(posts), randint(1, NUMBER_COMPANIES)))
#
#     '''
#    Подібні операції виконаємо й у таблиці payments виплати зарплат. Приймемо, що виплата зарплати у всіх компаніях
#     виконувалася з 10 по 20 числа кожного місяця. Діапазон зарплат генеруватимемо від 1000 до 10000 у.о.
#     для кожного місяця, та кожного співробітника.
#     '''
#     for_payments = []
#
#     for month in range(1, 12 + 1):
#         # Виконуємо цикл за місяцями'''
#         payment_date = datetime(2021, month, randint(10, 20)).date()
#         for emp in range(1, NUMBER_EMPLOYESS + 1):
#             # Виконуємо цикл за кількістю співробітників
#             for_payments.append((emp, payment_date, randint(1000, 10000)))
#
#     return for_companies, for_employees, for_payments


def insert_data_to_db() -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect(database) as con:

        cur = con.cursor()

        sql_to_goals = """INSERT INTO goal_weight(name)
                               VALUES (?)"""

        cur.executemany(sql_to_goals, GOALS)

        sql_to_levels = """INSERT INTO activity_level(name, wasted_calories, gender)
                               VALUES (?, ?, ?)"""

        activities = []

        for name, wasted_calories in LEVELS.items():
            for gender, calories in wasted_calories.items():
                activities.append((name, calories, gender))

        cur.executemany(sql_to_levels, activities)

        sql_to_activity_actions = """INSERT INTO activity_actions(name, wasted_calories)
                              VALUES (?, ?)"""

        actions = []
        for action in ACTIONS:
            for name, wasted_calories in action.items():
                actions.append((name, wasted_calories))

        cur.executemany(sql_to_activity_actions, actions)

        con.commit()


if __name__ == "__main__":
    insert_data_to_db()
