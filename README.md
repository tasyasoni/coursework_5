# coursework_5

Поиск вакансий с платформы HeadHunter по 10 крупным работодателям

Описание

Отчет реализован на языке Python, он выводит на экран список из вакансий с платформы HeadHunter по 10 крупным работодателям

Реализован функционал вывода количества вакансий по каждому работодателю,
10 вакансий с максимальной заработной плате, вывода средней зарплаты по вакансиям и вывода вакасний по ключевому слову. 

Вдохновением для данного проекта служит курс разработчика Python на платформе SkyPro, с которым подробно вы можете ознакомиться https://sky.pro/courses/programming/python-web-course.

О проекте. • Информация с результатами поиска выводится на экран пользователя. • Информациия также записывается в файл json. • Код написан на языке программирования Python

Запуск проекта Install main.py

Сфера применения • Поисковики данных с разлиных платформ

Поддержите мои начинания • Позитивные отзывы и положительная обратная связь – приветствуется 😘

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