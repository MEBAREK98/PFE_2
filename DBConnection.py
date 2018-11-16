import pymysql

def get_connection(datab) :
    db = pymysql.connect("localhost","root","Ketfi_amira",datab)
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

def insert_info(datab,FIRST_NAME, LAST_NAME, E_MAIL, AFFILIATION, H_INDEX, NUM_CITATION, DOMAINE) :
    
    db = get_connection(datab)
    cursor = db.cursor()
    #Prepare SQL query to INSERT a record into the database author table.
    sql ="INSERT INTO AUTHEUR(FIRST_NAME, \
                LAST_NAME, E-MAIL, AFFILIATION, H-INDEX, NUM_CITATION, DOMAINE) \
                VALUES ('%s', '%s', '%s', '%s', '%d', '%d', '%s' )" %\
                (FIRST_NAME, LAST_NAME, E_MAIL, AFFILIATION, H_INDEX, NUM_CITATION, DOMAINE)
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
   