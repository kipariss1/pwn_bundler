This is backend Django part of the project. To run it, you'll
need:

 - install python
 - create venv (optionally)
 - install all dependencies
 ```
pip install -r requirements.txt
 ```
 - add yours API keys for Etherium blockchain (I got mine from www.alchemy.com) and for Moralis services (www.developers.moralis.com) into settings.py
 - makemigrations
 ```
 python manage.py makemigrations
 python manage.py migrate
 ```
 - runserver
 ```
python manage.py runserver
 ```