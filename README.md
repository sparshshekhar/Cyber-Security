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
-Python 3.10 or above
-Virtual environment setup tool (venv or virtualenv)
-Flask and dependencies listed in requirements.txt
