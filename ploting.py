from IPython.display import display
import pandas as pd
import pymysql
import numpy as np
import matplotlib

import IPython
import codecs
matplotlib.use('agg')
#matplotlib.use('QT4Agg')
from matplotlib import pyplot as plt




def get_connection(datab):
    db = pymysql.connect(host='127.0.0.1',database=datab,user='root',password='')
    return db

def plotpub(db,img,query,x,y, chaine):
    
    engine= get_connection(db)
    df = pd.read_sql_query(query,engine)
    fig, ax = plt.subplots()
    plt.title(chaine)
    mortalityage = df.sort_values("publicationNumb", ascending = False)
    display(mortalityage.plot(kind='barh',x=x, y=y, ax= ax, legend = False, figsize=(25, 4)))
    #, figsize=(20, 1)
    plt.savefig(img)

def plotArticle(db,img,query,x,y, chaine):
    engine= get_connection(db)
    df = pd.read_sql_query(query,engine)
    fig, ax = plt.subplots()
    mortalityage = df.sort_values("article", ascending = False)
    plt.title(chaine)
    display(mortalityage.groupby('DB').plot(kind='barh',x=x, y=y, ax= ax, legend = True, figsize=(25, 4)))
    plt.savefig(img)


                                                                                                                                                                                                                                                                     #revuescientifique.`Index_ID`=`indexation`.`ID_index` AND indexation.`DB`="wos") GROUP by

#
#plotpub("metricoscience4","facPub.png",'SELECT COUNT( `publicationscientifique`.`ISSN`) AS `publicationNumb`, `faculte`.`Nom` FROM `faculte` JOIN (`publicationscientifique`, `labo`, `enseignantchercheur`, `departement`) ON (`publicationscientifique`.`author_ID` = `enseignantchercheur`.`Author_ID` AND `enseignantchercheur`.`labo_id`=`labo`.`id`AND `labo`.`dep_id`= `departement`.`ID` AND `departement`.`Faculte_ID`=`faculte`.`ID`) GROUP by `faculte`.`Nom`',"Nom","publicationNumb", "nombre de publication par laboratoire")
##p = Rectangle((0, 0), 1, 1, fc="r")
##legend([p], ["Red Rectangle"])
#p1 = matplotlib.pyplot.plot([1,2,3])
#print(p1)
#print("je suis LAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
#p2, = matplotlib.pyplot.plot([3,2,1])
#p3, = matplotlib.pyplot.plot([2,3,1])
#matplotlib.pyplot.plot.legend([p2, p1], ["line 2", "line 1"])


#plotpub("metricoscience4","depPub.png",'SELECT COUNT( `publicationscientifique`.`ISSN`) AS `publicationNumb`, `departement`.`name` FROM `departement` JOIN (`publicationscientifique`, `labo`, `enseignantchercheur`) ON (`publicationscientifique`.`author_ID` = `enseignantchercheur`.`Author_ID` AND `enseignantchercheur`.`labo_id`=`labo`.`id`AND `labo`.`dep_id`= `departement`.`ID`) GROUP by `departement`.`name`',"name","publicationNumb", "nombre de publication par departement")
#plotpub("metricoscience4","laboPub.png",'SELECT COUNT( `publicationscientifique`.`ISSN`) AS `publicationNumb`, `labo`.`name` FROM `labo` JOIN (`publicationscientifique`, `enseignantchercheur`) ON (`publicationscientifique`.`author_ID` = `enseignantchercheur`.`Author_ID` AND `enseignantchercheur`.`labo_id`=`labo`.`id`) GROUP by `labo`.`name`',"name","publicationNumb")


