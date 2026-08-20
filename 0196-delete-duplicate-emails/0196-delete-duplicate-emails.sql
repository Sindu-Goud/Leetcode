-- delete p1 
-- from person p1 
-- join 
-- person p2 
-- on 
-- p1.email = p2.email 
-- and 
-- p1.id > p2.id;

delete from person 
where id not in (select min_id from

(select min(id) as min_id
from person group by email)as temp);
