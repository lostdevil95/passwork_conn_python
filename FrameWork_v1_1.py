import requests
import json
import base64
from api_folder.API import ApiData_v1
from api_folder.API_Passwork import Api


class PassWork:
    def __init__(self):
        pass
# Здесь скрипт подключается к системе(Passwork) и забирает токен, который нужно передавать в следующие
# запросы
    def login(self):
        print('Запускаю сессию')
        print('Захожу в систему')
        url = f'{Api.server}{Api.Endpoint.login}{ApiData_v1.api_key}'
        responce = requests.post(url=url)
        if responce.status_code == 200:
            print('--OK--')
            responce = responce.json()
        else:
            print(responce.status_code, responce.text)
        print('ТОКЕН получен. Иду дальше\n')
        return responce['data']['token']
# Скрипт обходит папки для забора нужных данных

    def get_roles(self, token):
        output = {}
        print('Забираем пользователей')
        url = f'{Api.server}{Api.Endpoint.users_folder}'
        head = {'passwork-auth': token}
        responce = requests.get(url=url, headers=head)
        if responce.status_code == 200:
            res = responce.json()
            raw_data_passwords = res
            result = {}
            for pswrd in raw_data_passwords['data']:
                d = {}
                for entity in pswrd:
                    if entity == 'login':
                        login = pswrd[entity]
                    if entity == 'id' or entity == 'login' or entity == 'name':
                        d[entity] = pswrd[entity]
                result[login] = d
            output['user'] = result
        else:
            print(responce.status_code, responce.text)
        print('Забираем администраторов')
        url = f'{Api.server}{Api.Endpoint.admins_folder}'
        head = {'passwork-auth': token}
        responce = requests.get(url=url, headers=head)
        if responce.status_code == 200:
            res = responce.json()
            raw_data_passwords = res
            result = {}
            for pswrd in raw_data_passwords['data']:
                d = {}
                for entity in pswrd:
                    if entity == 'login':
                        login = pswrd[entity]
                    if entity == 'id' or entity == 'login' or entity == 'name':
                        d[entity] = pswrd[entity]
                result[login] = d
            output['admin'] = result
        else:
            print(responce.status_code, responce.text)
        print('Забираем секьюрити')
        url = f'{Api.server}{Api.Endpoint.securities_folder}'
        head = {'passwork-auth': token}
        responce = requests.get(url=url, headers=head)
        if responce.status_code == 200:
            res = responce.json()
            raw_data_passwords = res
            result = {}
            for pswrd in raw_data_passwords['data']:
                d = {}
                for entity in pswrd:
                    if entity == 'login':
                        login = pswrd[entity]
                    if entity == 'id' or entity == 'login' or entity == 'name':
                        d[entity] = pswrd[entity]
                result[login] = d
            output['security'] = result
            print('Все роли собраны\n')
            return output
        else:
            print(responce.status_code, responce.text)

# На данном этапе скрипт получает зашифрованные пароли и затем дешифрует их
    def get_decrypted_passwords(self, roles, token):
        passwords = {}
        for role in roles:
            print(f'Получаем пароли для группы {role}')
            passwords[role] = {}
            for user in roles[role]:
                id = roles[role][user]['id']
                url = f'{Api.server}{Api.Endpoint.passwords}/{id}'
                head = {'passwork-auth': token}
                responce = requests.get(url=url, headers=head)
                result = responce.json()
                result = result['data']['cryptedPassword']
                passwords[role][user] = base64.b64decode(result).decode('utf-8')
        print('Пароли собраны и обработаны успешно\n')
        return passwords
# Сохраняет пароли в JSON файл
    def save_to_json(self, file):
        print(f'Сохраняем файл JSON\n')
        with open('passwords.json', 'w', encoding='utf-8') as f:
            json.dump(file, f, ensure_ascii=False)
# Производит выход из системы
    def logout(self, token):
        print('Закрываем сессию и выходим')
        url = f'{Api.server}{Api.Endpoint.logout}'
        head = {'passwork-auth': token}
        responce = requests.post(url=url, headers=head)
        if responce.status_code == 200:
            return 'Сессия закрыта'
        else:
            print('Что-то пошло не так')
            print(responce.status_code, responce.text)
