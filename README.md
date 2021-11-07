# Recruitment task Embiq
Github projects managment

## Setup 

### Docker
Docker version 20.10.8, build 3967b7d

1. Rename .env-example to .env
2. Go to Docker directory.
2. Run shell script ./run.sh to setup Docker container
3. Application will be working on host: http://127.0.0.1:8000/ (if it is busy you can change it in docker-compose.yml)

To destroy container run shell script file 
```
./destroy.sh
```
### Manually
#### Requirements
* Python3
* pip

1. Rename .env-example to .env
2. In project directory:

#### Unix
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py makemigrations embiq_app
$ python3 manage.py migrate
$ python3 manage.py seed
$ python3 manage.py runserver 127.0.0.1:8000
```
#### Windows
```
$ python3 -m venv venv
$ .\venv\Scripts\activate
$ pip install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py makemigrations embiq_app
$ python3 manage.py migrate
$ python3 manage.py seed
$ python3 manage.py runserver 127.0.0.1:8000
```

## Documentation
Added swagger documentation on **'/docs'** endpoint

## Authentication
Authentication via Github Ouath2
Endpoints require token authentication in header
```
$ Authorization: Token XXXXXXXXX
```
Getting token form endpoint:
```
$ /auth/github/token/
```

