from pprint import pprint

import requests

def take_token():
    with open('../../Desktop/toke.txt', 'r') as file:
        return file.readline()

class YaUploader:
    files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    @property
    def headers(self):
        return {
            'Content_Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, file_path: str):
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(self.upload_url, params=params, headers=self.headers)
        print(response.json())
        return response.json()

    def upload(self, file_path):
        href = self.get_upload_link(file_path).get('href')
        if not href:
            return False

        with open(file_path, 'rb') as file:
            response = requests.put(href, data=file)
            if response.status_code == 201:
                print('Загрузка фала проведена успешно')
                return True
            print('Ошибка загрузки: ', response.status_code)
            return False

ya_client = YaUploader(take_token())
ya_client.upload('pdf.pdf')



#         {
#             "href": "string",
#             "method": "string",
#             "templated": true
#         }
#
#
# if __name__ == '__main__':
#     # Получить путь к загружаемому файлу и токен от пользователя
#     path_to_file = 'c:/Users/Gospartner/PycharmProjects/pythonProject1/pdf.pdf'
#     token = y0_AgAAAABj5QsgAADLWwAAAADWVEBAeiZ6aZJBReGBm_v2SqllUU5q_f0
#     uploader = YaUploader(token)
#     result = uploader.upload(path_to_file)