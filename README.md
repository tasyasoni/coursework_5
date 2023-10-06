# coursework_5

Создайте класс 
DBManager
, который будет подключаться к БД PostgreSQL и иметь следующие методы:

**— получает список всех компаний и количество вакансий у каждой компании.**

get_companies_and_vacancies_count()

cur.execute('select employer.company_name, count (*) from vacancy
inner join employer using (id_company)
group by employer.company_name') 

list_company = cur.fetchall()


  **— получает список всех вакансий с указанием названия компании, названия вакансии
и зарплаты и ссылки на вакансию.**
get_all_vacancies()
cur.execute(select employer.company_name, vacancy_name, salary, link_hh 
from vacancy 
inner join employer using (id_company))

 **— получает среднюю зарплату по вакансиям.**
get_avg_salary()
cur.execute(select round (avg (salary)) from vacancy)

**— получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.**
get_vacancies_with_higher_salary()

cur.execute(select vacancy_name, salary from vacancy 
where salary > (select avg (salary) from vacancy)
order by salary desc limit 10)
 
 **— получает список всех вакансий, в названии которых содержатся переданные в метод слова,
например python.**
get_vacancies_with_keyword()

cur.execute(select * from vacancy
where vacancy_name like ('%Менеджер%'))

Класс 
DBManager
 должен использовать библиотеку 
psycopg2
 для работы с БД.