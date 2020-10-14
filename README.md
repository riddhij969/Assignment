# Django Rest Framework API

# Description
    This API uses GET/POST/PUT/DELETE request to communicate and HTTP response codes to indenticate status and errors. All responses come in standard JSON. All requests must         include a content-type of application/json and the body must be valid JSON. This API consists products of Mobile and Laptop.
    By default Django REST Framework will produce a response like:

    {
          "id": 2,
          "Model_No": "A2",
          "Name": "MI",
          "Description": "Good Phone",
          "RAM": 4,
          "Processor": "2.83",
          "Type": "Mobile"
      },

# Prerequisites:

    . Python3 (with pip)
    . Django
    . Django REST Framework
    . Pycharm
  
  
# INSTALLATION

    . pip install django
    . pip install djangorestframework
    . pip install mysqlclient
    . pip install oauth2
    . pip install requests
    . pip install django-heroku
    . pip install gunicorn
  
# Configure MySQL Database
  
    Open your settings.py file and make changes.

    'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'your schema name',   (In my case schema name is products)
          'USER': 'your user name',     (In my case user name is root)
          'PASSWORD': 'your user password',
          'HOST': 'localhost',
          'PORT': '3306',
      }

# Running/ Development
  
    . python manage.py makemigrations
    . python manage.py migrate
    . python manage.py runserver
    . visit your API at http://127.0.0.1:8000/
    . For admin - http://127.0.0.1:8000/admin/
    . My user name - Riddhi
    . My user password - Rj@123456
    . For API View - http://127.0.0.1:8000/api/products_list/
  
# Deploying
  
    . Create a Heroku account
    . Create a Heroku application
    . heroku login
    . git init
    . heroku git:remote -a <AppName>
    . git add .
    . git commit -m "first commit"
    . git push heroku master


# Postman Collection:

    <The request type>

    GET | POST | PUT | DELETE    
  
    The get() method sends a GET request to the specified url.
  ![Get ](https://user-images.githubusercontent.com/69605346/96024279-25035200-0e71-11eb-9eae-c5429d72baf7.png)
 
    The post() method is used to create a new resource into the collection of resources.
  ![Post](https://user-images.githubusercontent.com/69605346/96026229-defbbd80-0e73-11eb-9afd-61f3878cbce6.png)
  
    The put() method is used to update existing resources.
  ![Put](https://user-images.githubusercontent.com/69605346/96027671-d4dabe80-0e75-11eb-8833-73f1dfb4141b.png)

    The delete() method is used to delete existing resources.
  ![Delete](https://user-images.githubusercontent.com/69605346/96028019-677b5d80-0e76-11eb-9088-5c526f0513aa.png)



