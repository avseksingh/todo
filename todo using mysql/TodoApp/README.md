# DjangoTodoApp

## Prerequisites
 Please ensure that python, pip, mysqlclient, and MySQL are installed into your system.

## Steps to run this application into your system

### <em>I'm assuming that MySQL is installed and is connected with Django app using mysqlclient.</em>

### 1. Create a new database in the MySQL database engine.
```
CREATE DATABASE testdb;
```

### 2. Create a new user in the MySQL database engine.
```
CREATE USER 'user123'@'localhost' IDENTIFIED WITH mysql_native_password BY '123';
```

### 3. Grant complete access on database "testdb" to user "user123".
```
GRANT ALL ON testdb.* TO 'user123'@'localhost';
```

### 4. Flush the privileges to refresh the MySQL database so that you can use a newly created user.
```
FLUSH PRIVILEGES;
```

### 5. Update the following section in settings.py in the Django project.
```
DATABASES = {<br/>
'default': {<br/>
'ENGINE': 'django.db.backends.mysql',<br/>
'NAME': 'testdb',<br/>
'USER': 'user123',<br/>
'PASSWORD': '123',<br/>
'HOST': 'localhost',<br/>
'PORT': '3306'<br/>
}<br/>
}<br/>
```
### 6. Migrate so that all the required tables of this app will be created in testdb database. It executes SQL commands.
```
python manage.py migrate
```

### 7. Finally, run this application.
```
python manage.py runserver
```
