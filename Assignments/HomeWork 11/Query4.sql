select s.CWID, s.Name, count(g.Course) as No_of_Course
from students as s
join grades as g
where s.CWID = g.StudentCWID
group by s.CWID