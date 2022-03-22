from FrameWork_v1_0 import PassWork
from api_folder.API import ApiData_v1

key = ApiData_v1.api_key
API = PassWork()
ROLE = 'user'  # Роли - user, admin, security.. Регистр не важен
LOGIN = 'longtimesupport'  # Логин пользователя.. Регистр не важен
# Открываем сессию, логинимся с помощью api-key, установить другой апи кей или скрыть можно в env - Api_key.ApiData
TOKEN = API.login()
# Выбираем роль(админ/секьюрити/админ)
GET_ROLE = API.get_roles(ROLE ,TOKEN)
# Забираем зашифрованныe для этой группы
RAW_ALL_PASSWORDS = API.get_encrypted_passwords(GET_ROLE, TOKEN)
# Дешифруем пароль конкретного пользователя(юзера/админа/секьюрити)
PASSWORD = API.complete_data(LOGIN, RAW_ALL_PASSWORDS)
# Сохраняем пароль пользователя в файл JSON (можно зашифровать файл и при передаче расшифровать)
GET_FILE = API.save_to_json(PASSWORD)
# Завершаем сессию
API.logout(TOKEN)
