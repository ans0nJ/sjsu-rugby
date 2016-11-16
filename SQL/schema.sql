DROP TABLE IF EXISTS roster;
CREATE TABLE roster (
	Name varchar(255) primary key,
	Position varchar(255),
	Height varchar(255),
	Weight varchar(255),
	Year varchar(255),
	Hometown varchar(255)
);
DROP TABLE IF EXISTS schedule;
CREATE TABLE schedule (
	Date varchar(255),
	Team varchar(255),
	Location varchar(255),
	Time varchar(255),
	Score varchar(255)
);
DROP TABLE IF EXISTS contact;
CREATE TABLE contact (
	Name varchar(255) primary key,
	Position varchar(255),
	Email varchar(255),
	Phone varchar(255)
);

