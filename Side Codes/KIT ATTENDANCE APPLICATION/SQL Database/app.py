from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__, static_folder='static')

import mysql.connector

app = Flask(__name__)

# Database connection details
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",  # Central server IP address
        user="root",  # MySQL username
        password="shaheersql",  # MySQL password
        database="KIT"  # Database name
    )

# Home route (form to submit attendance)
@app.route('/')
def home():
    return render_template('attendance_form.html')

# Submit form data
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        activity = request.form['activity']
        arrival_time = request.form['arrival_time']
        departure_time = request.form['departure_time']

        # Insert data into MySQL
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO attendance (name, course, activity, arrival_time, departure_time)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, course, activity, arrival_time, departure_time))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
