Use Aeroport
Go

create Table constructeur (
id int not null identity,
nom nvarchar(100) not null,
constraint UK_typeAvion_nom unique (nom),
constraint PK_constructeur Primary key(id)
);

create Table typeAvion(
id int not null identity,
nom nvarchar(100) not null,
puissance int not null,
nbrPlace smallint not null,
idConstructeur  int not null,
constraint PK_typeAvion primary key (id),
constraint CK_typeAvion_nbrPlace check(nbrPlace>0),
constraint CK_typeAvion_puissance check(puissance>0),
constraint FK_typeAVion_constructeur foreign key (idConstructeur) 
references constructeur (id)
);

create table avion(
imatriculation nvarchar(50) not null,	
idType int not null,
constraint PK_avion primary key (imatriculation),
constraint FK_avion_typeAvion foreign key(idType)
references typeAvion(id)
);
create table personne(
idPersonne int not null identity ,
Nom nvarchar(50)not null,
prenom nvarchar(50) not null,
tel nvarchar (20)not null,
rue nvarchar (300)not null,
numero int not null,
cp int not null,
ville nvarchar (300) not null,
constraint Pk_personne primary key (idPersonne),
constraint Ck_Personne_numero check(numero>0),
constraint Ck_Personne_cp check(cp>0)
);
create table pilote(
idPilote int not null,
numBrevet int not null constraint UK_Pilote_numeroBrevet unique,
constraint Pk_pilote primary key (idPilote),
constraint Fk_pilote_personne foreign key (idPilote)
references personne(idPersonne)
);
create table mecanicien(
idMecanicien int not null,
constraint Pk_mecanicien primary key (idMecanicien),
constraint Fk_mecanicien_personne foreign key (idMecanicien)
references personne(idPersonne)
);
create table Entretien(
idEntretien int not null identity,
objet varchar (1000) not null,
duree int not null ,
[date] date not null  constraint DF_entretien_date Default(GetDate()),
imatriculation nvarchar(50) not null,
idMecanicienRepare int not null,
idMecanicienVerif int not null,
constraint Pk_Entretien primary key (idEntretien),
constraint Ck_entretien_mecano check(idMecanicienRepare!= idMecanicienVerif),
constraint Ck_entretien_duree check(duree>0),
constraint Fk_entretien_mekano_repare foreign key(idMecanicienRepare)
references mecanicien (idMecanicien),
constraint Fk_entretien_mekano_verif foreign key(idMecanicienVerif)
references mecanicien (idMecanicien),
constraint Fk_entretien_avion foreign key(imatriculation)
references avion (imatriculation)

);
create table achat (
imatriculation nvarchar(50) not null,
dateDebut date not null,
idPersonne int not null,
DateFin datetime,
constraint Pk_achat primary key(imatriculation,dateDebut,idPersonne),
constraint Ck_achat_date check(dateFin>dateDebut),
constraint Fk_achat_avion foreign key(imatriculation)
references avion(imatriculation),
constraint FK_achat_personne foreign key (idPersonne)
references personne(idPersonne),
);
create table vol (
id int not null identity,
imatriculation nvarchar(50) not null,
dateDebut datetime2(0) not null,
brevetPilote int not null,
DateFin datetime2(0)
constraint Pk_vol primary key(id),
constraint Ck_vol_date check(dateFin>dateDebut),
constraint Fk_vol_avion foreign key(imatriculation)
references avion(imatriculation),
constraint FK_vol_pilote foreign key (brevetPilote)
references pilote(numBrevet)
);

create table brevetPilotage (
idType int not null,
[date] date not null constraint DF_brevet_date Default(GetDate()),
brevetPilote int not null,

constraint Pk_brevetPilotage primary key(brevetPilote,idType),
constraint Fk_brevetPilotage_type foreign key(idType)
references typeAvion(id),
constraint FK_brevetPilotage_pilote foreign key (brevetPilote)
references pilote(numBrevet),

);
create table habilitation(
[date] date not null constraint DF_habilitation_date Default(GetDate()),
idType int not null,
idmecanicien int not null,
constraint Pk_habilitation primary key(idType,idMecanicien),
constraint Fk_habilitation_type foreign key(idType)
references typeAvion(id),
constraint FK_habilitation_mecanicien foreign key (idmecanicien)
references mecanicien(idmecanicien)
);
drop table habilitation;
drop table brevetpilotage;
drop table vol;
drop table achat;
drop table entretien;
drop table mecanicien;
drop table pilote;
drop table personne;
drop table avion;
drop table typeAvion;
drop table constructeur;
