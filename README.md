# Bank Security Panel

Система мониторинга безопасности для банковских учреждений. Проект реализован на Django и предоставляет панель управления для отслеживания подозрительной активности, визитов и обеспечения безопасности.

## Установка

#### Клонируйте репозиторий:
    git clone https://github.com/Equ17y/Bank_security_panel_-Part_2-.git
    cd Bank_security_panel_-Part_2-

#### Создайте виртуальное окружение:
    python -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    # или
    venv\Scripts\activate     # Для Windows

#### Установите зависимости:
    pip install -r requirements.txt

### Обязательные настройки

`DEBUG`  Режим отладки. Используйте `True` только для разработки. Для production всегда `False`.

#### Настройте базу данных:
    
    DEBUG=True
    DB_ENGINE=django.db.backends.postgresql
    DB_HOST=ваш_хост
    DB_PORT=ваш_порт
    DB_NAME=имя_бд
    DB_USER=ваш_логин
    DB_PASSWORD=ваш_пароль
    SECRET_KEY=ваш_секретный_ключ

`DB_ENGINE` Движок базы данных (для PostgreSQL используйте `django.db.backends.postgresql`) [ENGINE](https://docs.djangoproject.com/en/5.2/ref/settings/#engine)

`DB_HOST`	Адрес сервера базы данных [Host](https://docs.djangoproject.com/en/5.2/ref/settings/#host)

`DB_PORT`	Порт подключения к БД (по умолчанию 5432 для PostgreSQL) [PORT](https://docs.djangoproject.com/en/5.2/ref/settings/#port)

`DB_NAME`	Имя базы данных [NAME](https://docs.djangoproject.com/en/5.2/ref/settings/#name)

`DB_USER`	Пользователь БД [USER](https://docs.djangoproject.com/en/5.2/ref/settings/#user)

`DB_PASSWORD`	Пароль пользователя БД [PASSWORD](https://docs.djangoproject.com/en/5.2/ref/settings/#password)

`SECRET_KEY`	Криптографический ключ для защиты Django. Должен быть уникальным! [SECRET_KEY](https://docs.djangoproject.com/en/5.2/ref/settings/#secret-key)
   
#### Запустите сервер разработки:
    python manage.py runserver