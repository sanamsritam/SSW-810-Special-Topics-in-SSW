select s.Name as Student_Name, s.CWID, g.Course, g.Grade, i.Name as Instructor_Name
from students as s
join grades as g on g.StudentCWID = s.CWID
join instructors as i on  g.InstructorCWID = i.CWID
order by s.Name