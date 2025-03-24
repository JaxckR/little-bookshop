# EN - A little bookshop API

For start the project you need python, redis and postgres on your PC or just docker<br>
This is a simple API using a django, DRF, postgres, redis, celery and JWT

<hr>

## Installation without docker:

1. Create and activate environments file:<br>

```console
python -m venv venv
```

```console
source venv/bin/activate
```

2. Install all packages:<br>

```console
pip install -r requirements.txt
```

3. Fill .env-example file and rename to .env(if you're not going to use email backend, you must ignore EMAIL...)
4. Apply migrations:<br>

```console
python manage.py migrate
```

5. And run server:<br>

```console
python manage.py runserver
```

<br><br>

<hr>

## Installation with docker(Recommended)

1. Fill .env-example file and rename to .env(if you're not going to use email backend, you must ignore EMAIL...)
2. Build and up docker(you must be in directory with docker-compose.yml):

```console
docker compose up
```

<br><br><br><br><br>

# RU - API маленького книжного магазина

Для старта проекта вам нужно иметь python, redis, postgres на вашем компьютере или же просто docker<br>
Это простой API с использованием django, DRF, postgres, redis, celery и JWT

<hr>

## Установка без докера:

1. Создайте и активируйте окружение виртуальной среды:<br>

```console
python -m venv venv
```

```console
source venv/bin/activate
```

2. Установите все пакеты:<br>

```console
pip install -r requirements.txt
```

3. Заполните файл .env-example и переименуйте его в .env(Если вы не собираетесь использовать e-mail, то вы не должны заполнять EMAIL...)
4. Примените все миграции:<br>

```console
python manage.py migrate
```

5. И запустите сервер:<br>

```console
python manage.py runserver
```

<br><br>

<hr>

## Установка с докером(Рекомендуемый способ)

1. Заполните файл .env-example и переименуйте его в .env(Если вы не собираетесь использовать e-mail, то вы не должны заполнять EMAIL...)
2. Build and up docker(вы должны находиться в директории с docker-compose.yml):

```console
docker compose up
```