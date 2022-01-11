# The Hood
## Author
* [Shaggy](https://github.com/Dhyder)

## Description
This is a web application allows you to be in the loop about everything happening in your neighborhood. From meeting announcements to even alerts.

## Screenshots
![Ring](https://user-images.githubusercontent.com/86789832/148875055-b0faa6d0-b216-4a86-b0f8-046858bb577c.png)
![Ring](https://user-images.githubusercontent.com/86789832/148875085-42ebb474-8cc3-424a-9631-0977546a9808.png)
![Ring](https://user-images.githubusercontent.com/86789832/148875095-0fd9443e-f699-46a1-af2c-a57159c94da4.png)

## Live Link
You can view the site at: [Hood](https://nxtdoor.herokuapp.com/)

## User Story
- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.


## SetUp / Installation Requirements
### Prerequisites
* Django 2.2.24
* python3.8.12
* virtualenv
* pgAdmin4
* HTML5  
* CSS3
* Javascript 
* Font Awesome
* jQuery

### Cloning
* In your terminal:

        git clone https://github.com/Dhyder/The-Hood.git
        cd The-Hood

## Running the Application
* Creating the virtual environment

        virtualvenv virtual
        source virtual/bin/activate
 or in (windows)
 
        source virtual/Scripts/activate

* Installing Dependencies

        pip install -r requirements.txt
        
* Making Migrations

        python manage.py makemigrations neighborhood
        
* Migrate

        python manage.py migrate

* Running the application:

        python3.8 manage.py runserver
        

## Testing the Application
* To run the tests for the class files:

        python3.8 manage.py test

## Technologies Used
* Python3.8.12
* Django2.2.24

## Known Bugs
* No known bugs at the moment
## Author's Contact Information
* For any queries, you can reach out at [desastrecaliente@gmail.com]

[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Dhyder/Awwards/blob/master/LICENSE)

Copyright (c) 2021 **Shaggy**
