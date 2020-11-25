
# Health++
Health++ is an application that helps user to manage their diet and calories consumption. It provides a common platform for dieticians and their patients, so that they can manage a proper diet. It also generates personalized infographics so that user properly understands his nutrition level.
# Run deployed website
Deployed at Heroku: [![img](https://i.ibb.co/2yZQT2S/deploy-32.png)](https://health-plus-plus.herokuapp.com/) (Click this image)

# Run locally
**Clone the Repository using:**

    git clone --single-branch --branch local https://github.com/AnonySharma/Django-HealthPlusPlus.git
    cd Django-HealthPlusPlus

**Basic Setup:**<br>
*(Run this to use shell shortcuts)*

    chmod +x s.sh

**Create virtual environment:**

    pip install virtualenv
    virtualenv venv
    
    source venv/bin/activate (for linux)
    ./venv/scripts/activate (for windows)
 
**Install required packages:**

    pip install -r requirements.txt

**Setup the database:**<br>
In the following code, replace \<USER> with any username of your choice.<br>
In the following code, replace \<PASS> with any password of your choice.

    mysql -u root -p
    create database HPP_database;
    create user '<USER>'@'localhost' identified by '<PASS>';
    grant usage on *.* to '<USER>'@'localhost';
    grant all priveleges on HPP_database.* to '<USER>'@'localhost';

**Setup settings.py**
<br>
*(Replace the following code in settings.py)* <br>
In the following code, replace \<USER> with the username you created above.<br>
In the following code, replace \<PASS> with the password you created above.<br>

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'HPP_database',
        'USER' : '<USER>',
        'PASSWORD' : '<PASS>',
        'HOST' : 'localhost',
        }
    }

**Then make migrations:**

    ./s.sh make
    or
    python3 manage.py makemigrations

**Then migrate the migrations:**

    ./s.sh mig
    or
    python3 manage.py migrate

**Then create a super-user:**

    ./s.sh sup
    or
    python3 manage.py createsuperuser

**Then run the server:**

    ./s.sh run
    or
    python3 manage.py runserver

# Contribute
Please contribute if you find our project interesting.
