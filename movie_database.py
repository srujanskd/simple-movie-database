import sqlite3
from sqlite3 import Error 

def create_connection(db_file):
    conne = None
    try:
        conne = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conne

def create_table(sql):
    global conn
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def insert_table(sql):
    global conn
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def retrive_data(sql):
    global conn
    
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print()




conn = create_connection(r"movie.db")
sql = """create table if not exists Movie(Title TEXT, Actor TEXT, Actress TEXT, Year INT, Director TEXT)"""
create_table(sql)

movie_title = ["Shutter Island", "Interstellar", "Inception", "Silence Of The Lambs"]
actor_name = ["Leonardo DiCaprio", "Matthew McConaughey", "Leonardo DiCaprio", "Anthony Hopkins"]
actress_name = ["Emily Mortimer", "Anne Hathaway", "Elliot Page", "Jodie Foster"]
year = [2010, 2014, 2010, 1991]
director = ["Martin Scorsese", "Christopher Nolan", "Christopher Nolan", "Jonathan Demme"]
for i in range(4):
    sql = """INSERT INTO Movie VALUES("%s", "%s", "%s", %d, "%s")""" % (movie_title[i], actor_name[i], actress_name[i], year[i], director[i])
    # print(sql)
    insert_table(sql)
sql = "SELECT * FROM Movie"
retrive_data(sql)
sql = "SELECT Title FROM Movie WHERE Actor = 'Leonardo DiCaprio'"

retrive_data(sql)
conn.close()
