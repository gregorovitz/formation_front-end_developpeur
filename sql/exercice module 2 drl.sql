--exercice 2.1.1
--– Les requêtes suivantes fonctionnent-elles sous SQL-Server ?
--Si non, comment les corriger ? 
--N’hésitez pas à tester vos requêtes directement sous Management Studio ! 


Select last_name,
	first_name as F_name 
from student;  --non  nom peux pas avoir d'espace

select last_name lname, 
	first_name as fname 
from student; --oui 

select last_name + '_' +  first_name as name
from student; --non car || ne fonctione pas sur sql server et il manque les quote autour de l'underline

select last_name +first_name as name ,
	Year_result * 10 result 
	From student; -- non car le x remplacer par * et pas de , avant from

--2.1.2

select last_name,
	birth_date ,
	[login],
	year_result 
from student;

--2.1.3
select last_name+' '+first_name as nomcomplet,
	student_id,
	birth_date
from student;

--2.1.4
select convert(nvarchar(10),student_id) +' | '+ last_name  +' | '+first_name  +' | '+convert(nvarchar(10),birth_date) +' | '+[login] +' | '+convert(nvarchar(10),year_result) +' | '+convert(nvarchar(10),section_id) +' | '+course_id from student

--2.2.1
select [login],
	year_result
from student
where year_result>16;
--2.2.2
select last_name,
	section_id 
from student 
where first_name ='Georges';
--2.2.3
select last_name,
	Year_result
from student
where year_result between 12 and 16;
--2.2.4
select last_name , 
	section_id,
	year_result 
from student
where section_id not in (1010,1020,1110);
--2.2.5
select last_name,
	year_result
from student 
where last_name like '%r';
--2.2.6
select last_name,
	year_result
from student 
where last_name like'__n%'and year_result >10;
--2.2.7
select last_name,
	year_result
from student
where year_result <=3
order by year_result desc;
--2.2.8
select last_name+' '+first_name,
	year_result 
from student 
where section_id =1010
order by last_name;
--2.2.9
select last_name,
	section_id,
	year_result 
from student
where section_id in (1010,1020) and year_result not between 12 and 18
order by section_id;
--2.2.10
select last_name,
	section_id,
	year_result*100/20 as [résultat sur 100] 
from student
where section_id like '13%' and year_result*100/20<=60;

--2.2.11
--Ordre « SELECT … FROM » p
--Alias p
--Concaténation et conversion de type de données (CONVERT) p
--Clause « WHERE » p
--Opérations arithmétiques p
--Opérateurs « BETWEEN », « IN », « LIKE » et leur négation p
--Comparaison avec une valeur « NULL » p
--Opérateurs « AND » et « OR » p
--Clause « ORDER BY » p

--obtenir des date

select GetDate(),
		GETUTCDATE(),
		SYSDATETIME(),
		SYSDATETIMEOFFSET();

--extraction d'une date
select DatePart(yyyy,getdate());
select DatePart(mm,getdate());
select DatePart(dd,getdate());
select DatePart(ns,getdate());
select DatePart(mcs,getdate());
select Year(getdate()); -->select DatePart(yyyy,getdate());
select MONTH(getdate()); -->select DatePart(mm,getdate());
select day(getdate()); -->select day(getdate()); -->

--avg attention avg entier
select avg(convert(float,year_result)) from student

--exercice2.3.1
 --car null ne peux pas etre comparer

--exercice 2.3.2

--car compte le nombre de ligne

--exercice 2.3.3
--La fonction « AVG » renvoie la moyenne de toutes les lignes résultantes d’une requête SELECT sur une colonne incluant toutes les valeurs « NULL ». (Vrai/Faux ?) 

 
--faux elle ne prend pas en compte les null

--exercice2.3.4
--pas pour ajouter les totaux aux colonne mais pour calculer le total d'une collone

--exercice 2.3.5

--vrai

--exercice 2.3.6

--select count (*)from student; --non il manque les parenthese autour du *

--select count (student_id),login From Student --nom car les agregat renvoi seulement une reponse donc peux pas metre le login de plus [login]

--select min(year_result),max(birth_date) from student where year_result>12; --oui

--exercice2.3.7

