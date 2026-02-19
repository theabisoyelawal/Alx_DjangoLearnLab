# Social Media API

This project is a simple Social Media API built using Django and Django REST Framework. It implements user registration, login, and profile management using token authentication.

---

## Setup Instructions

1. Install required packages:

pip install django djangorestframework djangorestframework-authtoken

2. Run migrations:

python manage.py makemigrations
python manage.py migrate

3. Start the development server:

python manage.py runserver

---

## API Endpoints

### Register User

URL: /register/  
Method: POST  

Example JSON body:

{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
}

Response: Returns user details and authentication token.

---

### Login User

URL: /login/  
Method: POST  

Example JSON body:

{
    "username": "testuser",
    "password": "password123"
}

Response: Returns user details and authentication token.

---

### User Profile

URL: /profile/  
Method: GET  

Headers required:

Authorization: Token <your_token_here>

Response: Returns logged-in user's profile information.

---

## Custom User Model

The custom user model extends Django’s AbstractUser and includes:

- bio (TextField)
- profile_picture (ImageField)
- followers (ManyToManyField referencing self, symmetrical=False)

---

## Authentication

This project uses Django REST Framework Token Authentication. A token is automatically created when a user registers or logs in.
