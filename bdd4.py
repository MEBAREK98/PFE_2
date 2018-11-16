# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 12:16:55 2018

@author: pc
"""

import pymysql

def get_connection(datab) :
    print("mebarek")
    db = pymysql.connect("127.0.0.1","","",datab)
    #cursor = db.cursor()
        #cursor.execute("SELECT VERSION()")
    #data = cursor.fetchone()
    #print("DB version: %s" % data)
    print("mouloud")
    return db

def insert_info(datab,FIRST_NAME, E_MAIL, AFFILIATION, H_INDEX, NUM_CITATION, DOMAINE) :
    
    db = get_connection(datab)
    cursor = db.cursor()
    print("here's working")
    #Prepare SQL query to INSERT a record into the database.
    print("here too")
    sql ="INSERT INTO users(FIRST_NAME, \
                 E-MAIL, AFFILIATION, H-INDEX, NUM_CITATION, DOMAINE) \
                VALUES ('%s', '%s', '%s', '%d', '%d', '%s' )" %\
                (FIRST_NAME, E_MAIL, AFFILIATION, H_INDEX, NUM_CITATION, DOMAINE)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        #Commit your changes in the database
        db.commit()
    except:
            #Rollback in case there is any error
            db.rollback()

    #disconnect from server
    db.close()
#insert_info("amira3","mebarek mouloud","mouloud9858@gmail.com","informatique",0,0,"informatique_academique")