import os
from flask import Flask, render_template,redirect,url_for,request
import MySQLdb
from flask_migrate import Migrate
import requests

conn = MySQLdb.connect('127.0.0.1','root','','capstone')
cursor= conn.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    city = ['Miami', 'New York City','Los Angeles']
    if request.method == 'POST':
        cityview= request.form.post('city')
        # return redirect(url_for({{city}}))
    return render_template('index.html', city=city)


@app.route('/miami')
def miami():
        resultValue= cursor.execute("SELECT * FROM capstone.food_search WHERE location_address like '%Miami%' ")
        if resultValue > 0:
            data= cursor.fetchall()
            return render_template("miami.html", value=data)

@app.route('/NewYork')
def newyork():
        resultValue= cursor.execute("SELECT * FROM capstone.food_search WHERE location_address like '%New York City%' ")
        if resultValue > 0:
            data= cursor.fetchall()
            return render_template("newyork.html", value=data)

@app.route('/LosAngeles')
def losangeles():
        resultValue= cursor.execute("SELECT * FROM capstone.food_search WHERE location_address like '%Los Angeles%' ")
        if resultValue > 0:
            data= cursor.fetchall()
            return render_template("la.html", value=data)

if __name__ == '__main__':
    app.run(debug=True)