select avg(convert(float,year_result)) from student;
--exercice 2.3.8
select max (year_result) from student;
--exercice 2.3.9
select sum(year_result) from student;
--exercice 2.3.10
select min (Year_result) from student;
--exercice 2.3.11
select count(*) from student;
--2.3.12
select [login],Year(birth_date) as [Année de naissance] 
from student 
where Year(birth_date)>1970;
 --exercice 2.3.13
 select [login],last_name from student where len(last_name)>=8;
 --exercice 2.3.14
 select Upper(Last_name) as [nom de Fammille],first_name,year_result 
 from student
 where year_result>=16 
 order by year_result desc;

 --exercice 2.3.15
 select first_name, last_name,[login]
 ,case 
 when Year_result between 6 and 10
 then substring(lower(first_name),1,2)+substring(lower(last_name),1,4) 
 end as [nouveau Login]
 from student
 where year_result between 6 and 10

 --exercice 2.3.16
 select first_name, last_name,[login]
 ,case year_result
 when 10
 then substring(lower(first_name),
 len(first_name)-2,
 len(first_name))+convert(nvarchar,year(getDate())-year(birth_date) )
  when 12
 then substring(lower(first_name),
 len(first_name)-2,len(first_name))+convert(nvarchar,year(getDate())-year(birth_date) )
 when 14
 then substring(lower(first_name),len(first_name)-2,len(first_name))+convert(nvarchar,year(getDate())-year(birth_date) )

 end as [nouveau Login]
 from student where year_result=10 or year_result=12 or year_result=14;

 --exercice 2.3.17
 select last_name,[login],year_result
 from student
 where SUBSTRING(Last_name,1,1) in ('D','m','s')
 order by birth_date 
 --exercice 2.3.18
 select last_name,[login],Year_result
 from student
 where year_result%2 =1 and YEAr_result>10 
 order by year_result desc
 --exercice 2.3.19
 select count(*) as [nbre de noms de plus de 7 lettres]
 from student
 where len(last_name) >=7
 --exercice 2.3.20
 select last_name,year_result,
 case 
 when year_result >=12 then 'ok'
 else 'ko'
 end as status
 from student
 where year(birth_date)<1955;
 --exercice 2.3.21

 select last_name,Year_result,
  case 
 when year_result <10 then 'inferieure'
 when year_result =10 then 'neutre'
 else 'supérieure'
 end as status
 from student
 where year (birth_date) between 1955 and 1965;

--exercice 2.3.22

select last_name, year_result,convert (nvarchar,birth_date,106) as Literral_date  
from student 
where year (birth_date) between 1975 and 1985; 

--exercice 2.3.23
select last_name,month(birth_date) as [mois de naissance],
	year_result,
	nullif(year_result,4) as[nouveau résultat] 
from student 
where Month(birth_date) not in(12,1,2,3)and year_result<7;

--exemple group by
select section_id,Avg(year_result)
from student
where left(last_name,1)in('b','c','d')
group by section_id
having avg(year_result)>7;


select section_id,course_id,avg(year_result)
from student 
where section_id in(1010,1020)
group by course_id,section_id
--rollup 
select section_id,course_id,avg(year_result)
from student 
where section_id in(1010,1020)
group by rollup (section_id,course_id)
--cube
select section_id,course_id,avg(year_result)
from student 
where section_id in(1010,1020)
group by Cube(course_id,section_id)

--recupérer les 3 dernier lettre du last_name
select Right(last_name,3)
from student

select Right ('00' +convert(varchar,day(getdate())),2)

--group by
--exercice2.4.6

--select section_id,count(last_name) from student group by last_name --non car pas section_id n'est pas un agregat

--select section_id ,avg(year_result) from student where avg(year_result)>50
--group by section_id -- pas de fonction aggragate dans la clause where

--select section_id ,avg(year_result) from student where year_result>10
--group by section_id -- oui

--exercice 2.4-7

select section_id,max(year_result)as [résultat maximun]
from student
group by section_id;
--exercice 2.4.8
select section_id ,avg(convert(float,year_result)) as Moyenne from student
where section_id like '10%'
group by section_id

--exercice 2.4.9

select month(birth_date) as [mois de naissance], avg(Year_result) as moyenne
from student 
where year(birth_date) between 1970 and 1985
group by month(birth_date)

--exercice 2.4.10

select section_id, avg(convert(float,year_result)) as Moyenne
from student 
group by section_id
having count(*)>3

--exercice 2.4.11

select section_id,avg(year_result)as moyenne, max (year_result) as [Résultat maximum]
from student
group by section_id
having avg(year_result)>8

--cube rollup
--exercice 2.5.1
--exercice 2.5.5
select section_ID,course_id, sum(convert(float,year_result)) as total
from student
where section_id in (1010,1320)
group by cube(course_id,section_id)
--exercice2.5.6

select section_ID,course_id, avg(convert(float,year_result)) as Moyenne
from student
where section_id in (1010,1320)
group by rollup(section_id,course_id)

--exercice 2.5.7
select course_id,section_ID, avg(convert(float,year_result)) as Moyenne
from student
where section_id in (1010,1320)
group by cube(course_id,section_id)

--2.5.8
-- Clause « GROUP BY … HAVING » et règles d’or   p
-- Différence entre les clauses « WHERE » et « HAVING »   p
-- « GROUP BY » sur plusieurs colonnes   p
-- Clause « ROLLUP » s
-- Clause « CUBE »  s


