import requests
import json

url = "https://akabab.github.io/superhero-api/api/all.json"
request = requests.get(url)
her_list = json.loads(request.text)

class Super_hero_brain:

    def __init__(self, super_heroes):
       self.super_heroes = super_heroes

    def get_intelligence(self):
        intelligence = {}

        for hero in self.super_heroes:
            for item in her_list:
                if item['name'] == hero:
                    intelligence.update({item['name']: item['powerstats']['intelligence']})
        most_intelligence = max(intelligence.items(), key=lambda item: item[1])
        return most_intelligence


if __name__ == '__main__':
    heroes = input('Введите героев через запятую с заглавной буквы: ').split(', ')

    result = Super_hero_brain(heroes)

    print(f'Самый умный из указанных супер героев: {result.get_intelligence()[0]}, его ум: {result.get_intelligence()[1]} пунктов')

