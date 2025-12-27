CREATE TABLE fitness(

 UserID SERIAL PRIMARY KEY,
 UserName VARCHAR(50),
 Age INT,
 Gender TEXT,
 JoinDate DATE,
 Goal TEXT,
Trainer_Name TEXT,
Membership VARCHAR(20),
MembershipStart DATE,
MembershipEnd DATE,
Status VARCHAR(20),
Height_cm INT,
StartingWeight NUMERIC(4,1),
BMI NUMERIC(4,1)

);

SELECT * FROM fitness

COPY fitness (UserID, UserName, Age,Gender,JoinDate,Goal,Trainer_Name,Membership,MembershipStart,MembershipEnd,Status,Height_cm,StartingWeight,BMI)
FROM 'C:\Program Files\PostgreSQL\17\data\fitness_data.csv'
DELIMITER ','
CSV HEADER;



-- 1.Count total members

SELECT COUNT(username) As Total_Members
FROM fitness;


-- 2.Find all members with Active membership
SELECT UserName, Membership, MembershipEnd
FROM fitness
WHERE Status = 'Active';


-- 3.List members who joined after July 2024
SELECT UserName, JoinDate
FROM fitness
WHERE JoinDate > '2024-07-01';


-- 4.Average BMI by Goal

SELECT Goal, ROUND(AVG(BMI), 2) AS Avg_BMI
FROM fitness
GROUP BY Goal
ORDER BY Avg_BMI DESC;


-- 5.Find top 5 members with highest BMI

SELECT UserName, BMI
FROM fitness
ORDER BY BMI DESC
LIMIT 5;



-- 6.Count members by Membership Type and Status

SELECT Membership, Status, COUNT(*) AS Total
FROM fitness
GROUP BY Membership, Status
ORDER BY Membership, Status;


-- --------------------------------THE END----------------------


