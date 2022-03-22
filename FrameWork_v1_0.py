import requests
import json
import base64
from api_folder.API import ApiData_v1
from api_folder.API_Passwork import Api_v1


class PassWork:
    def __init__(self):
        pass

    def login(self):
        print('start session')
        print('Login to the system')
        url = f'{Api_v1.server}{Api_v1.Endpoint.login}{ApiData_v1.api_key}'
        responce = requests.post(url=url)
        if responce.status_code == 200:
            print('--OK--')
            responce = responce.json()
        else:
            print(responce.status_code, responce.text)
        print('Got the token')
        return responce['data']['token']

    def get_roles(self, role, token):
        if role.lower() == 'user':
            print('Забираем пользователя')
            url = f'{Api_v1.server}{Api_v1.Endpoint.users_folder}'
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
                return result
            else:
                print(responce.status_code, responce.text)
        elif role.lower() == 'admin':
            print('Забираем администратора')
            url = f'{Api_v1.server}{Api_v1.Endpoint.admins_folder}'
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
                return result
            else:
                print(responce.status_code, responce.text)
        elif role.lower() == 'security':
            print('Забираем секьюрити')
            url = f'{Api_v1.server}{Api_v1.Endpoint.securities_folder}'
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
                return result
            else:
                print(responce.status_code, responce.text)
        else:
            return 'Вы должны передать в функцию строку с именем запрашиваемой группы'

    def get_encrypted_passwords(self, role, token):
        passwords = {}
        for login in role:
            print('Получаем пароли')
            id = role[login]['id']
            url = f'{Api_v1.server}{Api_v1.Endpoint.passwords}/{id}'
            head = {'passwork-auth': token}
            responce = requests.get(url=url, headers=head)
            result = responce.json()
            passwords[login] = result['data']['cryptedPassword']
        return passwords

    def complete_data(self, login, raw_pswds):
        output = {}
        if isinstance(login, str) and login in raw_pswds:
            print(f'Получаем пароль для пользователя {login}')
            for login_in in raw_pswds:
                if login.lower() in login_in.lower():
                    output['login'] = login
                    psw = raw_pswds[login]
                    pswd = base64.b64decode(psw).decode('utf-8')
                    output['password'] = pswd
                    json.dumps(output)
                    return output
        else:
            return f'Проверьте введенный вами логин. Вы должны передать логин пользователя, регистр важен. Вы ввели {login}'

    def save_to_json(self, file):
        print(f'Сохраняем файл JSON')
        with open('password.json', 'w', encoding='utf-8') as f:
            json.dump(file, f, ensure_ascii=False)

    def logout(self, token):
        print('Закрываем сессию и выходим')
        url = f'{Api_v1.server}{Api_v1.Endpoint.logout}'
        head = {'passwork-auth': token}
        responce = requests.post(url=url, headers=head)
        if responce.status_code == 200:
            return 'Сессия закрыта'
        else:
            print('Что-то пошло не так')
            print(responce.status_code, responce.text)
