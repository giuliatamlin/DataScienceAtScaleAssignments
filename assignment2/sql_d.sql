   SELECT count(distinct f.docid)
   FROM frequency f
   WHERE f.term = 'law' OR f.term = 'legal';
