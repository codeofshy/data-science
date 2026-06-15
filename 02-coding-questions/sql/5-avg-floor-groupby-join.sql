-- https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true

-- Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.


SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY CROSS JOIN COUNTRY
ON CITY.CountryCode = COUNTRY.Code
GROUP BY COUNTRY.CONTINENT;


-- https://www.hackerrank.com/challenges/average-population/problem?isFullScreen=true
-- Query the average population for all cities in CITY, rounded down to the nearest integer.
select floor(avg(population))
from city;
