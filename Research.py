# -*- coding: utf-8 -*-
"""
Created on Wed May 16 17:28:51 2018

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
def Research_step1(datab):
    db = get_connection(datab)

    cursor = db.cursor()
        # Execute the SQL command
    cursor.execute("""SELECT * FROM `article_revue` WHERE 1""")
    rows = cursor.fetchall()
    return rows


def Research_step2(datab,key_word):
    p=Research_step1("metricoscience4")
    article=[]
    for i in p:
        l=i[5].find(key_word.upper())
        if l!=-1:   article.append(i)
    return article


def Research_step3(datab,name_article,date,issn):
    p=Research_step1("metricoscience4")
    article=[]
    for i in p:
        l=i[5].find(name_article.upper())
        article.append(i)
        if l!=-1:   
            if i[4]==date or i[3]==issn: 
                article.clear()
#                print(article)
                article.append(i)
    return article
#print(Research_step2("metricoscience","learning"))
#print(Research_step3("metricoscience4","A NOVEL BROADBAND ANTENNA DESIGN FOR UHF RFID TAGS ON METALLIC SURFACE ENVIRONMENTS","2017","2299"))