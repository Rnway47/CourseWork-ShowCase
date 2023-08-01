-- Retrieve the list of states (showing both the id and abbreviation) 
-- and their corresponding total area, 
-- not accounting for the counties that have more than 10000 population in the year of 2010, 
-- sorted by area in descending order.

-- 1.05 marks: < 11 operators
-- 1.0 marks: < 13 operators
-- 0.8 marks: correct answer

SELECT id, abbr, sum(sq_km) AS 'area' FROM State 
JOIN County ON (state = id) JOIN CountyPopulation ON (county = fips AND year = 2010) 
WHERE population < 10000 
GROUP BY state 
ORDER BY sum(sq_km) DESC;