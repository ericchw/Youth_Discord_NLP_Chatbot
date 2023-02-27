import psycopg2

def initiate():

    try:
        try:
            connection = psycopg2.connect(user="admin",
                                    password="admin",
                                    host="localhost",
                                    port="5432",
                                    database="sjs")
            cursor = connection.cursor()
            print("PostgreSQL connection is established.")

            cursor.execute("""
        
DROP TABLE account;
DROP TABLE chatlog;
DROP TABLE helplog;
DROP TABLE games;
DROP TABLE information;
DROP TABLE event_detail;
DROP TABLE event_header;


CREATE TABLE IF NOT EXISTS account
(
    id SERIAL PRIMARY KEY,
	email VARCHAR,
	pwd VARCHAR,
    username VARCHAR
);

CREATE TABLE IF NOT EXISTS chatlog
(
    id SERIAL PRIMARY KEY,
    senderName VARCHAR,
	senderId VARCHAR,
	message VARCHAR,
	label VARCHAR,
	timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS helplog
(
    id SERIAL PRIMARY KEY,
    userName VARCHAR,
	userId VARCHAR,
	timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS games
(
    id SERIAL PRIMARY KEY,
	name VARCHAR,
    name_zh VARCHAR
);

CREATE TABLE IF NOT EXISTS information
(
    name VARCHAR PRIMARY KEY,
    phoneNumber VARCHAR,
    whatsapp VARCHAR,
    website VARCHAR,
    instagram VARCHAR,
    discord VARCHAR,
    servicehours VARCHAR
);

INSERT INTO account(email, pwd, username) VALUES ('cyberyouth@sjs.org.hk', 'sjs', 'sjs');
INSERT INTO information VALUES ('聖雅各福群會6PM網上青年支援隊', '26093228', '59333711', 'https://www.cyberyouth.sjs.org.hk/', 'https://www.instagram.com/6pm.hk/', 'https://discord.gg/6pm', 'https://cdn.discordapp.com/attachments/709787197385080852/933897809076314132/5ee1ae88efa3e739.png');
INSERT INTO games VALUES
	(1, 'Other', '其他'),
	(2, 'League of Legends', '英雄聯盟'),
	(3, 'Apex Leagues', 'Apex 英雄'),
	(4, 'Fall Guys', '糖豆人'),
	(5, 'PUBG: Battlegrounds', '絕地求生'),
	(6, 'PUBG MOBILE', '絕地求生M'),
	(7, 'Brawlhalla', '英靈神殿大亂鬥'),
	(8, 'Talesrunner', '跑Online'),
	(9, 'Among Us', '太空狼人殺'),
	(10, 'Rummikub', '魔力橋'),
	(11, 'Board Game Arena', '桌遊競技場'),
	(12, 'Arena of Valor', '傳說對決'),
	(13, 'Honor of Kings', '王者榮耀')
;


CREATE TABLE IF NOT EXISTS Event_Header(
    eHdrId SERIAL PRIMARY KEY,
    eHdrTitle VARCHAR,
    eHdrStatus VARCHAR,
    eHdrLimitMem int,
    eHdrDesc VARCHAR,
    eHdrDate TIMESTAMP,
    eHdrCreateDate TIMESTAMP,
    eHdrUpdateDate TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Event_Detail(
    eDtlId SERIAL PRIMARY KEY,
    eDtlHdrId INTEGER,
    eDtlVoteDtl VARCHAR, 
    CONSTRAINT fk_EventDetail FOREIGN KEY (eDtlHdrId) REFERENCES Event_Header(eHdrId)
);

INSERT INTO event_header VALUES (DEFAULT, 'test1', 'Pending', 1, 'desc', '2023-12-28 01:37:00', '2023-02-27 01:37:00', NULL);

""")
        
            connection.commit()
            
        except(Exception, psycopg2.Error) as error:
            
            connection = psycopg2.connect(user="admin",
                                        password="admin",
                                        host="localhost",
                                        port="5432",
                                        database="sjs")
            cursor = connection.cursor()
            print("PostgreSQL connection is established.")

            cursor.execute("""

            
CREATE TABLE IF NOT EXISTS account
(
    id SERIAL PRIMARY KEY,
	email VARCHAR,
	pwd VARCHAR,
    username VARCHAR
);

CREATE TABLE IF NOT EXISTS chatlog
(
    id SERIAL PRIMARY KEY,
    senderName VARCHAR,
	senderId VARCHAR,
	message VARCHAR,
	label VARCHAR,
	timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS helplog
(
    id SERIAL PRIMARY KEY,
    userName VARCHAR,
	userId VARCHAR,
	timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS games
(
    id SERIAL PRIMARY KEY,
	name VARCHAR,
    name_zh VARCHAR
);

CREATE TABLE IF NOT EXISTS information
(
    name VARCHAR PRIMARY KEY,
    phoneNumber VARCHAR,
    whatsapp VARCHAR,
    website VARCHAR,
    instagram VARCHAR,
    discord VARCHAR,
    servicehours VARCHAR
);

INSERT INTO account(email, pwd, username) VALUES ('cyberyouth@sjs.org.hk', 'sjs', 'sjs');
INSERT INTO information VALUES ('聖雅各福群會6PM網上青年支援隊', '26093228', '59333711', 'https://www.cyberyouth.sjs.org.hk/', 'https://www.instagram.com/6pm.hk/', 'https://discord.gg/6pm', 'https://cdn.discordapp.com/attachments/709787197385080852/933897809076314132/5ee1ae88efa3e739.png');
INSERT INTO games VALUES
	(1, 'Other', '其他'),
	(2, 'League of Legends', '英雄聯盟'),
	(3, 'Apex Leagues', 'Apex 英雄'),
	(4, 'Fall Guys', '糖豆人'),
	(5, 'PUBG: Battlegrounds', '絕地求生'),
	(6, 'PUBG MOBILE', '絕地求生M'),
	(7, 'Brawlhalla', '英靈神殿大亂鬥'),
	(8, 'Talesrunner', '跑Online'),
	(9, 'Among Us', '太空狼人殺'),
	(10, 'Rummikub', '魔力橋'),
	(11, 'Board Game Arena', '桌遊競技場'),
	(12, 'Arena of Valor', '傳說對決'),
	(13, 'Honor of Kings', '王者榮耀')
;


CREATE TABLE IF NOT EXISTS Event_Header(
    eHdrId SERIAL PRIMARY KEY,
    eHdrTitle VARCHAR,
    eHdrStatus VARCHAR,
    eHdrLimitMem int,
    eHdrDesc VARCHAR,
    eHdrDate TIMESTAMP,
    eHdrCreateDate TIMESTAMP,
    eHdrUpdateDate TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Event_Detail(
    eDtlId SERIAL PRIMARY KEY,
    eDtlHdrId INTEGER,
    eDtlVoteDtl VARCHAR, 
    CONSTRAINT fk_EventDetail FOREIGN KEY (eDtlHdrId) REFERENCES Event_Header(eHdrId)
);
        """)
        
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        

