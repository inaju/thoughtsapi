Record your random thoughts throughout the day by interacting with an api

# API Endpoints

# User Management with Djoser + Django Rest Framework
**Create Users(POST)** <br />
```curl -X POST http://127.0.0.1:8000/auth/users/ --data 'username=mitcheljohn&password=iloveapples' ```

**Get User Token(POST)** <br /> 
```curl -X POST http://127.0.0.1:8000/auth/jwt/create/ --data 'username=mitcheljohn&password=iloveapples'```

The refresh and access token would be returned, you append "Bearer <token>" to use it

**Check User Details(GET)** <br />
```curl -LX GET http://127.0.0.1:8000/auth/users/me/ -H 'Authorization:Bearer <token>' ```


# Create Thoughts
**Create Thoughts** <br />
``` curl -X POST http://127.0.0.1:8000/thoughts/ --data 'content="This is my first thought"&like=True&amount=4000' -H 'Authorization:Bearer <token>' ```


# Clone thoughtsapi
```git clone https://github.com/inaju/thoughtsapi```

``` pip install virtualenv ```

``` cd thoughtsapi ```

``` source env/sctipts/activate```- Linux

``` \env\Scripts\activate.bat ```- Windows

``` pip install -r requirements.txt ```

> The main packages we need are ```djangorestframework```, ```djangorestframework-simplejwt ```, ```djoser ```, ```Django```

``` python manage.py makemigrations ```

``` python manage.py migrate ```

``` python manage.py runserver ```




