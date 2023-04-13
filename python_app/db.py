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
        with open('dbSQLStatement.sql', 'r') as file:
            sql = file.read()
        cursor.execute(sql)
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

    # finally:
    #     # closing database connection.
    #     if connection:
    #         cursor.close()
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
  