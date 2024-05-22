--query
with table11 as (

    select * from country group by id, name, iso3_code

),

table12 as (
    
    select country_id, year, sum(value) soma  from gdp group by country_id, year
    
),

table1 as (
    
    select * 
    from table11 a left join table12 b on b.country_id = a.id
    
    )


SELECT
    id, name, iso3_code,
    ROUND(SUM(CASE WHEN year = 2019 THEN soma/ 1000000000.0 ELSE 0 END),2) AS '2019',
    ROUND(SUM(CASE WHEN year = 2020 THEN soma/ 1000000000.0 ELSE 0 END),2) AS '2020',
    ROUND(SUM(CASE WHEN year = 2021 THEN soma/ 1000000000.0 ELSE 0 END),2) AS '2021',
    ROUND(SUM(CASE WHEN year = 2022 THEN soma/ 1000000000.0 ELSE 0 END),2) AS '2022',
    ROUND(SUM(CASE WHEN year = 2023 THEN soma/ 1000000000.0 ELSE 0 END),2) AS '2023'
FROM
    table1
GROUP BY
    id, name, iso3_code;