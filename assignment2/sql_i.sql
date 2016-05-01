create table if not exists q(kw varchar(20));
insert into q values('washingston');
insert into q values('taxes');
insert into q values('treasury');

--without similarity matrix
select max(s.v) from (
    SELECT f1.docid,sum(f1.count) as v
    from frequency f1
    where f1.term in (select kw from q)
    group by f1.docid) s;
