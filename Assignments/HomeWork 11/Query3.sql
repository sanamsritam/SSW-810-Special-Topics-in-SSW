select Course, Grade, count(Grade) as Frequency
from grades
where Course = 'SSW 810'
group by Grade
limit 1