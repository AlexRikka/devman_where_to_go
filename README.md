# Куда пойти — Москва глазами Артёма

Сайт о самых интересных местах в Москве. Авторский проект Артёма.

[Ссылка на сайт](https://alexrikka.pythonanywhere.com/)

## Окружение

### Требования
Для запуска сайта вам понадобится Python 3.10. Скачайте репозиторий и установите python пакеты из `requirements.txt`:
```bash
git clone https://github.com/AlexRikka/devman_where_to_go.git
cd devman_where_to_go
pip install -r requirements.txt
```

### Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в корне проекта и добавьте в него следующие переменные: 
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

### Запуск

Создайте базу данных SQLite:
```
python manage.py migrate
```

Загрузите данные о локациях с помощью команды `load_place`, которая принимает одну ссылку на файл json:
```
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9A%D0%BE%D0%B2%D0%BE%D1%80%D0%BA%D0%B8%D0%BD%D0%B3%20Gravity.json
```

Запустите сервер:
```
python manage.py runserver
```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

