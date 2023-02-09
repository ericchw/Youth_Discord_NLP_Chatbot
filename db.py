import psycopg2
from datetime import datetime, timezone

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
        
        if mode == "r":
             column_names = [desc[0] for desc in cursor.description]
             record = cursor.fetchall()
             return column_names, record
        else: # c = create, u = update, d = delete
            connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")




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
  