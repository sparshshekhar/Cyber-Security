# Malicious IP Tracking for banking website

## Introduction
This project is a simple banking login application built with Flask. It tracks a user's IP address and location after three incorrect login attempts, storing this data in a database for review. This can be used as a security measure to log suspicious login activity.

## Features
- Login page with username and password fields.
- Tracks incorrect login attempts using Flask sessions.
- After three failed attempts, captures the user's IP address and location using the httpbin.org and ipinfo.io APIs.
- Stores IP address, location, and timestamp data in a MySQL/PostgreSQL database.
- Simple HTML structure with two pages: a homepage and a login page.

## Requirements
- Python 3.10 or above
- Virtual environment setup tool (venv or virtualenv)
- Flask and dependencies listed in requirements.txt

## Frontend Documentation

### 1. login.html
The login page contains a form where users enter their username and password. This form submits to the backend (/login endpoint) to verify credentials. If the user enters the wrong credentials three times, their IP and location will be logged.

#### HTML Structure:
- Form Fields: 
- username: A text input for the username.
- password: A password input for the password.
- Button: 
- Login: Submits the form data.

### 2. index.html
The homepage displays a welcome message once a user has logged in successfully.


## Setup Instruction

1) Clone the Repository
   - git clone https://github.com/sparshshekhar/Cyber-Security
   - cd Cyber-Security
     
2) Set Up a Virtual Environment
   - python3 -m venv venv
   - source venv/bin/activate  # On Windows, use venv\Scripts\activate
     
4) Install Dependencies
   - pip install -r requirements.txt
     
5) Configure Database in config.py
   - DB_USERNAME = 'your_username'
   - DB_PASSWORD = 'your_password'
   - DB_HOST = 'your_username.mysql.pythonanywhere-services.com'
   - DB_NAME = 'your_username$database_name'
  
   - SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
   - SQLALCHEMY_TRACK_MODIFICATIONS = False

## Running the Application

1) Initialize the Database
   Run the following commands to create the database tables:
   - python
   Then in the Python shell:
   - from app import db
   - db.create_all()
   - exit()
   
2) Start the Application
   Run the Flask application with:
   - python app.py
   
3) Access the App
  - Open a browser and go to http://127.0.0.1:5000 to see the homepage.

## Outputs
1. *Frontend Overview*
    ![Frontend Overview](https://github.com/sparshshekhar/Cyber-Security/blob/main/screenshots/1.jpg)
2. *Failed Attempts*
    ![Failed Attempts](https://github.com/sparshshekhar/Cyber-Security/blob/main/screenshots/2.jpg)
3. *Tracked IP*
    ![Tracked IP](https://github.com/sparshshekhar/Cyber-Security/blob/main/screenshots/3.jpg)



## Deployment on PythonAnywhere

1) Upload Files to PythonAnywhere
   Log in to PythonAnywhere.
   Open a Bash console and clone your GitHub repository:
   - git clone https://github.com/sparshshekhar/Cyber-Security
   - cd Cyber-Security
  
2) Create a Virtual Environment on PythonAnywhere
   - mkvirtualenv myenv --python=/usr/bin/python3.10
   - workon myenv
   - pip install -r requirements.txt
3) Configure the Web App
   Go to the Web tab on PythonAnywhere and add a new web app.
   Choose Flask and Manual configuration with Python 3.10.
   Set the Source code to your app.py file.
   Under Virtualenv, specify the path to the virtual environment created in step 2.
   Configure the WSGI file to point to the Flask app as follows:
   - import sys
   - path = '/home/yourusername/Cyber-Security'
   - if path not in sys.path:
   - sys.path.append(path)
   - from app import app as application
     
4) Create Database Tables on PythonAnywhere
   Open a Python console on PythonAnywhere and run:
    - from app import db
    - db.create_all()
      
5) Reload the Web App
   Return to the Web tab and click Reload.


   Your application should now be accessible at https://yourusername.pythonanywhere.com.


## Conclusion
This project demonstrates the creation of a secure banking web interface with a simple, user-friendly design. The system integrates IP and location tracking functionality, triggered after multiple unsuccessful login attempts, which enhances security and provides insight into potential unauthorized access attempts. By using Flask for backend processing and HTML/CSS/JavaScript for frontend design, this project achieves an effective, lightweight, and aesthetically pleasing solution for a demo banking website.
The integration of tracking mechanisms into the authentication process reflects an understanding of key security concepts essential in modern web applications. This project serves as a foundation that can be expanded with further features, such as multi-factor authentication, transaction management, and real-time monitoring, to create a fully-functional, secure banking platform.


