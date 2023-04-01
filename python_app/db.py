import psycopg2
import logging
import sys

# create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a console handler
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

# create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handler to the logger
logger.addHandler(handler)

def initiate():
    try:
        connection = psycopg2.connect(
            host="db",
            port="5432",
            database="sjs",
            user="admin",
            password="admin"
            )
        cursor = connection.cursor()
        logger.debug("PostgreSQL connection is established.")
        cursor.execute("""
--DROP TABLE IF EXISTS account;
--DROP TABLE IF EXISTS chatlog;
--DROP TABLE IF EXISTS information;
--DROP TABLE IF EXISTS helplog;
--DROP TABLE IF EXISTS polling;
--DROP TABLE IF EXISTS event;
--DROP TABLE IF EXISTS activity;
        
CREATE TABLE IF NOT EXISTS account (
    id SERIAL PRIMARY KEY,
    email VARCHAR,
    pwd VARCHAR,
    username VARCHAR
);

INSERT INTO
    account(email, pwd, username)
VALUES
    (   
        '1234@gmail.com',
        MD5('1234'),
        'Ken'
    );


CREATE TABLE IF NOT EXISTS chatlog (
    id SERIAL PRIMARY KEY,
    senderName VARCHAR,
    senderId VARCHAR,
    message VARCHAR,
    label VARCHAR,
    timestamp TIMESTAMP
);


CREATE TABLE IF NOT EXISTS helplog (
    id SERIAL PRIMARY KEY,
    userName VARCHAR,
    userId VARCHAR,
    timestamp TIMESTAMP
);


CREATE TABLE IF NOT EXISTS information (
    name VARCHAR PRIMARY KEY,
    phoneNumber VARCHAR,
    whatsapp VARCHAR,
    website VARCHAR,
    instagram VARCHAR,
    discord VARCHAR,
    servicehours VARCHAR
);

INSERT INTO
    information
VALUES
    (
        '聖雅各福群會6PM網上青年支援隊',
        '26093228',
        '59333711',
        'https://www.cyberyouth.sjs.org.hk/',
        'https://www.instagram.com/6pm.hk/',
        'https://discord.gg/6pm',
        'https://cdn.discordapp.com/attachments/709787197385080852/933897809076314132/5ee1ae88efa3e739.png'
    );


CREATE TABLE IF NOT EXISTS Activity (
    ATYId SERIAL PRIMARY KEY,
    ATYName VARCHAR,
    ATYCreateDate TIMESTAMP,
    ATYUpdateDate TIMESTAMP
);


CREATE TABLE IF NOT EXISTS Event(
    EVTId SERIAL PRIMARY KEY,
	ATYId SERIAL,
    EVTTitle VARCHAR,
    EVTLimitMem int,
    EVTDesc VARCHAR,
    EVTDeadline TIMESTAMP,
    EVTDate TIMESTAMP,
    EVTCreateDate TIMESTAMP,
    EVTUpdateDate TIMESTAMP,
	CONSTRAINT fk_Event FOREIGN KEY (ATYId) REFERENCES Activity(ATYId)
);


CREATE TABLE IF NOT EXISTS Polling(
    POLLId SERIAL PRIMARY KEY,
    EVTId SERIAL,
    POLLDCId VARCHAR,
    POLLDCUsername VARCHAR,
    POLLCreateDate TIMESTAMP,
    POLLUpdateDate TIMESTAMP,
	CONSTRAINT fk_Polling FOREIGN KEY (EVTId) REFERENCES Event(EVTId)
);
""")
        connection.commit()
        logger.debug('db initial done')
    except (Exception, psycopg2.Error) as error:
        logger.debug("Error while fetching data from PostgreSQL in db.initial", error)
        

def connectDB(sqlStatement, mode):
    try:
        connection = psycopg2.connect(user="admin",
                                    password="admin",
                                    host="db",
                                    port="5432",
                                    database="sjs")
        cursor = connection.cursor()
        logger.debug("PostgreSQL connection is established.")

        cursor.execute(sqlStatement)
        if mode == "c":
            defaultId = cursor.fetchone()[0]
            connection.commit()
            return defaultId
        elif mode == "r":
             column_names = [desc[0] for desc in cursor.description]
             record = cursor.fetchall()
             return column_names, record
        else: # i = insert, u = update, d = delete
            connection.commit()
    except (Exception, psycopg2.Error) as error:
        logger.debug("Error while fetching data from PostgreSQL in db.connectDB", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            # connection.close()
            # logger.debug("PostgreSQL connection is closed")


    ###################SEARCH######################
    # postgreSQL_select_Query = "select * from account"
    # cursor.execute(postgreSQL_select_Query)
    # logger.debug("Selecting rows from account table using cursor.")
    # account_records = cursor.fetchall()

    # logger.debug("Print each row and it's columns values")
    # for row in account_records:
    #     logger.debug("aid = ", row[0], )
    #     logger.debug("email = ", row[1])
    #     logger.debug("usename  = ", row[3], "\n")

    ###################SEARCH######################
    # # create table
    # create_table_query = '''CREATE TABLE employees (ID SERIAL PRIMARY KEY, NAME TEXT NOT NULL, SALARY REAL NOT NULL);'''
    # cursor.execute(create_table_query)
    # connection.commit()
    # logger.debug("Table created successfully in PostgreSQL ")
# test
# connectDB(f"INSERT INTO chatlog VALUES (DEFAULT,'{'CyberU'}', '{'test'}', '{'chatbot'}', '{datetime.now(timezone.utc)}')", "u")
  