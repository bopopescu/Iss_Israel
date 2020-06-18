import mysql.connector

#mysql connention is private

#
# mycursor.execute("CREATE TABLE orbital_data_haifa (name VARCHAR(255))")
mycursor.execute("DROP TABLE IF EXISTS orbital_data_tel_Aviv")
mycursor.execute("CREATE TABLE orbital_data_tel_Aviv (name VARCHAR(255) ,avg INTEGER(10))")
# mycursor.execute("CREATE TABLE orbital_data_hannah (name VARCHAR(255),  duration INTEGER(10) ,risetime DATETIME )")
# mycursor.execute("CREATE TABLE city_stats_hannah1 (name VARCHAR(255),  avg INTEGER(10) )")

mycursor.execute("SHOW TABLES")
for db in mycursor:
    print(db)
mycursor.execute("SELECT  COUNT(*) FROM orbital_data_eilat4")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
mydb.commit()

# proc = "CREATE PROCEDURE hannah_avg_iss (IN name varchar(50)) BEGIN insert into city_stats_hannah (name,avg) values (name ,user_name,branch);END"
proc = "CREATE PROCEDURE hannah_avg_iss (IN name varchar(50)) BEGIN  insert into city_stats_hannah1 (name,avg) values (name ,SELECT  COUNT(*) FROM orbital_data_hannah);END"
proc2 ="CREATE PROCEDURE Hannah_avg_iss() BEGIN UPDATE orbital_data_tel_Aviv SET avg = (SELECT AVG(*) FROM orbital_data_eilat4 GROUP BY name) WHERE name = 'Tel Aviv'; END;"
mycursor.execute("DROP PROCEDURE IF EXISTS Hannah_avg_iss")
mycursor.execute(proc2 ,multi=True)
mycursor.execute("call Hannah_avg_iss()",multi=True)

mycursor.execute("SELECT  COUNT(*) FROM orbital_data_tel_Aviv")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# mycursor.execute("CREATE TABLE orbital_data_eilat (name VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for db in mycursor:
    print(db)
# print(mycursor.execute("SELECT * FROM orbital_data_hannah"))
# mycursor.execute("INSERT INTO orbital_data_tel_Aviv (name) VALUES (%s)",'Tel Aviv')
name='Tel Aviv'
avg=1
sql = "INSERT INTO orbital_data_tel_Aviv (name,avg) VALUES (%s,%s)"
# mycursor.execute(sql,(name,avg),)
# mycursor.execute("SELECT * FROM orbital_data_tel_Aviv")
# print(mycursor.execute("INSERT INTO json_col VALUES "+"hhhh"+""))

# sql = """INSERT INTO orbital_data_haifa (name) VALUES (%s) """
# val = ('John',)
# mycursor.execute(sql, val)
# mycursor.execute("SELECT * FROM orbital_data_haifa")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
mydb.commit()
