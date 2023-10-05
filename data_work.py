"""Скрипт для заполнения данными таблиц в БД Postgres."""
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
            with open('vacancy.json', 'r') as file:
                vacancy_data = json.load(file)
                query = 'insert into vacancy values (%s, %s, %s, %s, %s)'
                for data in vacancy_data:
                    data_line = data['id_vacancy'], data['vacancy_name'], data['salalry'], data['link'], data['id_company']
                    cur.execute(query, (tuple(data_line)))

            with open('vacancy.json', 'r') as file:
                employer_data = json.load(file)
                print (employer_data)
                test_emplouer = list(set(employer_data))
                query = 'insert into employer values (%s, %s)'
                for data in test_emplouer:
                    data_line = data['id_company'], data['company_name']
                    cur.execute(query, (tuple(data_line)))
finally:
    conn.close()

 # def del_vacancy(self):
    with open('vacancy.json', "w", encoding='utf-8') as outfile:
        content = []
        json.dump(content, outfile)
