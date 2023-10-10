from api_work import Api_work
from api_work import Data_file
from db_work import DBManager

print('Давай проверим что получилось:))')
api_result = Api_work()

vacant = api_result.get_api_vacancies()
vac_dict = api_result.vacancy_data(vacant)
emp_dict = api_result.employer_data(vacant)
print('Я нашла вакансии с HH.ru')
Data_file.vacancy_file_create(vac_dict)
Data_file.employer_file_create(emp_dict)
db_result = DBManager()
db_result.filling_db_of_vacancies()
db_result = DBManager()
db_result.filling_db_of_employer()
print('И записала вакансии в таблицы базы данных "coursework_5"')
print('Попробуем сделать запросы к базе данных?')
while True:
    print('Выбери из списка:\n'
            "1 - Вывести список всех компаний и количество вакансий у каждой компании; \n"
            "2 - Вывести список всех вакансий; \n"
            "3 - Вывести среднюю зарплату по вакансиям; \n"
            "4 - Вывести список всех вакансий, у которых зарплата выше средней по всем вакансиям; \n"
            "5 - Вывести список всех вакансий в названии которых будем искать твой запрос; \n"
            "exit - для выхода. \n"
        )
    choose = input()

    if choose.lower() == "exit":
        break
    elif choose == '1':
        db_result = DBManager()
        data = db_result.get_companies_and_vacancies_count()
        print(data)

    elif choose == '2':
        db_result = DBManager()
        data = db_result.get_all_vacancies()
        print(data)
    elif choose == '3':
        db_result = DBManager()
        data = db_result.get_avg_salary()
        print(data)
    elif choose == '4':
        db_result = DBManager()
        data = db_result.get_vacancies_with_higher_salary()
        print(data)
    elif choose == '5':
        print('Ведите ключевое слово для запроса')
        keyword = input()
        db_result = DBManager()
        data = db_result.get_vacancies_with_keyword(keyword)
        print(data)