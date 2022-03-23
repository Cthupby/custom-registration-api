# Custom registration api  

Custom registration application made with [Django REST framework](https://www.django-rest-framework.org/)

## Installation
1. Download the custom-registration-api
2. Create and activate virtual environment  
   ```python -m virualenv venv```  
   ```source ./venv/bin/activate```
3. Install the required libraries  
  ```pip install -r requirements.txt```

## Usage 
For using custom-registration-api enter  
```gunicorn custom_registration.wsgi```  or  ```python manage.py runserver 8000```  

## The REST application made with Django Rest Framework:  
  
```https://localhost:8000/api/clients/create/```  

When registering, the user can specify information about himself, which is collected in a dictionary Json-file:  


```
{
    "username": "",
    "email": "",
    "password1": "",
    "password2": "",
    "avatar": null,
    "gender": null,
    "first_name": "",
    "last_name": ""
}
```

