# PROJECT_SETUP
Social Network REST API project setup for Rive Interview

## DEPLOYED API
To save time to you, I deployed the app in heroku.

username: admin@admin.com
password: riveadmin
API LINK: https://social-network-rest-api.herokuapp.com/

## LOCAL SET UP
<ol>
  <li>Install python 3.11.1</li>
  <li>Install postgreSQL 15.1</li>
  <li>Install any IDE (visual studio code) in my case</li>
  <li>Create virtual environment: python -m venv venv</li>
  <li>Activate virtual envonment: venv\Scripts\activate.bat</li>
  <li>Install dependencies into venv from requirements.txt: pip install -r requirements.txt</li>
  <li>Create database in PostgreSQL in GUI</li>
  <li>Create ".env" file and set constants (in my case):
        
      DATABASE_HOSTNAME=localhost
      DATABASE_PORT=5432
      DATABASE_PASSWORD=root
      DATABASE_NAME=social_network_db
      DATABASE_USERNAME=postgres
      SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
      ALGORITHM=HS256
      ACCESS_TOKEN_EXPIRE_MINUTES=60
      ADMIN_PWD=riveadmin
  </li>
  <li>Run command to start the app: uvicorn src.main:app (--reload flag to reload when we save)</li>
  <li>Click the link with the app url to access it.</li>
  <li>Once we are in the root page, I setted a create an admin user for authorization purposes. This is not the best way to       do it, but I couldn't find any "post startup" to do it in the cleanest way. </li>
  <li>Read the page, and add /docs to the URL to try de API and read the openAPI documentation.</li>
</ol>
