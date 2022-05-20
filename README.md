# NotifyPrototype

Basic Flask application that allows users to register for notifications and administrators to send messages to groups of users

### Prerequisites

Requirements for the software and other tools to build, test and push 
- Python 3 (I have been using 3.9.2)
- MySQL Server / MariaDB (I have been using MariaDB 10.4.24)

### Installing

Clone the repository, then create a python virtual environment in your desired subdirectory

    python -m venv [directory]

Then activate the virtual environment

    source [directory]/bin/activate

Install required packages

    pip install -r requirements.txt

Then activate the virtual environment with 

    source [directory]/bin/activate
    
Before running you will want to start a local MySQL server, the database name is
specified in __init__.py, flask_app by default but you can make it whatever you want

And finally run the application with  

    flask run

this will run the application on port 5000 on localhost, you can specify another port or address using 
    
    flask run -h [ip address] -p [port]
    
## Improvements

Features to be added include putting the administrative features behind a secure login, hosting mail server, better admin view with options to select certain user characteristics, sms alerts

Current features include user registration and email confirmation, sending emails messages to groups of users

## Deployment

Information on deploying Flask to production server
https://flask.palletsprojects.com/en/2.1.x/deploying/
