# Malecious IP Tracking for banking website

## Introduction
This project is a simple banking login application built with Flask. It tracks a user's IP address and location after three incorrect login attempts, storing this data in a database for review. This can be used as a security measure to log suspicious login activity.

## Features
- Login page with username and password fields.
- Tracks incorrect login attempts using Flask sessions.
- After three failed attempts, captures the user's IP address and location using the httpbin.org and ipinfo.io APIs.
- Stores IP address, location, and timestamp data in a MySQL/PostgreSQL database.
- Simple HTML structure with two pages: a homepage and a login page.

## Project Structure
/app
  ├── templates/
  │   ├── index.html        # Homepage template
  │   └── login.html        # Login page template
  ├── app.py                # Main Flask application file
  ├── config.py             # Database configuration file
  ├── requirements.txt      # Project dependencies
  └── README.md             # Project documentation (you are here)
