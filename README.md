# Neighbourhood

### By Denzel Ouma

## Description

 This is an application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## User Stories
1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4.Find Contact Information for the health department and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.


## Behavior Driven Development

| Behavior  | Input |   Output |
| :------------- | :-------------: |   -------------: |
|   User athentication  |  Sign-up credentials   | Navigate to login page    |
|  User athentication    | Login credentials    |  Navigate to home page   |
|  Logout    | Logout    |  logged out   |
|  Post Neighbourhood    | Neighbourhood    |  Neighbourhood   |
|  Post Business    | Business Posted    |  Business   |

## Setup/Installation Requirements

 To start using this project use the following commands:

* git clone https://github.com/Denzel97/The-Neighbourhood.git
* cd The-Neighbourhood
* atom . OR code .

 To run this program

* run this command lines in your terminal:
* python manage.py runserver
* access the application on this localhost address http://127.0.0.1:8000

## Prerequisites

You need the following to work on the project:

- postgesql
- Python version 3.6
- Django 2.0+
- Pip
- virtualenv
- A text Editor

## Link to live Website

 [Neighbourhood](https://denzhood.herokuapp.com/)

## Technologies Used

* Django
* Html/css
* Bootstrap
* django-bootstrap4
* Heroku
* Python3.6

## Clone repository
* git clone https://github.com/Denzel97/The-Neighbourhood.git
* cd The-Neighbourhood
* virtualenv virtual
* source/virtual/bin/activate
* pip install django
* pip install -r requirements.txt(Install the dependencies)
* python3.6 manage.py migrate
* python manage.py runserver

## Known Bugs
 None at the moment

## License

 This project is licensed under the MIT License

 Copyright (c) 2018 Denzel Ouma