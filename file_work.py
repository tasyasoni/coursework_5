import json
from abc import ABC, abstractmethod

class Vacancy:
    def __init__(self, name, employer, salary, requirements, responsibility, url):
        self.name = name
        self.employer = employer
        self.salary = salary
        self.requirements = requirements
        self.responsibility = responsibility
        self.url = url


    def __dict__(self):
        return{"name": self.name,
               "employer": self.employer,
               "salary": self.salary,
               "requirements": self.requirements,
               "responsibility": self.responsibility,
               "url": self.url}


    def __str__(self):
        return self.name


    def compare_salary(self, quantity):
        with open('vacancy.json', 'r', encoding='utf-8') as outfile:
            vacancies_data = json.load(outfile)
            for vacancy in vacancies_data:
                if vacancy['salary'] == None:
                    vacancy['salary'] = 0
                else:
                    vacancy['salary']
            newlist = sorted(vacancies_data, key=lambda d: d['salary'], reverse=True)
            i = 0
            while i < quantity:
                print (newlist[i]['name'], newlist[i]['employer'], newlist[i]['salary'], newlist[i]['url'])
                i += 1


class FileAbsract(ABC):
    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def find_vacancy(self):
        pass
    @abstractmethod
    def del_vacancy(self):
        pass


class Filework(FileAbsract):

    def __init__(self):
        pass

    @staticmethod
    def add_vacancy(file):
        with open('vacancy.json', 'r', encoding='utf-8') as outfile:
            content = json.load(outfile)
        content.append(file.__dict__())
        with open('vacancy.json', 'w', encoding='utf-8') as outfile:
            json.dump(content, outfile, ensure_ascii=False, indent=6)


    def find_vacancy(request):
        with open('vacancy.json', 'r', encoding='utf-8') as outfile:
            content = json.load(outfile)
            for vacancy in content:
                if request in vacancy['employer']:
                    return (vacancy['employer'], vacancy['name'], vacancy['salary'], vacancy['url'])
                else:
                    continue
            return('Данный работодатель пока никого не ищет :((')


    def del_vacancy(self):
        with open('vacancy.json', "w", encoding='utf-8') as outfile:
            content = []
            json.dump(content, outfile)



def created_hh_vacancy(vacant):
    for vacancy in vacant['items']:
        name = vacancy['name']
        employer = vacancy['employer']['name']
        if vacancy['salary']:
            salary = vacancy['salary']['from']
        else:
            salary = 0
        requirements = vacancy['snippet']['requirement']
        responsibility = vacancy['snippet']['responsibility']
        url = vacancy['alternate_url']
        vacancy_for_file = Vacancy(name, employer, salary, requirements, responsibility, url)
        Filework.add_vacancy(vacancy_for_file)


