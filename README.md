# react_django


* #### Dependencies
    1. create conda env
        ```base
            $ conda create -n envname python=3.9
        ```
    2. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    3. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```
* #### Make a new app
    ```
    bash
    $ python manage.py startapp appName
    ```
* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/
    ```
* #### Test the post function
    Assume that you already runserver in the local machine
    ```bash
    $ python test_post.py
    ```
