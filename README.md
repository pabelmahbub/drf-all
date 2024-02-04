# drf-all
django rest framework porject:
1. create a folder in pc: ```django-rest-framework```

2. open in vs code in terminal and create a virtual env: 
```python3 -m venv drenv(drenv is our venv name)```

3. Now activate venv in terminal by, 
```source drenv/bin/activate(for mac)```
```drenv/Scripts/activate (for windows)```

4. Need to install django in venv: ```pip install django djangorestframework```
[if error of cpuldn't find a version that satifies the requirements djangorest.... 
```pip install djangorestframework-jsonapi```

5. If pip upgrading needed: ```pip install --upgrade pip```
6. create a project of django by: ```django-admin startproject apiproject(our root app name)```
7. 5a.  root app (apiproject) in settings: add in ```INSTALLED_APP= ['rest_framework']```

```cd apiproject```

```python3 manage.py migrate```

```python3 manage.py startapp myapp(app name)```

7. create a superuser: ```python3 manage.py createsuperuser(name,email,password) and app will start in 127.0.0.0/admijn```

```python3 manage.py runserver```

## Easy steps to create a GET,CREATE,DELETE API:
1. In myapp -> models.py:
```
from django.db import models

# Create your models here.

class Plan(models.Model):
    items = models.CharField(max_length=100)
```
2. In myapp -> admin.py:
```
from django.contrib import admin
from .models import Plan

# Register your models here.
@admin.register(Plan)
class PlanModelAdmin(admin.ModelAdmin):
    list_display = ['id','items', ]
```
a. python3 manage.py makemigrations
b. python3 manage.py migrate

3. In myapp -> create a file serailizers.py:
```
from rest_framework import serializers
from .models import Plan

class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id','items']
 ```
 4. In myapp -> views.py:
 ```
 from django.shortcuts import render
from rest_framework import viewsets
from .seralizers import PlanSerializers
from .models import Plan
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView 
# Create your views here.


class PlanList(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers
    
class PlanCreate(CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers
    
class PlanDestroy(DestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers 
```
5. In myapp -> urls.py:
```
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PlanList.as_view()),
    path('create/', views.PlanCreate.as_view()),
    path('delete/<int:id>', views.PlanDestroy.as_view()),
    
]
```
6. In root app urls.py add it:
```

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api1.urls'))
]
```
A field is added named item in api. GET,CREATE,DELETE api.


## Easy start:

 1. all setting initailly described.
 2. in myapp views.py:
 ```
 from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import Contact
from myapp.serializers import ContactSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics
```

```
class ContactList(generics.ListCreateAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
```
``` 
class ContactDetail(generics.RetrieveUpdateDestroyAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
   queryset = Contact.objects.all()
   serializer_class = ContactSerializer

   def get(self, request, *args, **kwargs):
       return self.retrieve(request, *args, **kwargs)
   
   def put(self, request, *args, **kwargs):
       return self.update(request, *args, **kwargs)
   
   def delete(self, request, *args, **kwargs):
       return self.destroy(request, *args, **kwargs) 
  ```
  
  3. create a file in myapp named urls.py:
  ```
 from django.urls import path
 from myapp import views

urlpatterns = [
     path('student/', views.ContactList.as_view()),
     path('student/<int:pk>/', views.ContactDetail.as_view()),
]
```

4. create a file named serializers.py in myapp:
```
from rest_framework import serializers
from myapp.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name','course','email','phone','address','profession']
```

5. In models.py of myapp:
```
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=30, default='')
    profession = models.CharField(max_length=30, default='')
    
    def __str__(self):
        return self.name
```


after creating models:
```
a. python3 manage.py makemigrations
b. python3 manage.py migrate
c. python3 manage.py runserver
```

6. In admin.py of myapp:
```
from django.contrib import admin
from .models import Contact
# Register your models here.
admin.site.register(Contact)
```

7. Now in root apiproject in urls.py add 5th line:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
```

8. In root app seting.py :
```
CORS POLICY:  Django side:
a. pip install django-cors-headers
b. In settings.py of root app:
 INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'rest_framework',
    'myapp',
    'vueapp',
    'corsheaders',
]

c.
MIDDLEWARE = [
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
]

d. And add the following :

CORS_ALLOWED_ORIGINS = [
    "hhttp://localhost:3000",
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
```
It will fix the cors issues for connecting django-vue/react/angular.

#### In vue side(if needed):

Enable CORS in your Vue app:
Another way to fix CORS issues is to enable CORS in your Vue app. You can do this by adding the axios.defaults.withCredentials = true line to your Vue app's main.js file. This will enable cookies to be sent in CORS requests made by Axios.

```
// main.js

import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

Vue.config.productionTip = false

axios.defaults.withCredentials = true

new Vue({
  render: h => h(App),
}).$mount('#app')
``` 
 ### Permission:
 1. app level: insettings .py
 ```
 REST_FRAMEWORK = {
     'DEFAULT_PERMISSION_CLASSES': [
         'rest_framework.permissions.IsAuthenticated',IsAuthenticatedOrReadOnly, ... 
     ]
}
```
2.In object level:
```
class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    #object level permission-in class/api view:https://www.django-rest-framework.org/api-guide/permissions/#object-level-permissions
    permission_classes = [IsAuthenticatedOrReadOnly] / [IsAuthenticated] / [IsAuthenticated|ReadOnly]
 /[IsAdmin]
    #.IsAuthenticatedOrReadOnly-used loggedIn but can only read
    #.IsAuthenticated-Only read and write if authenticated
    #.IsAuthenticated|ReadOnly - 
    ....
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchList=pk)
  ```


# How to install mySQL in Mac:
```
1.in ROOT terminal: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. In terminal: brew install pkg-config
3. In terminal: brew install mysql
4. In terminal:export MYSQLCLIENT_CFLAGS=-I/usr/local/opt/mysql/include
5. In terminal: export MYSQLCLIENT_LDFLAGS=-L/usr/local/opt/mysql/lib
6. In drf environment terminal: pip install mysqlclient

Change db:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drfAll',
        'USER': 'root',
        'PASSWORD':'japan56789',
        'HOST': 'localhost',  # Or the IP address of your MySQL server
        'PORT': '3306',  # Or the appropriate port for your MySQL instance
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
Now in drf app:
1. python manage.py makemigrations
2. python manage.py migrate
   ```



