# REST-API //IN PROGRESS
Social Network REST API for Rive Interview

## Set up a development environment with the Python framework and database you have chosen. This might involve installing the necessary software and libraries, as well as creating a new project or application.
<ol>
  <li>Set git project with python .gitignore</li>
  <li>Install python 3.11.1</li>
  <li>Install visual studio code</li>
  <li>Create virtual environment: "python -m venv venv"</li>
  <li>Install fastAPI: "pip install fastapi[all]"</li>
  <li>Create main.py to set up fastAPI main class.</li>
  <li>Set initial skeleton.</li>
</ol>


## Design the data models and database schema to support relationships between users, such as friends. This might involve creating classes or tables to represent the users and their relationships using SQLAlchemy/SQLModel, Django ORM or any other ORM/query builder of your choice. Please also consider the relationships between the data models and how they will be stored in the database.

alembic revision -m "update table names" -> Creates new revision
alembic upgrade <revision> -> updates with new revision
