# Write your MySQL query statement below
#Desc
SELECT score,
DENSE_RANK() over (ORDER BY score Desc) 'rank'
FROM Scores
