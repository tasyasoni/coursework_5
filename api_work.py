from abc import ABC, abstractmethod
import requests
import json


class Api_work(ABC):  #абстрактный метод для API
    @abstractmethod
    def get_vacancies(self):
        pass


class Hh_class(Api_work): #класс для получения вакансий с HeadHunter по API

    def get_vacancies(self, *answer):
        params = {
            "text": answer,
            'per_page': 100
        }
        req = requests.get('https://api.hh.ru/vacancies/', params=params)
        data = req.content.decode()
        vacant = json.loads(data)
        return vacant

    def print_vacancies(self, vacant):
        """
        метод для вывода вакансий с HeadHunter на печать
        """
        for vacancy in vacant['items']:
            name = vacancy['name']
            employer = vacancy['employer']['name']
            if vacancy['salary'] ==None:
                salary = 0
            else:
                salary = vacancy['salary']['from']
            url = vacancy['alternate_url']
            employer_id = vacancy['employer']['id']
            id_vacancy = vacancy['id']
            print(employer_id, '/', employer, '/', id_vacancy, '/', name, '/', salary, '/', url)


