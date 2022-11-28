""" Скачиваем библиотеку requests ибо не знаем какая другая работает с запросами хд) """
import requests

""" Так как Post (HTTP) передает информацию через тело сообщения, а не через параметры строки запроса. 
Используя requests, можно передать данные в параметр data."""


# class PostRestMethod(): //можно через класс(если будем расширять(хотя это противоречит принципу Open/Close),
# но лучше конечно же через обычные переменные)

response = requests.post('https://httpbin.org/post', json={'name': 'test', 'time': '16:18 26.11.2022'})
json_response = response.json()
print(response)

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