def connectDB(sqlStatement, mode):
    try:
        connection = psycopg2.connect(user="admin",
                                    password="admin",
                                    host="localhost",
                                    port="5432",
                                    database="sjs")
        cursor = connection.cursor()
        print("PostgreSQL connection is established.")

        cursor.execute(sqlStatement)
        if mode == "c":
            defaultId = cursor.fetchone()[0]
            connection.commit()
            return defaultId
        elif mode == "r":
             column_names = [desc[0] for desc in cursor.description]
             record = cursor.fetchall()
             return column_names, record
        else: # u = update, d = delete
            connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            # connection.close()
            # print("PostgreSQL connection is closed")




    ###################SEARCH######################
    # postgreSQL_select_Query = "select * from account"
    # cursor.execute(postgreSQL_select_Query)
    # print("Selecting rows from account table using cursor.")
    # account_records = cursor.fetchall()

    # print("Print each row and it's columns values")
    # for row in account_records:
    #     print("aid = ", row[0], )
    #     print("email = ", row[1])
    #     print("usename  = ", row[3], "\n")

    ###################SEARCH######################
    # # create table
    # create_table_query = '''CREATE TABLE employees (ID SERIAL PRIMARY KEY, NAME TEXT NOT NULL, SALARY REAL NOT NULL);'''
    # cursor.execute(create_table_query)
    # connection.commit()
    # print("Table created successfully in PostgreSQL ")
# test
# connectDB(f"INSERT INTO chatlog VALUES (DEFAULT,'{'CyberU'}', '{'test'}', '{'chatbot'}', '{datetime.now(timezone.utc)}')", "u")
  