select Last_Name +First_Name as FullName,
'10' +Year_result,
Year_Result +Section_ID,
convert( nvarchar(10),Student_id)+[Login]
from Student where last_name between 'a' and 'f'
order by FullName