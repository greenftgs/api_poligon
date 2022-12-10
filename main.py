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
        return response.json()

    def upload(self, file_path):
        href = self.get_upload_link(file_path).get('href')
        if not href:
            return print(f'Ошибка загрузки: {self.get_upload_link(file_path)["message"]}')

        with open(file_path, 'rb') as file:
            try:
                response = requests.put(href, data=file)
                if response.status_code == 201:
                    print('Загрузка файла проведена успешно')
            except (FileNotFoundError, Exception, KeyError):
                print(f'Ошибка загрузки: , {self.get_upload_link(file_path)["message"]}')


ya_client = YaUploader(take_token())
ya_client.upload('pdf.pdf')
