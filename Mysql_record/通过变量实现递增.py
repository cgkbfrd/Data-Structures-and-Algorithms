*********************并列排名连续增*******************************
SELECT 
	pid, 
	name, 
	age, 
	CASE 
		WHEN @prevRank = age THEN @curRank 
		WHEN @prevRank := age THEN @curRank := @curRank + 1
	END AS rank
FROM players p, 
(SELECT @curRank :=0, @prevRank := NULL) r
ORDER BY age

| PID |    NAME | AGE | RANK |
|-----|---------|-----|------|
|  10 |   Peter |  19 |    1 |
|  12 |   Andre |  20 |    2 |
|   2 |    Vino |  20 |    2 |
|   3 |    John |  20 |    2 |
|  11 |     Tom |  20 |    2 |
|   5 |   Brian |  21 |    3 |
|   4 |    Andy |  22 |    4 |
|   9 |  George |  23 |    5 |
|   6 |     Dew |  24 |    6 |
|   7 |    Kris |  25 |    7 |
|   1 |  Samual |  25 |    7 |
|   8 | William |  26 |    8 |




*********************并列排名非连续增*******************************
SELECT pid, name, age, rank 
FROM
(
	SELECT
		pid, name, age,
		@curRank := IF(@prevRank = age, @curRank, @incRank) AS rank, 
		@incRank := @incRank + 1, 
		@prevRank := age
	FROM players p, 
		(SELECT @curRank :=0, @prevRank := NULL, @incRank := 1) r #仅仅是对变量@curRank、@preRank、@incRank初始化的作用
	ORDER BY age
) s
| PID |    NAME | AGE | RANK |
|-----|---------|-----|------|
|  10 |   Peter |  19 |    1 |
|  12 |   Andre |  20 |    2 |
|   2 |    Vino |  20 |    2 |
|   3 |    John |  20 |    2 |
|  11 |     Tom |  20 |    2 |
|   5 |   Brian |  21 |    6 |
|   4 |    Andy |  22 |    7 |
|   9 |  George |  23 |    8 |
|   6 |     Dew |  24 |    9 |
|   7 |    Kris |  25 |   10 |
|   1 |  Samual |  25 |   10 |
|   8 | William |  26 |   12 |
