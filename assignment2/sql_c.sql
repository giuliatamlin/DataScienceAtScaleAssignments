SELECT count(*) FROM (
    SELECT f1.term
    FROM frequency f1
    WHERE f1.count =1 AND f1.docid = '10398_txt_earn'
    UNION
    SELECT f2.term
    FROM frequency f2
    WHERE f2.count = 1 AND f2.docid = '925_txt_trade') x;