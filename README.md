#### __pakages to be installed__
 - pip3 install Django==3.2 gunicorn
 - pip3 install dj_database_url psycopg2
 - pip3 install dj3-cloudinary-storage
 - pip3 freeze -- local > requirements.txt
 - django-admin startproject codestar .  this is the code to create the new django project
 - python3 manage.py startapp blog
 - python3 manage.py migrate   this migrates all our changes to the DB

 - python3 manage.py runserver    this is the code to run the file
