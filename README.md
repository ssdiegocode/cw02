# cw-etl-practice

A project to fetch data from the World Bank API, transform it, and store it in a DuckDB database using Docker.

## Project Structure

project/<br>
├── api-log/<br>
├── json-base/<br>
├── docker-compose.yml<br>
├── run.py<br>
├── cloud_con.py<br>
├── cloud_move.py<br>
├── cloud_transformation.py<br>
├── cloud_database.py<br>
├── cloud_report.py
├── delete.py
└── README.md<br>

Download this folder, make sure you are in the main directory and run:

`docker-compose up --build`<br>

## Tools 

* World Bank API
* Docker
* DuckDB
* Pure Python

## Description:

The project began with a straightforward function aimed at establishing a connection and extracting data from the World Bank API. However, it became apparent that this initial function only retrieved content from a single page. then my efforts were redirected towards enhancing the data retrieval process.

Anticipating the utilization of JSON files as a source for the DuckDB database, the focus went towards transforming the data to facilitate the integration, potentially through methods like the COPY command for efficient data movement within the database.

Additionally, utility functions such as delete.py and move.py were introduced to streamline file management and organization within the project structure.
