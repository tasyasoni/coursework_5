# coursework_5

Создайте класс 
DBManager
, который будет подключаться к БД PostgreSQL и иметь следующие методы:

**— получает список всех компаний и количество вакансий у каждой компании.**

get_companies_and_vacancies_count()
cur.execute(select id_company, count vacancy_name, employer.copmany_name from vacansy using (epmloyer_id) )
list_company = cur.fetchall()
откртыть. закрыть кусор

  **— получает список всех вакансий с указанием названия компании, названия вакансии
и зарплаты и ссылки на вакансию.**
get_all_vacancies()
cur.execute(select employer.copmany_name, vacancy_name, salary, link_vac from vacansy using (epmloyer_id))

 **— получает среднюю зарплату по вакансиям.**
get_avg_salary()
cur.execute(select avg (salary) from vacansy)

**— получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.**
get_vacancies_with_higher_salary()
cur.execute(select vacancy_name, salary from vacansy order by salary limit 10)
 
 **— получает список всех вакансий, в названии которых содержатся переданные в метод слова,
например python.**
get_vacancies_with_keyword()
cur.execute(select vacancy_name from vacansy where in ('ключевое слово'))

Класс 
DBManager
 должен использовать библиотеку 
psycopg2
 для работы с БД.