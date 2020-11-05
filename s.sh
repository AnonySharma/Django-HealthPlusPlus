#!/bin/bash

if [[ $# -ne 1 ]]
then
    echo "You missed the arguement part, try [run,make,mig,shl]"
else
    if [[ $1 = "run" ]] 
    then
        printf "\033[0;36m\033[1mRan command: \'python3 manage.py runserver 1803\'\033[0m\n"
        python3 manage.py runserver 1803
    elif [[ $1 = "shl" ]] 
    then
        printf "\033[0;36m\033[1mRan command: \'python3 manage.py shell\'\033[0m\n"
        python3 manage.py shell
    elif [[ $1 = "make" ]] 
    then
        printf "\033[0;36m\033[1mRan command: \'python3 manage.py makemigrations\'\033[0m\n"
        python3 manage.py makemigrations
    elif [[ $1 = "mig" ]] 
    then
        printf "\033[0;36m\033[1mRan command: \'python3 manage.py migrate\'\033[0m\n"
        python3 manage.py migrate
    else
        echo "Illegal arguments, try [run,make,mig,shl]"
    fi
fi
