from requests import get, post, delete

print(get('http://127.0.0.1:8080/api/v2/users').json())
print(get('http://127.0.0.1:8080/api/v2/users/1').json())
print(get('http://127.0.0.1:8080/api/v2/users/999').json()) # такого пользователя нет в базе
print(get('http://127.0.0.1:8080/api/v2/users/abc').json()) # id не является числом

print(post('http://127.0.0.1:8080/api/v2/users', json={'name': 'Igor',
                                                       'surname': 'Sadovnikov',
                                                       'position': 'student',
                                                       'age': 16,
                                                       'address': 'Kazan',
                                                       'speciality': 'computer sciences',
                                                       'hashed_password': 'qwerty',
                                                       'email': 'abc@mail.ru'}).json())
print(post('http://127.0.0.1:8080/api/v2/users', json={}).json()) # пустой json
print(post('http://127.0.0.1:8080/api/v2/users', json={'name': 'Igor'}).json()) # не все поля

print(delete('http://127.0.0.1:8080/api/v2/users/1').json())
print(delete('http://127.0.0.1:8080/api/v2/users/999').json()) # нет в базе