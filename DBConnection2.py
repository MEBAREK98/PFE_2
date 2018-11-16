# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:12:36 2018

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
# =============================================================================
# #    extraction du nombre de publication WOS 
# =============================================================================

#def select_revueScientifique_scopus(datab,author_ID):
#    db = get_connection(datab)
#    p=[]
#    cursor = db.cursor()
#        # Execute the SQL command
#    cursor.execute("""select ISSN,Date from (((`publicationscientifique` \
#    inner join `chercheur` on `publicationscientifique`.`author_ID` = '%s') \
#    inner join `article_revue` on `article_revue`.`PublicationScientifique_ISSN`=`publicationscientifique`.`ISSN`) \
#    inner join `revuescientifique` on `article_revue`.`Revue_ID`=`revuescientifique`.`Revue_ID`) \
#    where `revuescientifique`.`Index_ID` = 1 """, (int(author_ID)))
#    rows = cursor.fetchall()
#    for row in rows:
#            p.append(row)
#    return p,len(p)
#print(select_revueScientifique_scopus("metricoscience",3))
            
            
# =============================================================================
# #pour le nombre d'auteur par base d'indexation bibliographique
# =============================================================================
def select_ID_chercheur(datab,name):
    db = get_connection(datab)

    cursor = db.cursor()
        # Execute the SQL command
    cursor.execute("""SELECT `ID` FROM `chercheur` WHERE `FirstName` = %s """, name)
    rows = cursor.fetchone()
    return rows[0]
#print(select_ID_chercheur("metricoscience","KAABECHE Abdelhamid"))
def select_ISSN_publicationscientifique(datab,author_id):
    db = get_connection(datab)

    cursor = db.cursor()
        # Execute the SQL command
    cursor.execute("""SELECT `ISSN` FROM `publicationscientifique` WHERE `author_ID`= '%s' """, (author_id,))
    rows = cursor.fetchall()
    return rows
#r=select_ISSN_publicationscientifique("metricoscience",3)

def select_article_revu_revu_ID(datab,issn):
    db = get_connection(datab)

    cursor = db.cursor()
        # Execute the SQL command
    cursor.execute("""SELECT `Revue_ID` FROM `article_revue` WHERE `PublicationScientifique_ISSN`= %s """, (issn,))
    rows = cursor.fetchall()
    return rows    
#print(select_article_revu_revu_ID("metricoscience",'0'))
def select_revue_scientifique_revue_id_WOS(datab, revue_ID):
    db = get_connection(datab)

    cursor = db.cursor()
        # Execute the SQL command
    cursor.execute("""SELECT  `Revue_name` FROM `revuescientifique` WHERE `Index_ID`="1" and `Revue_ID` = """+str(revue_ID))
    rows = cursor.fetchone()
    return rows    
#p=select_revue_scientifique_revue_id_WOS("metricoscience",900000)
#if p==None :print(p)
def select_revue_scientifique_revue_id_SCOPUS(datab, revue_ID):
    db = get_connection(datab)
    
    cursor = db.cursor()
        # Execute the SQL command
#    print("""SELECT  `Revue_name` FROM `revuescientifique` WHERE `Index_ID`="2" and `Revue_ID` = """+str(revue_ID))
    cursor.execute("""SELECT  `Revue_name` FROM `revuescientifique` WHERE `Index_ID`="2" and `Revue_ID` = """+str(revue_ID))
    rows = cursor.fetchone()
    return rows

def select_revue_scientifique_revue_id_IET(datab, revue_ID):
    db = get_connection(datab)

    cursor = db.cursor()
        # Execute the SQL command
    cursor.execute("""SELECT  `Revue_name` FROM `revuescientifique` WHERE `Index_ID`="3" and `Revue_ID` = """+str(revue_ID))
    rows = cursor.fetchone()
    return rows
