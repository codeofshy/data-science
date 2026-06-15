-- verify students table 
select * from students;

-- verify marks table 
select * from marks;

-- inner join : returns the common data id exist in both the data
select students.name, marks.subject, marks.score
from students
inner join marks 
on students.id = marks.student_id;

-- left join : returns the left table and common data id exist in both the data
select students.name, marks.subject, marks.score
from students left join marks 
on students.id = marks.student_id;

-- right join : returns the right table and common data id exist in both the data
select students.name, marks.subject, marks.score
from students right join marks 
on students.id = marks.student_id;

-- cross join : returns the rall data exist in both the data
select students.name, marks.subject, marks.score
from students cross join marks;