
# Health++
Health++ is an application that helps user to manage their diet and calories consumption. It provides a common platform for dieticians and their patients, so that they can manage a proper diet. It also generates personalized infographics so that user properly understands his nutrition level.
# Run deployed website
Deployed at Heroku: [![img](https://i.ibb.co/2yZQT2S/deploy-32.png)](https://health-plus-plus.herokuapp.com/) (Click this image)

# Run locally
Clone the Repository using:

    git clone https://github.com/AnonySharma/Django-HealthPlusPlus.git

**Setting Up:**
<br>
Run this to use shortcuts

    chmod +x s.sh

Create virtual environment:

    virtualenv venv
    source venv/bin/activate

Then run migrate:

    ./s.sh mig
    or
    python3 manage.py migrate

Then create a super-user:

    ./s.sh sup
    or
    python3 manage.py createsuperuser

Then run the server:

    ./s.sh run
    or
    python3 manage.py runserver

# Contribute
Please contribute if you find our project interesting.
