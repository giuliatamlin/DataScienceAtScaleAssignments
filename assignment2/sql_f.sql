
SELECT count(*) FROM (
SELECT f1.docid
FROM frequency f1
WHERE f1.term = 'transactions'
INTERSECT
SELECT f2.docid
FROM frequency f2
WHERE f2.term = 'world') x
;
