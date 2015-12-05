CREATE TABLE EXPM_MCCRATE AS
(
  SELECT AAA.mccname, AAA.age, AAA.region_, AAA.sum_mcc/BBB.sum_total*100 as mcc_rate
  FROM
  (
    SELECT mccname, age, region_, SUM(summarur_amt) as sum_mcc
    FROM EXPM_balances
    WHERE cardtrnmcc_ccode IN ('5691', '5722', '4511', '5732', '5812', '8099', '5977', '5712') AND age >= 20 AND age <= 60
    GROUP BY mccname, age, region_
  ) AAA
  INNER JOIN
  (
    SELECT age, region_, SUM(summarur_amt) as sum_total
    FROM EXPM_balances
    WHERE mccname IS NOT NULL AND age >= 20 AND age <= 60
    GROUP BY age, region_
  ) BBB
  ON AAA.age = BBB.age AND AAA.region_ = BBB.region_
)
