create database if not exists coder01;

create table if not exists coder01.rooms
(
    roomn  int not null  primary key,
    status tinyint(1) default 0 null,
    type   varchar(20)          null
);

INSERT INTO coder01.rooms (roomn, status, type) VALUES (101, 0, 'suit');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (102, 0, 'suit');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (103, 0, 'suit');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (104, 0, 'suit');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (105, 0, 'suit');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (201, 0, 'executive');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (202, 0, 'executive');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (203, 0, 'executive');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (204, 0, 'executive');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (205, 0, 'executive');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (301, 0, 'single deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (302, 0, 'single deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (303, 0, 'single deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (304, 0, 'single deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (305, 0, 'single deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (401, 0, 'double deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (402, 0, 'double deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (403, 0, 'double deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (404, 0, 'double deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (405, 0, 'double deluxe');

create table if not exists hotelbookings
(
    bookingID int auto_increment primary key,
    name      varchar(20)  null,
    surname   varchar(20)  null,
    email     varchar(30)  null,
    address   varchar(100) null,
    mobile    bigint       null,
    roomno    int          null,
    meal      varchar(10)  null,
    cin       date         null,
    cout      date         null,
    foreign key (roomno) references rooms (roomn)
);

