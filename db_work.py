import json
import psycopg2


class DBManager:

    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="coursework_5",
            user="postgres",
            password="Antoniya2308"
        )

    def filling_db_of_vacancies(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    with open('vacancy.json', 'r', encoding="utf-8") as file:
                        vacancy_data = json.load(file)
                        query = 'insert into vacancy values (%s, %s, %s, %s, %s)'
                        for data in vacancy_data:
                            data_line = data['id_vacancy'], data['vacancy_name'], data['salalry'], data['link'], data['id_company']
                            cur.execute(query, (tuple(data_line)))
        finally:
            self.conn.close()

    def filling_db_of_employer(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    with open('employer.json', 'r', encoding="utf-8") as file:
                        employer_data = json.load(file)
                        query = 'insert into employer values (%s, %s)'
                        for data in employer_data:
                            data_line = data['id_company'], data['company_name']
                            cur.execute(query, (tuple(data_line)))

        finally:
            self.conn.close()
    def get_companies_and_vacancies_count(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('select employer.company_name, count (*) from vacancy inner join employer using (id_company) group by employer.company_name')
                    list_company = cur.fetchall()
                    for data in list_company:
                        for i in data:
                            print(i, ' ', end="")
                        print('\n')
        finally:
            self.conn.close()

    def get_all_vacancies(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('select employer.company_name, vacancy_name, salary, link_hh from vacancy inner join employer using (id_company)')
                    list_company = cur.fetchall()
                    for data in list_company:
                        for i in data:
                            print(i, ' ', end="")
                        print('\n')
        finally:
            self.conn.close()


    def get_avg_salary(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('select round (avg (salary)) from vacancy')
                    list_company = cur.fetchall()
                    for data in list_company:
                        print(data)
                    print(f"Средняя зарплата в вакансиях по запросу {list_company}")
        finally:
            self.conn.close()

    def get_vacancies_with_higher_salary(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('select vacancy_name, salary from vacancy where salary > (select avg (salary) from vacancy) order by salary desc limit 10')
                    list_company = cur.fetchall()
                    for data in list_company:
                        print(data)
        finally:
            self.conn.close()

    def get_vacancies_with_keyword(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("select * from vacancy where vacancy_name like ('%Менеджер%')")
                    list_company = cur.fetchall()
                    for data in list_company:
                        print(data)
        finally:
              self.conn.close()
