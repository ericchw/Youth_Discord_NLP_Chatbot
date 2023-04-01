import psycopg2

try:
    #connect to the database
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="admin",
        password="admin"
    )
    cursor = connection.cursor()

    # create table
    create_table_query = '''
    CREATE TABLE test
    (ID SERIAL PRIMARY KEY,
    NAME TEXT NOT NULL,
    SALARY REAL NOT NULL);'''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")