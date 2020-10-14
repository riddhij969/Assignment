# Django Rest Framework API

# Description
    This API uses GET/POST/PUT/DELETE request to communicate and HTTP response codes to indenticate status and errors. 
    All responses come in standard JSON. All requests must include a content-type of application/json and the body must be valid JSON.
    This API consists products of Mobile and Laptop.
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

    . Python3
    . Pycharm
    . Django
    . Django REST Framework  
  
# Installation

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
    
   ![admin](https://user-images.githubusercontent.com/69605346/96028525-04d69180-0e77-11eb-92eb-9c9548a920a4.png)
   
    . For API View - http://127.0.0.1:8000/api/products_list/
    
   ![products_list](https://user-images.githubusercontent.com/69605346/96028869-83333380-0e77-11eb-8bc9-2e92a47cbb5e.png)
  
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
  ![Get](https://user-images.githubusercontent.com/69605346/96029646-9266b100-0e78-11eb-963b-8a338efcf6ff.png)
 
    The post() method is used to create a new resource into the collection of resources.
  ![Post](https://user-images.githubusercontent.com/69605346/96029932-f2f5ee00-0e78-11eb-8f92-034705d16b60.png)
  
    The put() method is used to update existing resources.
  ![Put](https://user-images.githubusercontent.com/69605346/96030335-829b9c80-0e79-11eb-9b70-6466e706a124.png)

    The delete() method is used to delete existing resources.
  ![Delete](https://user-images.githubusercontent.com/69605346/96030508-b5459500-0e79-11eb-8b7a-c6b4dfa5231f.png)
  
# Result

  ![Database](https://user-images.githubusercontent.com/69605346/96032084-d1e2cc80-0e7b-11eb-936e-da5b833a1def.png)
