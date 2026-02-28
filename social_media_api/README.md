Ahhh got you now, Butterscotch 😎🔥

Here’s a **full copy-paste README.md** you can drop straight into your project root. Just save it as `README.md`:

---

````markdown
# Social Media API — Alx_DjangoLearnLab

## Project Overview
This is a Django-based Social Media API built from scratch.  
It allows users to register, login, and view their profile. Token-based authentication is used to secure endpoints.

## Features
- Custom User Model with:
  - bio
  - profile_picture
  - followers (Many-to-Many relationship)
- User registration endpoint (`/accounts/register/`)
- User login endpoint (`/accounts/login/`)
- Profile endpoint (`/accounts/profile/`) (requires token authentication)

## Installation
1. Clone the repo:

```bash
git clone <your-repo-url>
cd Alx_DjangoLearnLab
````

2. Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
python -m pip install django djangorestframework djangorestframework-authtoken
```

4. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the server:

```bash
python manage.py runserver
```

## API Endpoints

### Register User

* URL: `/accounts/register/`
* Method: POST
* Body (JSON):

```json
{
  "username": "example",
  "email": "example@example.com",
  "password": "12345678",
  "bio": "Hello world!"
}
```

* Response: Returns token

---

### Login User

* URL: `/accounts/login/`
* Method: POST
* Body (JSON):

```json
{
  "username": "example",
  "password": "12345678"
}
```

* Response: Returns token

---

### User Profile

* URL: `/accounts/profile/`
* Method: GET
* Header:

```
Authorization: Token <YOUR_TOKEN>
```

* Response: User profile info

```json
{
  "username": "example",
  "email": "example@example.com",
  "bio": "Hello world!",
  "profile_picture": null,
  "followers_count": 0,
  "following_count": 0
}
```

---

## Notes

* Make sure the server is running when testing endpoints
* Use the token in the `Authorization` header for protected routes
* The project uses a custom user model — migrations must be applied after setup

## Project Structure

```
Alx_DjangoLearnLab/
│
└── social_media_api/
    ├── manage.py
    ├── db.sqlite3
    ├── social_media_api/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    └── accounts/
        ├── __init__.py
        ├── models.py
        ├── views.py
        ├── serializers.py
        ├── urls.py
        └── migrations/
            └── __init__.py

