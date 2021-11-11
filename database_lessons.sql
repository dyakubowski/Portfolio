create database lessons_for_students;
use lessons_for_students;
create table students (
studentsID int auto_increment primary key,
first_name varchar(15),
last_name varchar(15)
);
create table groups_ (
groupID int auto_increment primary key,
number_group mediumint);
create table day_lessons (
day_ID tinyint auto_increment primary key,
day_name varchar(10)
);
create table lessons (
day_ID tinyint,
groupID int primary key,
lessons text,
foreign key (day_ID) references day_lessons(day_ID),
foreign key (groupID) references groups_(groupID)
);
create table groups_students(
studentsID int,
groupID int,
foreign key (studentsID) references students(studentsID),
foreign key (groupID) references lessons(groupID)
);
insert into students (first_name, last_name) values('', '');
insert into groups_ (number_group) values('');
insert into day_lessons (day_name) values('');
insert into lessons (day_ID, groupID, lessons) values();
insert into groups_students(studentsID, groupID) values();
