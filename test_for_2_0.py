from FrameWork_v2_0 import PassWork


API = PassWork()
# Открываем сессию, логинимся с помощью api-key, установить другой апи кей
# или скрыть можно в env - Api_key.ApiData_v2
TOKEN = API.login()
# Выбираем роль(админ/секьюрити/админ)
GET_ROLE = API.get_all(TOKEN)
# Забираем зашифрованныe для этой группы и дешифруем
ALL_PASSWORDS = API.get_decrypted_passwords(GET_ROLE, TOKEN)
# Сохраняем пароль пользователя в файл YAML
# (можно зашифровать файл и при передаче расшифровать)
GET_FILE = API.save_to_yaml(ALL_PASSWORDS)
# Завершаем сессию
API.logout(TOKEN)
