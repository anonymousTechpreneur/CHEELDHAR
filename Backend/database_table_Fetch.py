import sqlalchemy

from Create_database_connection import *

db_conn, connector = connect()
results = db_conn.execute(sqlalchemy.text("CALL GetCustomerDetails();")).fetchall()

for row in results:
    print(type(row))
    print(row.tuple)
    print(type(row))
    print(row[0])
disconnect(connector)
print("done")
#   # create ratings table in our sandwiches database
#   db_conn.execute(
#     sqlalchemy.text(
#        "CREATE PROCEDURE GetCustomerDetails() AS"
#         "BEGIN"
#         "SELECT *" 
#         "FROM Customer"
#         "WHERE CustomerId = customerID;"
#         "END;"
#     )
#   )

#   # commit transaction (SQLAlchemy v2.X.X is commit as you go)
#   db_conn.commit()

#   # insert data into our ratings table
#   insert_stmt = sqlalchemy.text(
#       "INSERT INTO ratings (name, origin, rating) VALUES (:name, :origin, :rating)",
#   )

#   # insert entries into table
#   db_conn.execute(insert_stmt, parameters={"name": "HOTDOG", "origin": "Germany", "rating": 7.5})
#   db_conn.execute(insert_stmt, parameters={"name": "BÀNH MÌ", "origin": "Vietnam", "rating": 9.1})
#   db_conn.execute(insert_stmt, parameters={"name": "CROQUE MADAME", "origin": "France", "rating": 8.3})

#   # commit transactions
#   db_conn.commit()

  # query and fetch ratings table
