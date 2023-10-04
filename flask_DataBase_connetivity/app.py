from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure the database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'money'
app.config['MYSQL_DB'] = 'student'

# Create a MySQL object
mysql = MySQL(app)

# Define a route to display data from the database
@app.route('/')
def index():
    # Create a cursor object
    cur = mysql.connection.cursor()

    # Execute a query to retrieve data from the database
    cur.execute('SELECT * FROM stu_record')

    # Fetch all the rows from the query result
    data = cur.fetchall()

    # Close the cursor object
    cur.close()

    # Return the data as a string
    return str(data)

if __name__ == '__main__':
    app.run(debug=True)
