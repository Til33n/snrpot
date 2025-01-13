import sqlite3
import numpy as np

#conn = sqlite3.connect("database_1.db")
#creates a cursor
#c = conn.cursor()

#donn = sqlite3.connect("database_2.db")
#d = donn.cursor()

#eonn = sqlite3.connect("database_3.db")
#e = eonn.cursor()


#creates a table                             # AFTER CREATION OF DATABASE, WE COMMENT THIS PROCESS
#c.execute("""CREATE TABLE database_1
#(
#    username text,
#    password text,
#    mail text,
#    highest_score INTEGER,
#    played_matches INTEGER  
#
#)""")

#creates a table                             # AFTER CREATION OF DATABASE, WE COMMENT THIS PROCESS
#d.execute("""CREATE TABLE database_2
#(
#    match_id text,
#    username text,
#    time_played INTEGER,
#    highest_score INTEGER,
#    current_time INTEGER  
#
#)""")

#creates a table                             # AFTER CREATION OF DATABASE, WE COMMENT THIS PROCESS
#e.execute("""CREATE TABLE database_3
#(
#    username text,
#    score INTEGER
#
#)""")


#   DATATYPES
#NULL - it doesnt exit
#INTEGER - whole nubmer
#REAL - decimel
#TEXT - text/string
#BLOB - image, mp3,...



# RANDOM DATA FOR TESTING FUNCTIONS
multiple_data_row_1 = [   
    ('tilen','tomos','','33',''),   # ?,?,?    TUPLE PLACEHOLDER WITH ?      
      ]
multiple_data_row_11 = [   
    ('janez','tomos1','','20',''),   # ?,?,?    TUPLE PLACEHOLDER WITH ?      
      ]

multiple_data_row_111 = [   
    ('mojca','1234','13','10','14'),   # ?,?,?    TUPLE PLACEHOLDER WITH ?      
      ]

multiple_data_row_1111 = [   
    ('milfan','1234','13','40','14'),   # ?,?,?    TUPLE PLACEHOLDER WITH ?      
      ]


multiple_data_row_3 = [   
    ('11','12'),   # ?,?,?    TUPLE PLACEHOLDER WITH ?      
      ]


multiple_data = [   
    ('11','12','13','14'),   # ?,?,?    TUPLE PLACEHOLDER WITH ?
    ('21','22','23','24'),   # ?,?,?
    ('31','32','33','34'),
    ('41','42','43','44'),   # ?,?,?    TUPLE PLACEHOLDER WITH ?
    ('51','52','53','54'),   # ?,?,?
    ('61','62','63','64'),   # ?,?,?
      
      ]


#c.execute ( "INSERT INTO random_data VALUES ('somebodyfells@gmail.com','forlife2004@gmail.com','current_date','blob')")

#c.executemany( "INSERT INTO random_data VALUES (?,?,?,?)", multiple_data )

# Query the Database

#c.execute("SELECT rowid, * FROM random_data")
#c.execute("SELECT rowid, * FROM random_data")
#c.execute("SELECT rowid, * FROM random_data WHERE time_of_post LIKE 'cu%' ")
#c.execute("SELECT rowid, * FROM random_data WHERE time_of_post = '33' ")


#print(c.fetchone()  )                                   #its a tuple, 0 means first item of first row 
#print(c.fetchmany(2) )                                     #2 is number of fetched rows 
#print(c.fetchall())                                       #returns as a python list

#items = c.fetchall()
#print("Email_1 " +  "\t\t Email_2" )
#print("--------  " +  "\t\t--------")
#for item in items:
#    print(item[0] + " " + item [1] + "\t" + item[2] + " " + item[3]) 



#c.execute("""UPDATE random_data SET time_of_post = "changed" WHERE rowid = 5""")
#c.execute("DELETE from random_data WHERE rowid = 4")
#c.execute("SELECT rowid, * FROM random_data WHERE time_of_post LIKE '3%' AND rowid rowid = 3 ")
#c.execute("SELECT rowid, * FROM random_data WHERE time_of_post LIKE '3%' OR rowid rowid = 3 ")
#c.execute("DROP TABLE random_data")  #deletes entire table


#show all data in datatable
def show_all(database_id):  
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM " + str(database_id))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()    


#adds new record to table
#def add_one(source_email,destination_email,time_of_post,blob):                                 
def add_one_1(database_id, username, password, email, highest_score, played_matches):                                 
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.execute("INSERT INTO "+str(database_id)+" VALUES (?,?,?,?,?)", ( 'username','password','email','highest_score','played_matches'))
    conn.commit()
    conn.close()


def add_one_2(database_id, match_id, username, total_time_played, score, current_time):                                
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.execute("INSERT INTO "+str(database_id)+" VALUES (?,?,?,?,?)", ( 'match_id','username','total_time_played','score','current_time'))
    conn.commit()
    conn.close()


def add_one_3(database_id, username, score):                                 
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.execute("INSERT INTO "+str(database_id)+" VALUES (?,?)", ( 'username','score'))
    conn.commit()
    conn.close()


#adds multiple data(rows) at a time for database_1 and database_2
def add_many(database_id, list):
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.executemany("INSERT INTO "+str(database_id)+" VALUES (?,?,?,?,?)", (list))
    conn.commit()
    conn.close()


#adds multiple data(rows) at a time for database_1 and database_2
def add_many_3(database_id, list):
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.executemany("INSERT INTO "+str(database_id)+" VALUES (?,?)", (list))
    conn.commit()
    conn.close()


#deletes a single given row of data
def delete_one(database_id, id):
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.execute("DELETE from "+str(database_id)+" WHERE rowid = (?)", id)
    conn.commit()
    conn.close()


