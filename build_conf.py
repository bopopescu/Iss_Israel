# import configparser
# config = configparser.ConfigParser()
# file = open("config.ini","w")
# config.add_section('City')
# config.set('City',"Name" ,'Haifa')
# config.set('City','lat' ,'19')
# config.set('City','lon','20')
# config.write(file)



import json

data = {}
data['cities'] = []
data['cities'].append({
    'name': 'Haifa',
    'lat': '32.794044',
    'lon': '34.989571'
})
data['cities'].append({
    'name': ' Tel Aviv',
    'lat': '32.109333',
    'lon': '34.855499'
})
data['cities'].append({
    'name': 'Beer Sheva',
    'lat': '31.25181',
    'lon': '34.7913'
})
data['cities'].append({
    'name': 'Eilat',
    'lat': '29.55805',
    'lon': '34.94821'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)