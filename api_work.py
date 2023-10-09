import requests
import json


class Api_work:

    def get_api_vacancies(self, *request):
        params = {
            "text": request,
            'per_page': 100
        }
        req = requests.get('https://api.hh.ru/vacancies/', params=params)
        data = req.content.decode()
        vacant = json.loads(data)
        return vacant

    def vacancy_data(self, vacant):
        vac_dict = []
        for vacancy in vacant['items']:
            name = vacancy['name']
            if vacancy['salary'] is None:
                salary = 0
            else:
                salary = vacancy['salary']['from']
            url = vacancy['alternate_url']
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
        emp_dict = []
        for vacancy in vacant['items']:
            employer = vacancy['employer']['name']
            employer_id = vacancy['employer']['id']
            dictionary_emp = {'id_company': employer_id,
                              'company_name': employer,
            }
            if dictionary_emp not in emp_dict:
                print(dictionary_emp['id_company'])
                print(emp_dict)
                emp_dict.append(dictionary_emp)
            else:
                continue
        return emp_dict


class Data_file:

    def vacancy_file_create(self, vac_dict):
        with open("vacancy.json", 'w',encoding="utf-8") as outfile:
            json.dump(vac_dict, outfile, ensure_ascii=False, indent=6 )


    def employer_file_create(self,emp_dict ):
        with open("employer.json", 'w',encoding="utf-8") as outfile:
            json.dump(emp_dict, outfile, ensure_ascii=False, indent=6)


    def vacancy_file_clear (self):
        with open('vacancy.json', "w", encoding='utf-8') as outfile:
            content = []
            json.dump(content, outfile)

    def employer_file_clear(self):
        with open('employer.json', "w", encoding='utf-8') as outfile:
            content = []
            json.dump(content, outfile)