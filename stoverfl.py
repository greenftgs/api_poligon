import requests

from datetime import datetime, timedelta
time_now = datetime.now().timestamp()
dt = datetime.now() - timedelta(days=2)
two_days_ago = dt.timestamp()

api_url = 'https://api.stackexchange.com'
questions_request = f'/2.3/questions?fromdate={int(two_days_ago)}&todate={int(time_now)}&order=desc&sort=activity&tagged=python&site=stackoverflow'

response = requests.get(api_url + questions_request)
all_found_questions = response.json()

print('Все вопросы за последние два дня на сайте "stackoverflow" с тегом "Python":\n')
for question_search in all_found_questions['items']:
    print(question_search['title'].strip(), question_search['link'].strip())