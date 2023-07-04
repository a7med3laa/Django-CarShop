# Django-CarShop

My first Django project

------------

## Project functions

Create a project called myproject that has a Cars App that includes:

1. Model.py: It has two tables:
   - Driver (name and license)
   - Car (Make/Model and VIN and foreign key to the driver table)
2. views.py: It has 4 functions to view tables data and to submit new data

3. Template folder as HTML files

------------


## Run Project

clone repo and open the command line in the folder directory and install virtualenv and Django

- Virtual Environment

download virtual environment
`pip install virtualenv`

Convert the folder to a virtual environment
`virtualenv venv`

To begin with Django, you first need to activate virtualenv
The command to activate 
`venv\Scripts\activate`
The command to deactivate
`venv\Scripts\deactivate.bat`

- Install Django

`pip install Django`

- Install PostgreSQL

Install Postgres and create DB called Car and update the setting.py file with your password then run the following commands in CMD

`pip install psycopg2-binary `
To provide connection to postgre

`Py manage.py makemigrations `

`Py manage.py migrate`

To update the project and create tables in model.py to Car DB