#plotpub("metricoscience4","laboPub.png",'SELECT COUNT( article_revue.`publication_scientifique_id`) AS article, labo.`name` , article_revue.`Date`, indexation.`DB`FROM labo JOIN (article_revue, enseignantchercheur,`publicationscientifique`, revuescientifique,`indexation`) ON (publicationscientifique.`author_ID` = enseignantchercheur.`Author_ID` AND enseignantchercheur.`labo_id`=`labo`.`id` AND publicationscientifique.`PublicationScientifique_ID`=`article_revue`.`publication_scientifique_id` and revuescientifique.`Revue_ID`=`article_revue`.`Revue_ID`AND revuescientifique.`Index_ID`=`indexation`.`ID_index` AND indexation.`DB`="web of science") GROUP by labo.`name',"name","publicationNumb")

#plotArticle("metricoscience4","laboArt.png",'SELECT COUNT( `article_revue`.`PublicationScientifique_ISSN`) AS `article`, `labo`.`name` , `article_revue`.`Date`FROM `labo` JOIN (`article_revue`, `enseignantchercheur`,`publicationscientifique`) ON (`publicationscientifique`.`author_ID` = `enseignantchercheur`.`Author_ID` AND `enseignantchercheur`.`labo_id`=`labo`.`id` AND `publicationscientifique`.`ISSN`=`article_revue`.`PublicationScientifique_ISSN`) GROUP by `article_revue`.`Date` ',"name","article")
#
#plotArticle("metricoscience4","laboind.png",'SELECT COUNT( `article_revue`.`PublicationScientifique_ISSN`) AS `article`, `labo`.`name` , `article_revue`.`Date`, `indexation`.`DB`FROM `labo` JOIN (`article_revue`, `enseignantchercheur`,`publicationscientifique`, `revuescientifique`,`indexation`) ON (`publicationscientifique`.`author_ID` = `enseignantchercheur`.`Author_ID` AND `enseignantchercheur`.`labo_id`=`labo`.`id` AND `publicationscientifique`.`ISSN`=`article_revue`.`PublicationScientifique_ISSN` and `revuescientifique`.`Revue_ID`=`article_revue`.`Revue_ID`AND `revuescientifique`.`Index_ID`=`indexation`.`ID_index`) GROUP by  `labo`.`name` ',"name","article")


#plotting for labo number of articles published per index
#SELECT COUNT( `article_revue`.`publication_scientifique_id`) AS `article`, `labo`.`name` , `article_revue`.`Date`, `indexation`.`DB`FROM `labo` JOIN (`article_revue`, `enseignantchercheur`,`publicationscientifique`, `revuescientifique`,`indexation`) ON (`publicationscientifique`.`author_ID` = `enseignantchercheur`.`Author_ID` AND `enseignantchercheur`.`labo_id`=`labo`.`id` AND `publicationscientifique`.`PublicationScientifique_ID`=`article_revue`.`publication_scientifique_id` and `revuescientifique`.`Revue_ID`=`article_revue`.`Revue_ID`AND `revuescientifique`.`Index_ID`=`indexation`.`ID_index`) GROUP by  `labo`.`name`, `indexation`.`DB`

#plotting for dep numb of art pub per indx
#SELECT COUNT( `article_revue`.`publication_scientifique_id`) AS `article`, `departement`.`name` , `article_revue`.`Date`, `indexation`.`DB`FROM `departement` JOIN (`article_revue`, `enseignantchercheur`,`publicationscientifique`, `revuescientifique`,`indexation`,`labo`) ON (`publicationscientifique`.`author_ID` = `enseignantchercheur`.`Author_ID` AND `enseignantchercheur`.`labo_id`=`labo`.`id` AND `publicationscientifique`.`PublicationScientifique_ID`=`article_revue`.`publication_scientifique_id` and `revuescientifique`.`Revue_ID`=`article_revue`.`Revue_ID`AND `revuescientifique`.`Index_ID`=`indexation`.`ID_index` and `labo`.`dep_id`=`departement`.`ID`) GROUP by `departement`.`name`, `indexation`.`DB` 

