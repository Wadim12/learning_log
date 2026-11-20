# Learning Log — электронный журнал обучения

Современный адаптивный сайт на Python 3.12 + Django 5.2 + SQLite.

## Возможности
- Регистрация, вход и выход пользователей.
- Личные темы обучения: каждый пользователь видит только свои темы.
- Создание, просмотр, редактирование и удаление тем.
- Записи внутри каждой темы: добавление, редактирование и удаление.
- Поиск по названиям тем.
- Главная панель со статистикой и быстрыми действиями.
- Адаптивный интерфейс для телефона и компьютера.

## Запуск на Windows (PowerShell)
```powershell
py -3.12 -m venv ll_env
.\ll_env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Откройте http://127.0.0.1:8000/

## Запуск на Linux / macOS
```bash
python3.12 -m venv ll_env
source ll_env/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Админ-панель: http://127.0.0.1:8000/admin/

Для учебной локальной демонстрации используется DEBUG=True. Перед публикацией в интернете нужно настроить SECRET_KEY, DEBUG=False, ALLOWED_HOSTS, HTTPS и статические файлы.
