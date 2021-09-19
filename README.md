# Recruitment task Iteo
Computing sum and average values for applied columns

## Setup 

### Docker
1. Rename .env-example to .env
2. Run shell script ./Docker/run.sh to setup Docker container
3. Application will be working on host: http://127.0.0.1:8000/ or http://0.0.0.0:8000/

To destroy container run shell script file 
```
./Docker/destroy.sh
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
$ python3 manage.py runserver
```
#### Windows
```
$ python3 -m venv venv
$ .\venv\Scripts\activate
$ pip install -r requirements.txt
$ python3 manage.py runserver
```

## Swagger
Added swagger documentation on **'/swagger'** endpoint

