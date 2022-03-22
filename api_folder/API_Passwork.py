from api_folder.API import ApiData_v1
from api_folder.API import ApiData_v2

class Api_v1:
    server = 'http://172.17.127.22/api/v4'  # хост вашего API

    class Endpoint:
        # Эндпоинты для апи
        login = '/auth/login/'
        logout = '/auth/logout'
        admins_folder = f'/folders/{ApiData_v1.folderID_admins}/passwords'
        users_folder = f'/folders/{ApiData_v1.folderID_users}/passwords'
        securities_folder = f'/folders/{ApiData_v1.folderID_security}/passwords'
        passwords = '/passwords'

class Api_v2:
    server = 'http://172.17.127.22/api/v4'  # хост вашего API

    class Endpoint:
        # Эндпоинты для апи
        login = '/auth/login/'
        logout = '/auth/logout'
        passwords = '/passwords/'