#fac
#SELECT COUNT( `article_revue`.`publication_scientifique_id`) AS `article`, `faculte`.`Nom` , `article_revue`.`Date`, `indexation`.`DB`FROM `faculte` JOIN (`article_revue`, `enseignantchercheur`,`publicationscientifique`, `revuescientifique`,`indexation`,`labo`,`departement`) ON (`publicationscientifique`.`author_ID` = `enseignantchercheur`.`Author_ID` AND `enseignantchercheur`.`labo_id`=`labo`.`id` AND `publicationscientifique`.`PublicationScientifique_ID`=`article_revue`.`publication_scientifique_id` and `revuescientifique`.`Revue_ID`=`article_revue`.`Revue_ID`AND `revuescientifique`.`Index_ID`=`indexation`.`ID_index` and `labo`.`dep_id`=`departement`.`ID` and `departement`.`Faculte_ID`=`faculte`.`ID`) GROUP by `departement`.`name`, `indexation`.`DB`
    
#plotArticle("metricoscience4","test.PNG","SELECT COUNT( `article_revue`.`publication_scientifique_id`) AS `article`, `faculte`.`Nom` , `article_revue`.`Date`, `indexation`.`DB`FROM `faculte` JOIN (`article_revue`, `enseignantchercheur`, `publicationscientifique`, `revuescientifique`, `indexation`, `labo`, `departement`) ON (`publicationscientifique`.`author_ID` = `enseignantchercheur`.`Author_ID` AND `enseignantchercheur`.`labo_id`=`labo`.`id` AND `publicationscientifique.`PublicationScientifique_ID`=`article_revue`.`publication_scientifique_id` and revuescientifique.`Revue_ID`=`article_revue`.`Revue_ID`AND revuescientifique.`Index_ID`=`indexation`.`ID_index` and `labo`.`dep_id`=`departement`.`ID` and `departement`.`Faculte_ID`=`faculte`.`ID`AND `indexation`.`DB`= \"web of science\" ) GROUP by `faulte`.`Nom`","nom","article")
#plotArticle("metricoscience4","test.PNG",'SELECT COUNT( article_revue.`publication_scientifique_id`) AS article, faculte.`Nom` , article_revue.`Date`, indexation.`DB`FROM faculte JOIN (article_revue, enseignantchercheur,`publicationscientifique`, revuescientifique,`indexation`,`labo`,`departement`) ON (publicationscientifique.`author_ID` = enseignantchercheur.`Author_ID` AND enseignantchercheur.`labo_id`=`labo`.`id` AND publicationscientifique.`PublicationScientifique_ID`=`article_revue`.`publication_scientifique_id` and revuescientifique.`Revue_ID`=`article_revue`.`Revue_ID`AND revuescientifique.`Index_ID`=`indexation`.`ID_index` and labo.`dep_id`=`departement`.`ID` and departement.`Faculte_ID`=`faculte`.`ID`AND indexation.`DB`="web of science" ) GROUP by faulte.`Nom`','Nom','article')
#plotArticle("metricoscience4","test.PNG",'SELECT COUNT( article_revue.`publication_scientifique_id`) AS article, faculte.`Nom` , article_revue.`Date`, indexation.`DB`FROM faculte JOIN (article_revue, enseignantchercheur,`publicationscientifique`, revuescientifique,`indexation`,`labo`,`departement`) ON (publicationscientifique.`author_ID` = enseignantchercheur.`Author_ID` AND enseignantchercheur.`labo_id`=`labo`.`id` AND publicationscientifique.`PublicationScientifique_ID`=`article_revue`.`publication_scientifique_id` and revuescientifique.`Revue_ID`=`article_revue`.`Revue_ID`AND revuescientifique.`Index_ID`=`indexation`.`ID_index` and labo.`dep_id`=`departement`.`ID` and departement.`Faculte_ID`=`faculte`.`ID`AND indexation.`DB`="IET inspec" ) GROUP by faculte.`Nom`','Nom','article')
    