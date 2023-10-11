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

    def __call__(self):
        pass


    def create_db_of_vacancies(self):
        """
        Создает таблицу с вакансиями
        """
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("create table vacancy (id_vacancy varchar(50) primary key, vacancy_name text, salary int, link_hh text, id_company varchar(50));")
        finally:
            self.conn.close()

    def create_db_of_epmloyers(self):
        """
        Создает таблицу с работодателями
        """
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("create table employer(id_company varchar(50) primary key, company_name text);")
        finally:
            self.conn.close()
    def filling_db_of_vacancies(self):
        """
        Заполняет таблицу с вакансиями
        данными из файла
        """
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
        """
        Заполняет таблицу с работодателями
        данными из файла
        """
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
        """
        Считает вакансии по компаниям
        """
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('select employer.company_name, count (*) from vacancy inner join employer using (id_company) group by employer.company_name')
                    list_company = cur.fetchall()
                    for data in list_company:
                        print(data)
        finally:
            self.conn.close()


    def get_all_vacancies(self):
        """
        Выводит все вакансии
        """
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('select employer.company_name, vacancy_name, salary, link_hh from vacancy inner join employer using (id_company)')
                    list_company = cur.fetchall()
                    for data in list_company:
                        print(data)
        finally:
            self.conn.close()


    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям
        """
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('select round (avg (salary)) from vacancy')
                    list_company = cur.fetchall()
                    for data in list_company:
                        for i in data:
                            print(f"Средняя зарплата в вакансиях по запросу {i}")
        finally:
            self.conn.close()

    def get_vacancies_with_higher_salary(self):
        """
        Выводит 10 вакансий с максимальной зарплатой
        """
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute('select vacancy_name, salary from vacancy where salary > (select avg (salary) from vacancy) order by salary desc limit 10')
                    list_company = cur.fetchall()
                    for data in list_company:
                        print(data)
        finally:
            self.conn.close()

    def get_vacancies_with_keyword(self, keyword):
        """
        Выводит вакансии по ключевому запросу
        """
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute(f"select * from vacancy where vacancy_name like ('%{keyword}%')")
                    list_company = cur.fetchall()
                    if len(list_company) == 0:
                        print("Нет вакансий по вашему запросу")
                    else:
                        for data in list_company:
                            print(data)
        finally:
              self.conn.close()

    def delete_db_of_vacancies(self):
        """
        Удаляет таблицу с вакансиями
        """
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("DROP TABLE vacancy")
        finally:
            self.conn.close()


    def delete_db_of_epmloyer(self):
        """
        Удаляет таблицу с компаниями
        """
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("DROP TABLE employer")
        finally:
              self.conn.close()