--exemmple  join
select st.section_id,last_name,se.section_name
from student as st
join section as se on st.section_id=se.section_id
where st.section_id in (1010,1020)

--exemple cross join
select *
From section s1
cross join section s2
where s1.section_id!=s2.section_id

--ou
select *
From section s1,section s2
where s1.section_id!=s2.section_id

--exemple inner join
 select * from student st join section se on st.section_id=se.section_id
 --ou
  select * from student st,section se where  st.section_id=se.section_id


  --exemple exept

  select section_id from section except select distinct section_id from professor
--2.6.1

select c.course_name,section_name,professor_name 
from professor as p join section as s on p.section_id=s.section_id
join course as c on p.professor_id =c.professor_id;

--2.6.2

select s.section_id,s.section_name,st.last_name 
from section as s join student as st on s.delegate_id=st.student_id
order by s.section_id desc

--2.6.3
select s.section_id,s.section_name,professor_name 
from section as s left join professor as p on s.section_id=p.section_id
order by s.section_id desc

--2.6.4

select s.section_id,s.section_name,professor_name 
from section as s join professor as p on s.section_id=p.section_id
order by s.section_id desc

--2.6.5

select last_name,year_result,grade
 from student s join grade g
 on s.year_result between g.lower_bound and g.upper_bound
 where Year_result>=12
 order by grade
  --2.6.6
  select p.professor_name, s.section_name,c.course_name,c.course_ects
  from professor p left join section s on p.section_id=s.section_id
  left join course c on P.professor_id =c.professor_id
  order by course_ects desc;

  --2.6.7

  select p.professor_id ,sum(course_ects) as ECTS_TOT
  from course c right join professor p on c.professor_id=p.professor_id
  group by p.professor_id
  order by ECTS_TOT desc;
  
  --2.6.8

  select first_name ,last_name,'S'
  from student 
  where len(last_name)>8
  union
  select professor_surname ,professor_name,'P'
  from professor
  where len(professor_name)>8;

  --2.6.9
  select section_id 
  From section
  except
  select section_id from professor;
  

  --requete imbriqué

  --exemple requete imbrique dans select
  select last_name ,
  first_name, (select section_name 
				from section 
				where section_id=st.section_id)section_name
  from student st

  --exemple  requete au niveau du from
  select last_name ,first_name,section_name
  from (select * from student where section_id like '10%') st
  join (select * from section where section_id like '10%') se on st.section_id=se.section_id
 --exemple requet au niveau du having
 select section_id , avg(year_result)moyenne 
 from student
 group by section_id 
 having avg(year_result)=(
  select max(moyenne)
  from(select avg(year_result)moyenne
  from student group by section_id)moyennes)

  -- avec cte
  go
  with moyennes(section_id, moyenne)as
  (select section_id,avg(year_result)as moyenne
  from student
  group by section_id),
  sections(section_id,[name])as
  (select section_id, section_name
  from section
  where section_id like'10%')
  select s.section_id,moyenne,[name]
  from moyennes m
  left join sections s on m.section_id= s.section_id 
  where moyenne=(select max(moyenne) as moyenne from moyennes)

  --avec corélation

  select last_name, first_name, section_id
  from student st
  where year_result>=(select avg (year_result) 
						from student 
						where section_id=st.section_id)


						--cte pseudo table <> table temporaire
  ---2.7.1
select last_name,first_name,section_id
from student
where section_id = (
	select section_id from student where last_name='Roberts')
and last_name!='roberts'
--2.7.2
select last_name,first_name,year_result
from student 
where year_result > (
select avg(year_result)*2 from student
)
--2.7.3
select section_id,section_name from section
where section_id not in (select section_id from professor)

--2.7.4
select last_name,first_name,convert(varchar,birth_date,101) as [date de naissance],year_result
from student where month(birth_date) =(select month(professor_hire_date) from professor where professor_name='giot') order by year_result desc

--2.7.5
select last_name,first_name ,year_result 
from student where  year_result>=(select lower_bound from grade where grade ='TB') 
					and year_result<=(select upper_bound from grade where grade ='TB')


					--avec with
--2.7.6

select last_name,first_name,section_id
from student 
where section_id in(select section_id 
					from section
					where delegate_id = (select student_id
										from student
										where Last_name='marceau'))

--2.7.7
select section_id,section_name 
from section 
where section_id in(
select section_id from student group by section_id having (count(*)>4))

--2.7.8
select last_name,first_name,section_id
from student s
where year_result = (select max(year_result) from student where section_id =s.section_id)
and section_id not in(select section_id from student group by section_id having avg(year_result)<10)

--2.7.9

with Avgs(section_id,moyenne)as(
	select s.section_id,(select avg(year_result)from student where section_id =s.section_id)as AVG from section s group by s.section_id)
 
select 
(select section_id from student group by section_id having avg(year_result)=max(moyenne))as section_id,
max(moyenne) [AVG] 
from avgs


