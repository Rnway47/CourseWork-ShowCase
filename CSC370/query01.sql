-- Retrieve the abbreviations of states that have over 150 counties 
-- which have an employment rate of at least 90% for each country in 2008, 
-- ordered by the number of counties in each state in descending order.

-- 1.05 marks: <8 operators
-- 1.0 marks: <10 operators
-- 0.8 marks: correct answer

SELECT abbr FROM County 
JOIN Countylabourstats ON (fips = county) 
JOIN State ON (state = id) 
WHERE (employed/labour_force) >= 0.9 AND year = 2008 
GROUP BY State 
Having COUNT(fips) > 150
ORDER BY COUNT(fips) DESC;