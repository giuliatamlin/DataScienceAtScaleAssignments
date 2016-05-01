
--matrix multiply
SELECT mm.v FROM
(SELECT A.row_num,B.col_num, sum(A.value*B.value) as v
FROM A,B
where A.col_num=B.row_num
GROUP BY A.row_num,B.col_num) mm
WHERE mm.row_num = 2 AND mm.col_num = 3;