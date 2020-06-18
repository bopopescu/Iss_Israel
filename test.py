# Make the same request we did earlier, but with the coordinates of San Francisco instead.
import json
import re
from datetime import datetime
import pytz
import  db_connection
from flask import Flask, request, render_template, redirect
# parameters = {"lat": 37.78, "lon": -122.41}
# response = request.get("http://open-notify.org/Open-Notify-API/ISS-Pass-Times/", params=parameters)
# # Get the response data as a python object. Verify that it's a dictionary.
# data = response.json()
# print(type(data))
# print(data)
# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
import requests


def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val



# get international space station geo location
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/

def get_space_station_location():
    r = requests.get(url='http://api.open-notify.org/iss-now.json')
    space_station_location = (r.json())

    space_station_longitude = float(space_station_location['iss_position']['longitude'])
    print('space_station_longitude', space_station_longitude)
    space_station_latitude = float(space_station_location['iss_position']['latitude'])
    print('space_station_latitude', space_station_latitude)

    return (space_station_longitude, space_station_latitude)

# print(get_space_station_location())
def try1():
    # Set up the parameters we want to pass to the API.
    # This is the latitude and longitude of New York City.
    parameters = {"lat": 40.71, "lon": -74 , "n": 50}
    # Make a get request with the parameters.
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    next_pass = response['response'][0]['risetime']
    next_pass_datetime = datetime.fromtimestamp(next_pass, tz=pytz.utc)
    # Print the content of the response (the data the server returned)
    print(response.content)
    # This gets the same data as the command aboveresponse = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
    print(response.content)



def get_next_pass(name,lat, lon):
    iss_url = 'http://api.open-notify.org/iss-pass.json'
    location = {'lat': lat, 'lon': lon, "n": 50}
    response = requests.get(iss_url, params=location).json()
    print(response)
    # for res in response['response'][0]:
    #     for i in range(50):
    #         print(response['response'][i]["risetime"])
    #         # db_connection.mycursor.execute("")
    #     # print("risetime:", res["risetime"])
    #
    #     # if 'response' in response:
    #         next_pass = response['response'][0]['risetime']
    #         next_pass_datetime = datetime.fromtimestamp(next_pass, tz=pytz.utc)
    #         print('Next pass for {}, {} is: {}'.format(lat, lon, next_pass_datetime))
    #         print(next_pass_datetime)
    #
    #
    #         duration = str((response['response'][i]["duration"]))
    #         print(duration)
    #         risetime = str((response['response'][i]["risetime"]))
    #         json_column_name = response['response'][0]
    #
    #         sql = "INSERT INTO orbital_data_eilat (duration ,risetime) VALUES (%s ,%s)"
    #         db_connection.mycursor.execute(sql, (json.dumps(json_column_name),))
    #         # db_connection.mycursor.execute("INSERT INTO orbital_data_eilat (name) VALUES (%s)",(duration))
    print("response " ,response['response'])
    for i, item in enumerate(response['response']):
        duration = (item.get('duration', None))
        risetime = (item.get('risetime', None))
        next_pass_datetime = datetime.fromtimestamp(risetime, tz=pytz.utc)
        print(next_pass_datetime)
        sql = "INSERT INTO orbital_data_eilat4 (name, duration ,risetime) VALUES (%s ,%s ,%s)"
        db_connection.mycursor.execute(sql, (name,duration,next_pass_datetime),)
        # else:
        #     print('No ISS flyby can be determined for {}, {}'.format(lat, lon))
    db_connection.mycursor.execute("SELECT * FROM orbital_data_eilat4")
    myresult = db_connection.mycursor.fetchall()

    for x in myresult:
        print(x)



     # try
    avg=1
    print("proc")
    sql = "INSERT INTO orbital_data_tel_Aviv (name,avg) VALUES (%s,%s)"
    db_connection.mycursor.execute(sql,(name,avg),)
    db_connection.mycursor.execute("SELECT * FROM orbital_data_tel_Aviv")
    p ="""DELIMITER // CREATE PROCEDURE Hannah_avg_iss(IN city VARCHAR(255)) BEGIN UPDATE orbital_data_tel_Aviv SET avg=(SELECT COUNT(*)
     FROM orbital_data_eilat4
     WHERE name=city)/(SELECT Sum
     FROM orbital_data_eilat4
     WHERE name=city)
      WHERE name=city; END;DELIMITER ;"""

    proc2 = """DELIMITER // CREATE PROCEDURE Hannah_avg_iss(IN city VARCHAR(255), IN up INTEGER(10)) 
    BEGIN UPDATE orbital_data_tel_Aviv SET avg=up WHERE name=city; END //
    DELIMITER ;"""
    db_connection.mycursor.execute("DROP PROCEDURE IF EXISTS Hannah_avg_iss")
    
    
    # delllli

    delimiters = re.compile('DELIMITER *(\S*)', re.I)
    result = delimiters.split(p)

    # Insert default delimiter and separate delimiters and sql
    result.insert(0, ';')
    delimiter = result[0::2]
    section = result[1::2]

    # Split queries on delimiters and execute
    for i in range(len(delimiter)):
        queries = section[i].split(delimiter[i])
        for query in queries:
            if not query.strip():
                continue
            db_connection.mycursor.execute(query)
    
    # end
    # db_connection.mycursor.execute(proc2, multi=True)
    args=("Tel Aviv",)
    db_connection.mycursor.callproc("Hannah_avg_iss",args)

    db_connection.mycursor.execute("SELECT * FROM orbital_data_tel_Aviv")

    myresult = db_connection.mycursor.fetchall()

    for x in myresult:
        print(x)
    print("end proc")
# end
    # db_connection.mycursor.execute("SELECT  COUNT(*) FROM orbital_data_eilat4 ")
    # myresult = db_connection.mycursor.fetchall()
    # print(myresult)

def main():
    get_next_pass("Haifa",32.794044,34.989571)
    get_next_pass("Tel Aviv",32.109333, 34.855499)
    get_next_pass("Beer Sheva", 31.25181, 34.7913)
    get_next_pass("Eilat", 29.55805, 34.94821)

main()