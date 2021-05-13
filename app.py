import os
from flask import Flask, render_template,redirect,url_for,request
import MySQLdb
from flask_migrate import Migrate
import requests
from flask_bootstrap import Bootstrap




conn = MySQLdb.connect("127.0.0.1","dhruv","password","capstone")

cursor = conn.cursor()  #Dhruvs Database Connection :: Current & forcast weather
cursor1 = conn.cursor() #Nicks Database connection :: Food search
cursor2 = conn.cursor() #Mikes Databse Connection :: Hotels
cursor3 = conn.cursor() #Jons Database Conecction :: Historical weather


app = Flask(__name__)
Bootstrap(app)

#MAIN HOME PAGE
@app.route('/',methods=['GET','POST'])
@app.route('/home')
def home():
        city = ['Miami','New York','Los Angeles']
        if request.method == 'POST':
            city = request.form["city"]
            if city=="Miami":
                return redirect(url_for("miami"))
            elif city=="New York":
                return redirect(url_for("newyork"))
            elif city=="Los Angeles":
                return redirect(url_for("losangeles"))
        return render_template('index.html',city=city)


@app.route('/Miami', methods=['POST','GET'])
def miami():
        results= cursor.execute("SELECT * FROM capstone.currentWeather WHERE name LIKE '%Miami%'")
        results1 = cursor1.execute("SELECT * FROM capstone.food_search WHERE location_address LIKE '%Miami%' LIMIT 10")
        result2 = cursor2.execute("SELECT * FROM capstone.hotelSearch WHERE city LIKE '%Miami%' LIMIT 10")
        result3 = cursor3.execute("SELECT * FROM capstone.historicalWeather WHERE city_name LIKE '%Miami%'")
        if ((results > 0) and (results1 > 0) and (result2 > 0) and (result3 > 0)):
            data=cursor.fetchall()
            data1=cursor1.fetchall()
            data2=cursor2.fetchall()
            data3=cursor3.fetchall()
            return render_template("miami.html",value=data,value1=data1,value2=data2,value3=data3)

@app.route('/NewYork', methods=['POST','GET'])
def newyork():
    results= cursor.execute("SELECT * FROM capstone.currentWeather WHERE name LIKE '%New York%'")
    results1 = cursor1.execute("SELECT * FROM capstone.food_search WHERE location_address LIKE '%New York%' LIMIT 10")
    result2 = cursor2.execute("SELECT * FROM capstone.hotelSearch WHERE city LIKE '%New York%' LIMIT 10")
    result3 = cursor3.execute("SELECT * FROM capstone.historicalWeather WHERE city_name LIKE '%New York City%'")
    if ((results > 0) and (results1 > 0) and (result2 > 0) and (result3 > 0)):
        data=cursor.fetchall()
        data1=cursor1.fetchall()
        data2=cursor2.fetchall()
        data3=cursor3.fetchall()
        return render_template("newyork.html",value=data,value1=data1,value2=data2,value3=data3)


@app.route('/LosAngeles', methods=['POST','GET'])
def losangeles():
     results= cursor.execute("SELECT * FROM capstone.currentWeather WHERE name LIKE '%Los Angeles%'")
     results1 = cursor1.execute("SELECT * FROM capstone.food_search WHERE location_address LIKE '%Los Angeles%' LIMIT 10")
     result2 = cursor2.execute("SELECT * FROM capstone.hotelSearch WHERE city LIKE '%Los Angeles%' LIMIT 10")
     result3 = cursor3.execute("SELECT * FROM capstone.historicalWeather WHERE city_name LIKE '%Los Angeles%'")

     if ((results > 0) and (results1 > 0) and (result2 > 0) and (result3 > 0)):
         data=cursor.fetchall()
         data1=cursor1.fetchall()
         data2=cursor2.fetchall()
         data3=cursor3.fetchall()
         return render_template("losangeles.html",value=data,value1=data1,value2=data2,value3=data3)




if __name__ == "__main__":
        app.run(debug=True)
