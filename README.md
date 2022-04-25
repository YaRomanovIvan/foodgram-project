# Foodgram ![example workflow](https://github.com/YaRomanovIvan/foodgram-project/actions/workflows/foodgram.yml/badge.svg)
«Продуктовый помощник».  
Это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.  
Ссылка http://foodgram-food.ga/

# Стек технологий  
  ***nginx, gunicorn, Django, Django REST, python, docker, docker-compose***
# Установка
1. Обновляем пакеты, устанавливаем postgres и nginx:
  ***sudo apt update -y && apt upgrade -y && apt install nginx postgresql -y*** 
2. Клонируем репозиторий:  
  ***git clone***  
3. Создаем контейнер:  
  ***docker-compose up -d***  
4. Выполняем миграции:  
  ***docker-compose exec web python manage.py migrate --noinput***  
5. Создаем суперпользовотеля:  
  ***docker-compose exec web python manage.py createsuperuser***  
6. Собираем статику:  
  ***docker-compose exec web python manage.py collectstatic --no-input***  
7. Загружаем данные:  
  ***docker-compose exec web python manage.py loaddata fixtures.json***  

# Об авторе  
Я являюсь выпускником Яндекс Практикума по направлению python-разработчик. Данная работа была выполнена мной как итоговый проект курса! Путь был долог и труден, но я справился)
