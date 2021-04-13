import os
from flask import Flask, render_template,redirect,url_for,request
import MySQLdb
from flask_migrate import Migrate
import requests
from flask_bootstrap import Bootstrap

conn = MySQLdb.connect('127.0.0.1','root','','capstone')
cursor= conn.cursor()

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET','POST'])
def index():
    city=['Miami','New York','Los Angeles']
    print(city[0])
    print(city[1])
    print(city[2])
    if request.method=='POST':
        city = request.form["city"]
        if city=="Miami":
            print('you selected miami')
            return redirect(url_for('miami'))
        elif city=="New York":
            return redirect(url_for('newyork'))
        elif city=="Los Angeles":
            return redirect(url_for('losangeles'))
    return render_template('index.html', city=city)

# @app.route('/cityview', methods=['POST','GET'])
# def cityview():
#     request.method=='POST'
#     if request.form.to_dict(["city"])=='Miami':
#         return render_template("miami.html", value=data)
#     elif request.form.to_dict(["city"])=="New York City":
#         return render_template("newyork.html", value=data)
#     elif request.form.to_dict(["city"])=="Los Angeles":
#         return render_template("la.html", value=data)
#     return 'no'



@app.route('/Miami', methods=['POST','GET'])
def miami():
        resultValue= cursor.execute("SELECT * FROM capstone.food_search WHERE location_address like '%Miami%' ")
        if resultValue > 0:
            data= cursor.fetchall()
            return render_template("miami.html", value=data)

@app.route('/NewYork', methods=['POST','GET'])
def newyork():
        resultValue= cursor.execute("SELECT * FROM capstone.food_search WHERE location_address like '%New York%' ")
        if resultValue > 0:
            data= cursor.fetchall()
            return render_template("newyork.html", value=data)

@app.route('/LosAngeles', methods=['POST','GET'])
def losangeles():
        resultValue= cursor.execute("SELECT * FROM capstone.food_search WHERE location_address like '%Los Angeles%' ")
        if resultValue > 0:
            data= cursor.fetchall()
            return render_template("la.html", value=data)

if __name__ == '__main__':
    app.run(debug=True)
