from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
  
app = Flask(__name__)
  
  
app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user'
  
mysql = MySQL(app)
  
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('user.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)

@app.route('/user')
def user():
    if 'email' in session:
        return render_template("user.html")
    else:
        return redirect(url_for('login'))

@app.route('/stunting')
def stunting():
    if 'email' in session:
        return render_template("stunting.html")
    else:
        return redirect(url_for('login'))
    
@app.route('/kasus_ptm')
def kasus_ptm():
    if 'email' in session:
        return render_template("Kasus_ptm.html")
    else:
        return redirect(url_for('login'))
    
@app.route('/kasus_pm')
def kasus_pm():
    if 'email' in session:
        return render_template("Kasus_pm.html")
    else:
        return redirect(url_for('login'))

@app.route('/kunjungan')
def kunjungan():
    if 'email' in session:
        return render_template("Kunjungan_totalkunjungan.html")
    else:
        return redirect(url_for('login'))

@app.route('/kunjungan_pm')
def kunjungan_pm():
    if 'email' in session:
        return render_template("Kunjungan_pm.html")
    else:
        return redirect(url_for('login'))
    
@app.route('/kunjungan_ptm')
def kunjungan_ptm():
    if 'email' in session:
        return render_template("Kunjungan_ptm.html")
    else:
        return redirect(url_for('login'))
    
@app.route('/kunjungan_puskesmas')
def kunjungan_puskesmas():
    if 'email' in session:
        return render_template("Kunjungan_puskesmas.html")
    else:
        return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))
  

if __name__ == "__main__":
    app.run(debug=True, port=8001)
