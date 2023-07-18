создаем виртуальное окружение
& C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe -m venv venv   

активируем виртуальное окружение
venv\scripts\activate

обновление пакетного менеджера
python -m pip install --upgrade pip

устанавлеваем framework
pip install django


создаем проект
django-admin startproject store_project

переходим в папку проекта
cd store_project

создаем приложение
python manage.py startapp store

подключаем баззу данных и создаем вспомагательные таблицы
python manage.py migrate

запускаем сервер
python manage.py runserver

останавлеваем  сервер
ctrl + c

настройки - добавить приложение 
INSTALLED_APPS  

при изменении структуры баззы данных
python manage.py makemigrations
python manage.py migrate

регистрируем администратора
python manage.py createsuperuser

работа с изображениями
pip install pillow 