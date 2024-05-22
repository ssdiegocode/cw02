import duckdb

def execute_query(database, query):

    conn = duckdb.connect(database)

    with open(query, 'r') as file:
        sql_query = file.read()

    results = conn.execute(sql_query).fetchall()

    for row in results:
        print(row)

    conn.close()

if __name__ == "__main__":
    
    database = "database.duckdb"  
    query = "query.sql"  

    execute_query(database, query)