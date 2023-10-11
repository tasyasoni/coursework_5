import requests
import json


class Api_work:


    def get_api_vacancies(self, *request):
        """
        Получает вакансии по 10 выбранным работодателям
        """
        emp_list = ['1740', '740', '581458', '205', '116918', '3809', '2180', '3095', '4509', '947']
        params = {
            'employer_id': emp_list,
            'per_page': 100
        }
        req = requests.get('https://api.hh.ru/vacancies/', params=params)
        data = req.content.decode()
        vacant = json.loads(data)
        return vacant

    def vacancy_data(self, vacant):
        """
        Формирует данные по вакансиям в словрь
        """
        vac_dict = []
        for vacancy in vacant['items']:
            name = vacancy['name']
            if vacancy['salary'] is None:
                salary = 0
            else:
                salary = vacancy['salary']['from']
            url = vacancy['alternate_url']
            try:
                vacancy['employer']['id']
            except KeyError:
                continue
            else:
                employer_id = vacancy['employer']['id']
            id_vacancy = vacancy['id']
            dictionary_vac = {'id_company': employer_id,
                              'id_vacancy': id_vacancy,
                              'vacancy_name': name,
                              'salalry': salary,
                              'link':url
            }
            vac_dict.append(dictionary_vac)
        return vac_dict


    def employer_data(self, vacant):
        """
        Формирует данные по работодателям в словрь,
        пропускает дубли
        """
        emp_dict = []
        for vacancy in vacant['items']:
            employer = vacancy['employer']['name']
            try:
                vacancy['employer']['id']
            except KeyError:
                continue
            else:
                employer_id = vacancy['employer']['id']
                dictionary_emp = {'id_company': employer_id,
                                  'company_name': employer,
                }
            if dictionary_emp not in emp_dict:
                emp_dict.append(dictionary_emp)
            else:
                continue
        return emp_dict


class Data_file:


    @staticmethod
    def vacancy_file_create(vac_dict):
        """
        Записывает данные по вакансиям в файл
        """
        with open("vacancy.json", 'w',encoding="utf-8") as outfile:
            json.dump(vac_dict, outfile, ensure_ascii=False, indent=6 )


    @staticmethod
    def employer_file_create(emp_dict):
        """
        Записывает данные по работодателям в файл
        """
        with open("employer.json", 'w',encoding="utf-8") as outfile:
            json.dump(emp_dict, outfile, ensure_ascii=False, indent=6)


    @staticmethod
    def vacancy_file_clear():
        """
        Очищает файл
        """
        with open('vacancy.json', "w", encoding='utf-8') as outfile:
            content = []
            json.dump(content, outfile)


    @staticmethod
    def employer_file_clear():
        """
        Очищает файл
        """
        with open('employer.json', "w", encoding='utf-8') as outfile:
            content = []
            json.dump(content, outfile)