#look up where is item
def data_lookup(database_id, data):
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.execute("SELECT rowid,  * from "+str(database_id)+" WHERE username = (?)", (data,))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()
    return items[0]


def username_lookup(database_id, data):
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.execute("SELECT rowid,  * from "+str(database_id)+" WHERE username = (?)", (data,))
    output = c.fetchall()
    if data in str(output):
        return 1  
    else:
        return 0


def specific_data_lookup(database_id,  colom_search, colom_output , data):          #database select, which colom to search, which colom to return, searched data 
    output = []
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.execute("SELECT rowid,  * from "+str(database_id)+" WHERE "+str(colom_search)+" = (?)", (data,))
    #items = c.fetchall()
    output = [output[colom_output] for output in c.fetchall()]
    if data in str(output):
        conn.commit()
        conn.close()
        return output[0]
    conn.commit()
    conn.close()    
    return output[0]


def get_score_stats(database_id):
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.execute("SELECT username FROM "+str(database_id)) 
    players = c.fetchall()
    donn = sqlite3.connect(database_id+".db")
    d = donn.cursor()
    d.execute("SELECT highest_score FROM " + str(database_id)) 
    scores = d.fetchall()
  
    players = [i for sub in players for i in sub]
    scores  = [i for sub in scores  for i in sub]
    output = np.empty(shape=(len(players),2), dtype=object)   
     
    for y in range(0,2):
        for x in range(0,len(players),1):
            if(y == 0):
                output[x,y] = players[x]
            if(y==1):
                output[x,y] = scores[x]
                
    conn.commit()
    conn.close()    
    return output


def delete_all(database_id):
    conn = sqlite3.connect(database_id+".db") 
    c = conn.cursor()
    c.execute("DELETE from " +str(database_id))
    conn.commit()
    conn.close()


def get_last(database_id):
    conn = sqlite3.connect(database_id + ".db") 
    c = conn.cursor()
    c.execute("SELECT * FROM "+str(database_id)+" ORDER BY rowid DESC LIMIT 1;")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


def get_code(database_id):
    conn = sqlite3.connect(database_id + ".db") 
    c = conn.cursor()
    c.execute("SELECT * FROM "+str(database_id)+" ORDER BY rowid DESC LIMIT 1;")    
    code=c.fetchone()[1]
    return code



def delete_last_input(database_id):
    conn = sqlite3.connect(database_id + ".db") 
    c = conn.cursor()
    c.execute("DELETE FROM "+str(database_id)+" WHERE rowid = (SELECT MAX(rowid) FROM "+str(database_id)+");")
    conn.commit()
    conn.close()



def get_recepients_email(database_id):
    conn = sqlite3.connect(database_id + ".db") 
    c = conn.cursor()
    c.execute("SELECT * FROM "+str(database_id)+" ORDER BY rowid DESC LIMIT 1;")    
    recepients_email=c.fetchone()[2]
    return recepients_email



def get_file(database_id):
    conn = sqlite3.connect(database_id + ".db") 
    c = conn.cursor()
    c.execute("SELECT * FROM "+str(database_id)+" ORDER BY rowid DESC LIMIT 1;")    
    file=c.fetchone()[4]
    return file


def get_last_row_returned(database_id):
    conn = sqlite3.connect(database_id + ".db") 
    c = conn.cursor()
    c.execute("SELECT * FROM "+str(database_id)+" WHERE rowid = (SELECT MAX(rowid) FROM "+str(database_id)+");")
    zero = c.fetchone()[0]
    c.execute("SELECT * FROM "+str(database_id)+" WHERE rowid = (SELECT MAX(rowid) FROM "+str(database_id)+");")
    one =  c.fetchone()[1]
    c.execute("SELECT * FROM "+str(database_id)+" WHERE rowid = (SELECT MAX(rowid) FROM "+str(database_id)+");")
    two =  c.fetchone()[2]
    c.execute("SELECT * FROM "+str(database_id)+" WHERE rowid = (SELECT MAX(rowid) FROM "+str(database_id)+");")
    tree=  c.fetchone()[3]
    c.execute("SELECT * FROM "+str(database_id)+" WHERE rowid = (SELECT MAX(rowid) FROM "+str(database_id)+");")
    four = c.fetchone()[4]
    conn.commit()
    conn.close()

    return zero, one, two, tree, four


def get_last_item_returned(database_id):
    conn = sqlite3.connect(database_id + ".db") 
    c = conn.cursor()
    c.execute("SELECT * FROM "+str(database_id)+" WHERE rowid = (SELECT MAX(rowid) FROM "+str(database_id)+");")
    item = c.fetchone()[0]
    conn.commit()
    conn.close()

    return item


#def add_one_last(file_path):
#    conn = sqlite3.connect("data.db") 
#    c = conn.cursor()
#    c.execute("INSERT INTO data VALUES (?,?,?,?,?)", (list))
#    c.fetchone()[4] = file_path
#    conn.commit()
#    conn.close()

# Commit comand
#conn.commit()

# Close connection
#conn.close()

#add_many("database_1", multiple_data_row_1111)
#add_many("database_2", multiple_data_row_2)
#add_many_3("database_3", multiple_data_row_3)
#delete_all("database_1")
#delete_last_input("database_3")
#delete_last_input("database_1")
#show_all("database_1")
#show_all("database_2")
#show_all("database_3")

#x = specific_data_lookup("database_1","username",1, "tilen")
#y = specific_data_lookup("database_1","username",2, "tilen")
#z = specific_data_lookup("database_1","username",2, "janez")

#print(username_lookup("database_1","tilen2"))
#print(y)
#print(z)


#x = get_score_stats("database_1")
#print(x)
