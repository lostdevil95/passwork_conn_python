from FrameWork_v1_1 import PassWork
from api_folder.API import ApiData_v1

key = ApiData_v1.api_key
API = PassWork()
# Открываем сессию, логинимся с помощью api-key, установить другой апи кей или скрыть можно в env - Api_key.ApiData
TOKEN = API.login()
# Выбираем роль(админ/секьюрити/админ)
GET_ROLE = API.get_roles(TOKEN)
# Забираем зашифрованныe для этой группы и дешифруем
ALL_PASSWORDS = API.get_decrypted_passwords(GET_ROLE, TOKEN)
# Сохраняем пароль пользователя в файл JSON (можно зашифровать файл и при передаче расшифровать)
GET_FILE = API.save_to_json(ALL_PASSWORDS)
# Завершаем сессию
API.logout(TOKEN)
