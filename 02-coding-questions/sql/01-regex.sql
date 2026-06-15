-- question
-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

-- Solution:
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY REGEXP '^[aeiou]';



-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY REGEXP '[aeiou]$';


-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY REGEXP '^[aeiou].*[aeiou]$';


-- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

SELECT distinct CITY
from station
where city not REGEXP '^[aeiou]';

-- Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
SELECT distinct CITY
from station
where city not REGEXP '[aeiou]$';


-- Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
SELECT distinct city
from station
where city not regexp '^[aeiou].*[aeiou]$';


-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY REGEXP '^[^aeiou].*[^aeiou]$';

-- ^[^aeiou]: The second caret inside the brackets acts as a negation, meaning "does not start with a vowel".
-- [^aeiou]$: Similarly, this means "does not end with a vowel".