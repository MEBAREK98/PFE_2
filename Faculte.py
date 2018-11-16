# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:29:58 2018

@author: pc
"""

import pymysql

def get_connection(datab) :
    db = pymysql.connect(host='127.0.0.1',database=datab,user='root',password='')
    #cursor = db.cursor()
        #cursor.execute("SELECT VERSION()")
    #data = cursor.fetchone()
    #print("DB version: %s" % data)
    return db
def executeScripts(filename,datab):
    fd = open(filename, 'r')
    db=get_connection(datab)
    cursor = db.cursor()
    sqlScript = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlScript.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        try:
            cursor.execute(command)
            #db.commit()
        except db.OperationalError as msg:
            print ("Command skipped: ", msg)

def recupe_author(datab):
   db = get_connection(datab)

   cursor = db.cursor()
    #Prepare SQL query to INSERT a record into the database author table.
#    try:
        # Execute the SQL command
   cursor.execute(""" SELECT * FROM `table 1` INNER JOIN `table 2` ON `table 1`.`code` = `table 2`.`code_1`  """)
   rows = cursor.fetchall()
   return rows
p=recupe_author("chercheur_usthb")
print(p)


def insertion_fac(datab,fac):
    db = get_connection(datab)

    cursor = db.cursor()
    #Prepare SQL query to INSERT a record into the database author table.
    try:
        # Execute the SQL command
        cursor.execute(""" INSERT INTO `faculte`(`Nom`, `Universite_ID`) VALUES ('%s', %d) """ \
                %(fac, 1))
        #Commit your changes in the database
        db.commit()
    except:
#            Rollback in case there is any error
        db.rollback()

    #disconnect from server
    db.close() 

for i in p:
    insertion_fac("metricoscience",i[1])
    print(i[1])



def match(datab):
    
   db = get_connection(datab)
   lis_1=[]
   cursor = db.cursor()
    #Prepare SQL query to INSERT a record into the database author table.
#    try:
        # Execute the SQL command
   cursor.execute(""" SELECT * FROM `chercheur` WHERE 1  """)
   rows = cursor.fetchall()
   for i in rows:
#       print(i)
       lis_1.append(i[1])
   return lis_1

#match("metricoscience")
#print(match("metricoscience"))
#   def insertion_sans_redandence():
#       m=match("metricoscience")
#       for i in p:
#           if i in m:
#               pass
#           else:
        