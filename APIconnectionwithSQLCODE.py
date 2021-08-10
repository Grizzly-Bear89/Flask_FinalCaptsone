import requests, json, googlemaps
import mysql.connector

cnx =mysql.connector.connect(host="localhost",  # your host
                     user="root",       # username
                     password="",     # password
                     database="capstone")   # name of the database
cur = cnx.cursor()


api_key = 'AIzaSyDvGRRQTHsY_NCabKqX48wBTgpp2M3REnI'

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

query = input('Search Query: ')

r=requests.get(url + 'query=' + query + '&fields=name,formatted_address,id' +'&key=' + api_key)

x=r.json()



y = x['results']

for i in range(len(y)):
    print(y[i]['place_id'])  ##Test to verify output
    print(y[i]['name'])
    print(y[i]['formatted_address'])

    placeid=y[i]['place_id']  ##input statements to DB
    location=y[i]['name']
    address=y[i]['formatted_address']

    sql = "INSERT INTO food_search (place_id ,locationname, location_address) VALUES (%s, %s, %s)"
    val = (placeid, location, address)
    cur.execute(sql, val)

    cnx.commit()
    print("Data Inserted!")



cur.close()
cnx.close()
