<<<<<<< HEAD
Simple In-Memory Django REST API

This is a basic REST API built using Django and Django REST Framework It allows to:

Create a user (`POST /users/`)
Retrieve a user by ID (`GET /users/<id>/`)

All data is stored in memory (`Dictionary`)  meaning it is not saved to a database and will reset when the server restarts



How it works

 it Store user data using Python dictionary (no database)
 it incremen `id` for each user used in django
JSON input/output
Basic validation and error handling


Technology used

Python
Django
Django REST Framework

=======

Here it is how this system works

1. Once run the project it direct open rest framework as entry point of this stytem

2. if you want to add user you need to add data in JSON format

3. if you write (`port/user/id/`) it open the user detail accordint to the id you privide on url
>>>>>>> 74f50a6 (Add explanation)
