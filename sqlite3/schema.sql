DROP TABLE IF EXISTS roster;
CREATE TABLE roster (
	Name text primary key,
	Position text,
	Height text,
	Weight text,
	Year text,
	Hometown text
);
DROP TABLE IF EXISTS schedule;
CREATE TABLE schedule (
	Date text,
	Team text,
	Location text,
	Time text,
	Score text
);
DROP TABLE IF EXISTS contact;
CREATE TABLE contact (
	Name text primary key,
	Position text,
	Email text,
	Phone text
);
DROP TABLE IF EXISTS coaches;
CREATE TABLE coaches (
	Name text primary key,
	Position text,
	Year text
);
