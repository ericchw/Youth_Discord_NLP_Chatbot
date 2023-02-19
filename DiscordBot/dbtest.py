import psycopg2

try:
    connection = psycopg2.connect(user="admin",
                                password="admin",
                                host="localhost",
                                port="5432",
                                database="sjs")
    cursor = connection.cursor()
    print("PostgreSQL connection is established.")

    sqlStatement = "INSERT INTO games VALUES (DEFAULT, 'test', 'test_zh');"
    cursor.execute(sqlStatement)
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")