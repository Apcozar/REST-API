# PROJECT_SETUP
Social Network REST API project setup for Rive Interview

## DEPLOYED API
To save time to you, I deployed the app in heroku.

API LINK: https://social-network-rest-api.herokuapp.com/

## LOCAL SET UP
1.- Set git project with python .gitignore
1.- Install python 3.11.1
2.- Install any IDE (visual studio code) in my case
3.- Create virtual environment: python -m venv venv
4.- Activate virtual envonment: venv\Scripts\activate.bat
5.- Install dependencies into venv from requirements.txt: pip install -r requirements.txt
6.- Create database in PostgreSQL
7.- Create ".env" file and set constants (in my case):

  DATABASE_HOSTNAME=localhost
  DATABASE_PORT=5432
  DATABASE_PASSWORD=root
  DATABASE_NAME=social_network_db
  DATABASE_USERNAME=postgres
  SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
  ALGORITHM=HS256
  ACCESS_TOKEN_EXPIRE_MINUTES=60
  
8.- Run command to start the app: uvicorn src.main:app (--reload flag to reload when we save)
9.- Click the link with the app url to access it.
10.- Once we are in the root, I setted a create an admin user for authorization purposes. This is not the best way to do        it, but I couldn't find any "post startup" to do it in the cleanest way. 
11.- Read the page, and add /docs to the URL to try de API and read the openAPI documentation.
