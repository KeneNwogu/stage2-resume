from flask import Flask, render_template, request, redirect
import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE IF NOT EXISTS contact ('name TEXT, email TEXT, message TEXT')
print ("Table created successfully")
conn.close()

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO contact (name,email, message) VALUES (?,?,?)",(name,email, message))
                con.commit()
                msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("thankyou.html",msg = msg)
            conn.close()