import duckdb

def create_database(name, data_list):
    conn = duckdb.connect(database=f"{name}.duckdb")

    base1 = data_list[0]
    base2 = data_list[1]

    conn.execute(f"CREATE OR REPLACE TABLE country AS SELECT * FROM read_json_auto('{base1}.json')")

    conn.execute(f"CREATE OR REPLACE TABLE gdp AS SELECT * FROM read_json_auto('{base2}.json')")

    conn.close()

#create_database('database', bases=['country_data', 'gpd_data'])