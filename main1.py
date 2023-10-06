import json
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="coursework_5",
    user="postgres",
    password="Antoniya2308"
)
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute('select employer.company_name, count (*) from vacancy inner join employer using (id_company) group by employer.company_name')
            list_company = cur.fetchall()
            for data in list_company:
                for i in data:
                    print(i, ' ', end="")
                print('\n')

            cur.execute('select employer.company_name, vacancy_name, salary, link_hh from vacancy inner join employer using (id_company)')
            list_company = cur.fetchall()
            for data in list_company:
                for i in data:
                    print(i, ' ', end="")
                print('\n')

            cur.execute('select round (avg (salary)) from vacancy')
            list_company = cur.fetchall()
            for data in list_company:
                print(data)
            print(f"Средняя зарплата в вакансиях по запросу {list_company}")

            cur.execute('select vacancy_name, salary from vacancy where salary > (select avg (salary) from vacancy) order by salary desc limit 10')
            list_company = cur.fetchall()
            for data in list_company:
                print(data)

            cur.execute("select * from vacancy where vacancy_name like ('%Менеджер%')")
            list_company = cur.fetchall()
            for data in list_company:
                print(data)

finally:
    conn.close()
