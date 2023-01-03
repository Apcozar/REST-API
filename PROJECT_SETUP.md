# REST-API
Social Network REST API for Rive Interview

## Set up a development environment with the Python framework and database you have chosen. This might involve installing the necessary software and libraries, as well as creating a new project or application.
1.- Set git project with python .gitignore
2.- Install python 3.11.1
3.- Install visual studio code
4.- Create virtual environment: "python -m venv venv"
5.- Install fastAPI: "pip install fastapi[all]"
6.- Create main.py to set up fastAPI main class.
7.- Set initial skeleton.


## Design the data models and database schema to support relationships between users, such as friends. This might involve creating classes or tables to represent the users and their relationships using SQLAlchemy/SQLModel, Django ORM or any other ORM/query builder of your choice. Please also consider the relationships between the data models and how they will be stored in the database.

alembic revision -m "update table names" -> Creates new revision
alembic upgrade <revision> -> updates with new revision
