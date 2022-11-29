""" Скачиваем библиотеку requests ибо не знаем какая другая работает с запросами хд) """
from datetime import datetime

import requests

""" Так как Post (HTTP) передает информацию через тело сообщения, а не через параметры строки запроса. 
Используя requests, можно передать данные в параметр data."""


# class PostRestMethod(): //можно через класс(если будем расширять(хотя это противоречит принципу Open/Close),
# но лучше конечно же через обычные переменные)

response = requests.post('https://httpbin.org/post', json={'name': 'test', 'time': '11:25 26.11.2022'})
# не нашел информацию по TLCListener, но и этот запрос рабочий типо
json_response = response.json()
datetime = datetime.now()
print(response)
# Ответ приходит, <Response [200]> (круто верно?)

if datetime == response.request.body:  # Но на этой строке он почемуто ломается и не выводит текущую дату, суть в том что он должен отработать когда наступит время(time), но сейчас почему-то не работает
    print('Выполнение команды')
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')
else:
    print("Ничего не работает")
