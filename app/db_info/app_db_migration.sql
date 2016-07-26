CREATE SCHEMA mydwtool;

CREATE TABLE mydwtool.USERS
(
    id  INT,
    nickname VARCHAR(64),
    email VARCHAR(120),
    password VARCHAR(255),
    role VARCHAR(255)
);