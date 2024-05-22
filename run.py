import requests
import json
from datetime import datetime
import os
import glob

from cloud_con import api_conn
from cloud_move import move_all
from cloud_transformation import transform_data
from cloud_database import create_database
from cloud_report import execute_query
from delete import delete_json_files

# -------------------------------

def execution_steps():
    current_directory = os.getcwd()
    delete_json_files(current_directory)
    base_url = "https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page="
    data = api_conn(base_url)
    move_all('api-log', '*.json')
    transform_data(data)
    print("data ready")
    bases=['country_data', 'gpd_data']
    create_database('database', bases)
    move_all('json-base', '*.json')
    execute_query('database.duckdb', 'query.sql')

execution_steps()