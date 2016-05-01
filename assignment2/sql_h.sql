--similarity matrix
SELECT dd.v FROM
   (SELECT f1.docid as row_in,f2.docid as col_in,sum(f1.count*f2.count) as v
    from frequency f1, frequency f2
    --exploit symmetry
    where f1.term = f2.term AND f1.docid<f2.docid
    group by f1.docid,f2.docid) dd
    where dd.row_in = '10080_txt_crude' AND dd.col_in = '17035_txt_earn';