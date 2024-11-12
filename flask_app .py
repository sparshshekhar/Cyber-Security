from flask import Flask, request, redirect, render_template, session, url_for, flash
import requests
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import pytz  # For handling timezones

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Secret key for session management

# Database configuration
db_config = {
    'host': 'alooHacker.mysql.pythonanywhere-services.com',  # Replace with actual host
    'user': 'admin10',  # Replace with actual username
    'password': 'user1000',  # Replace with actual password
    'database': 'alooHacker$user_database'  # Replace with actual database name
}

# Initialize the database and create a table if it doesn't exist
def init_db():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    ip_address VARCHAR(255),
                    city VARCHAR(255),
                    region VARCHAR(255),
                    country VARCHAR(255),
                    timestamp DATETIME
                )
            ''')
            conn.commit()
    except Error as e:
        print(f"Error initializing database: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# Function to get location based on IP address using ipinfo.io
def get_location(ip_address):
    try:
        location_response = requests.get(f'https://ipinfo.io/{ip_address}/geo')
        if location_response.status_code == 200:
            location_data = location_response.json()
            return {
                "ip": ip_address,
                "city": location_data.get('city', 'N/A'),
                "region": location_data.get('region', 'N/A'),
                "country": location_data.get('country', 'N/A')
            }
    except Exception as e:
        print(f"Error fetching location data: {e}")
        return {"ip": ip_address, "city": "Unknown", "region": "Unknown", "country": "Unknown"}

# Save data to MySQL database with IST timestamp
def save_to_db(ip, city, region, country):
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            cursor = conn.cursor()
            # Convert timestamp to IST
            ist = pytz.timezone('Asia/Kolkata')
            timestamp = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute('''
                INSERT INTO user_data (ip_address, city, region, country, timestamp)
                VALUES (%s, %s, %s, %s, %s)
            ''', (ip, city, region, country, timestamp))
            conn.commit()
    except Error as e:
        print(f"Error saving to database: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# Route to render the login page
@app.route('/')
def index():
    return render_template('login.html')

# Route to handle login logic
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Dummy credentials (in practice, you'd query your database)
    valid_username = 'admin10'
    valid_password = 'user1000'

    if 'login_attempts' not in session:
        session['login_attempts'] = 0

    if username == valid_username and password == valid_password:
        session['login_attempts'] = 0  # Reset on successful login
        flash('Login successful!', 'success')
        return render_template('index.html')  # Redirect to index.html
    else:
        session['login_attempts'] += 1
        flash(f'Login failed! Attempt {session["login_attempts"]}/3', 'error')

        if session['login_attempts'] >= 3:
            # After 3 failed login attempts, track the user IP and redirect to "Authenticate" page
            user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
            location_info = get_location(user_ip)
            save_to_db(location_info['ip'], location_info['city'], location_info['region'], location_info['country'])
            session['login_attempts'] = 0  # Reset after 3 failed attempts
            return redirect(url_for('authenticate'))  # Redirect to authentication page

        return redirect(url_for('index'))  # Retry login after failed attempt

# Route to display home page (index.html) after successful login
@app.route('/home')
def home():
    return render_template('index.html')

# Route to render the "Authenticate your access" page after 3 failed attempts
@app.route('/authenticate')
def authenticate():
    return render_template('authenticate.html')

if __name__ == '__main__':
    init_db()  # Initialize database on app startup
    app.run(host='0.0.0.0', port=8080, debug=True)
