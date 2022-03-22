import requests
from yaml import dump
import base64
from api_folder.API import ApiData_v2
from api_folder.API_Passwork import Api_v2


class PassWork:
    def __init__(self):
        pass
# Здесь скрипт подключается к системе(Passwork) и забирает токен, который нужно передавать в следующие
# запросы
    def login(self, api_key=ApiData_v2.api_key):
        #На данном этапе апи кей вшит в окружение, на проде нужно будет передавать ключ в init
        print('Запускаю сессию')
        print('Захожу в систему')
        url = f'{Api_v2.server}{Api_v2.Endpoint.login}{api_key}'
        responce = requests.post(url=url)
        if responce.status_code == 200:
            print('--OK--')
            responce = responce.json()
        else:
            print(responce.status_code, responce.text)
        print('ТОКЕН получен. Иду дальше\n')
        return responce['data']['token']

# Скрипт обходит папки для забора нужных данных
    def get_all(self, token):
        output = {}
        try:
            # Все id папок находятся в словаре в окружении, поэтому обходим их в цикле
            for folder in ApiData_v2.folders:
                # Забираем айдишник отдельной папки и передаем в запрос
                url = f'{Api_v2.server}/folders/{ApiData_v2.folders[folder]}/passwords'
                head = {'passwork-auth': token}
                responce = requests.get(url=url, headers=head)
                if responce.status_code == 200:
                    raw_data_passwords = responce.json()
                    result = {}
                    # Здесь происходит отбор данных для каждой папки(id пароля, логин и имя)
                    for pswrd in raw_data_passwords['data']:
                        d = {}
                        for entity in pswrd:
                            if entity == 'login':
                                login = pswrd[entity]
                            if entity == 'id' or entity == 'login' or entity == 'name':
                                d[entity] = pswrd[entity]
                        result[login] = d
                    output[folder] = result
        except:
            print('Что-то пошло не так')
        # На выход получаем нужные данные всех паролей
        return output


# На данном этапе скрипт получает зашифрованные пароли и затем дешифрует их
    def get_decrypted_passwords(self, roles, token):
        passwords = {}
        try:
            # Обходим все сущности
            for role in roles:
                print(f'Получаем пароли для группы {role}')
                for user in roles[role]:
                    # Сохраняем в переменную ID пароля
                    id = roles[role][user]['id']
                    # Передаем его в запрос
                    url = f'{Api_v2.server}{Api_v2.Endpoint.passwords}{id}'
                    head = {'passwork-auth': token}
                    responce = requests.get(url=url, headers=head)
                    result = responce.json()
                    # Сохраняем зашифрованный пароль
                    result = result['data']['cryptedPassword']
                    # Здесь делаем конкатенацию для приведения к общему виду
                    passwords[f'{role}_USER'] = f'{roles[role][user]["login"]}'
                    # Дешифруем и присваиваем пароль
                    passwords[f'{role}_PASSWORD'] = base64.b64decode(result).decode('utf-8')
            print('Пароли собраны и обработаны успешно\n')
        except:
            print('Что-то пошло не так')
        # На выходе получаем словарь с паролями и юзерами
        return passwords
# Сохраняет пароли в YAML файл
    def save_to_yaml(self, file):
        print(f'Сохраняем файл YAML\n')
        try:
            from yaml import CDumper as Dumper
        except:
            from yaml import Dumper
        with open('passwords.yaml', 'w', encoding='utf-8') as f:
            dump(file, f, Dumper=Dumper)

# Производит выход из системы
    def logout(self, token):
        print('Закрываем сессию и выходим')
        url = f'{Api_v2.server}{Api_v2.Endpoint.logout}'
        head = {'passwork-auth': token}
        responce = requests.post(url=url, headers=head)
        if responce.status_code == 200:
            return 'Сессия закрыта'
        else:
            print('Что-то пошло не так')
            print(responce.status_code, responce.text)
