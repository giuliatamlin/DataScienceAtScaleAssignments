
SELECT count(*) FROM(
   SELECT docid, count(term) as term_cnt
   FROM frequency
   GROUP by docid
   HAVING term_cnt > 300);