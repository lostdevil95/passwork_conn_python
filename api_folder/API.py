class ApiData_v1:
    # Здесь хранится информация о сейфах, папках, ключах..
    # for framework v1.0 and v1.1
    api_key = '*****************'  # Введите ваш api_key
    vault_ASCII_id = '61c180c971c24646ad61d482'
    folderID_admins = '61c1b62476768d09ad7436fe'
    folderID_users = '61c3262224550d6f9a4961de'
    folderID_security = '61c3271824550d6f9a4961e8'


# for framework v2.0
class ApiData_v2:
    # Введите ваш api_key(Данный ключ выступает дефолтным(для dev), если не передан конкретный)
    api_key = '******************************'
    # Сейф, где хранятся пароли под нужды АСЦУИ
    vault_ASCII = '61dc2e03c7f8285d5062a141'
    # Папки всех сущностей
    folders = {'AD_SERVER': '61dc2eb4f18e9a5a9a46a332',
               'AD_USER': '61dc2f07f18e9a5a9a46a33b',
               'COD_LIST_SERVER': '61dc2e790bd6f17e0b7a4e74',
               'DNS_SERVER': '61dc2ec3f18e9a5a9a46a336',
               'FS': '61dc2ee2c7f8285d5062a15c',
               'HOST': '61dc2e33c7f8285d5062a14a',
               'HUAWEI_SERVER': '61dc2f35f18e9a5a9a46a343',
               'MAIL_SERVER': '61dc2f26f18e9a5a9a46a33f',
               'MRIP_FILE_SERVER': '61dc2ef30bd6f17e0b7a4e7a',
               'RP_LIST_SERVER': '61dc2e90f18e9a5a9a46a32d',
               'SATELLITE': '61dc2e47f18e9a5a9a46a329',
               'SCOM': '61dc2ec9c7f8285d5062a158',
               'SNAP_CENTER': '61dc2e4f0bd6f17e0b7a4e6f',
               'SVOD_TP_LIST_SERVER': '61dc2ea9c7f8285d5062a153',
               'VC': '61dc2e29c7f8285d5062a146'}
