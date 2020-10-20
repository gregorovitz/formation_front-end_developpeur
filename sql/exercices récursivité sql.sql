CREATE TABLE dbo.Employe
(
Id INT NOT NULL,
Nom NVARCHAR(50)  NOT NULL,
Prenom NVARCHAR(50) NOT NULL,   
ManagerId INT NULL,
CONSTRAINT PK_Employe PRIMARY KEY (Id),
CONSTRAINT FK_Employe_Employe FOREIGN KEY (ManagerId) REFERENCES Employe(Id)
);

-- Populate the table with values.
INSERT INTO dbo.Employe (Id, Nom, Prenom, ManagerId) VALUES  
 (1, N'Norris', N'Chuck', NULL)
,(273, N'Paltrow', N'Gwyneth',1)
,(274, N'Willis', N'Bruce',273)
,(275, N'Reynolds', N'Ryan',274)
,(276, N'Downey', N'Robert',274)
,(285, N'Johansson', N'Scarlett',273)
,(286, N'Jackson', N'Samuel L.',285)
,(16,  N'Ruffalo',N'Mark', 273)


with [directReport]( [id],[nom],[Prenom],[level] )as(
--definition point de départ
select e.id,e.prenom,e.nom,1 as[level]
from Employe as e
where ManagerId is null
union all
--definition de la récursivité va jusqu'a la fin du union all et ensuite quand il a trouver la derniere ligne revient 
-- en mettant les précédente du fait pas de doublons
select e.id,e.prenom,e.nom,[Level] + 1
from Employe as e
inner join directReport as d
on  e.ManagerId=d.id)
--recupére les donné a affiché dans drectreport
select prenom + ' '+nom as nom, 'rang ' +convert(varchar(10),Level)as rang
from directReport
order by rang


select em.nom +' '+ em.prenom as nom, 'rang 1'
from employe as em join employe e on em.id =e.managerid where em.managerId is Null
union
