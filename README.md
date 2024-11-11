# Malecious IP Tracking for banking website

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

## Setup Instruction

1) Clone the Repository
   - git clone https://github.com/yourusername/Banking-Website-with-IP-Tracking.git
   - cd Banking-Website-with-IP-Tracking
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



## Deployment on PythonAnywhere

1) Upload Files to PythonAnywhere
   Log in to PythonAnywhere.
   Open a Bash console and clone your GitHub repository:
   - git clone https://github.com/yourusername/banking-website-ip-tracking.git
   - cd banking-website-ip-tracking
  
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
   - path = '/home/yourusername/banking-website-ip-tracking'
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

