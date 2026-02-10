# Authentication System Documentation

## Features
- User registration
- User login and logout
- Profile management

## Registration
Users can register using the /register endpoint.

## Login
Users log in at /login using their credentials.

## Profile
Authenticated users can view and update their email at /profile.

## Security
- CSRF tokens are used in all forms.
- Passwords are securely hashed using Django authentication.
