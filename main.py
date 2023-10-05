import requests
import json

params = {
   "text": 'Яндекс',
   # "employer_id": 3529,
   'per_page': 100
}
req = requests.get('https://api.hh.ru/vacancies/', params=params)
data = req.content.decode()
vacant = json.loads(data)
print(vacant)

result = []
for vacancy in vacant['items']:
    name = vacancy['name']
    employer = vacancy['employer']['name']
    if vacancy['salary'] == None:
        salary = 0
    else:
        salary = vacancy['salary']['from']
    url = vacancy['alternate_url']
    employer_id = vacancy['employer']['id']
    id_vacancy = vacancy['id']
    dictionary = {'id_company': employer_id,
                  'company_name': employer,
                  'id_vacancy': id_vacancy,
                  'vacancy_name': name,
                  'salalry': salary,
                  'link':url
    }
    result.append(dictionary)
with open("vacancy.json", 'w') as outfile:
    json.dump(result, outfile, ensure_ascii=False, indent=6)

