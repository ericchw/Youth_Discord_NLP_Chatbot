-- ####################################################
-- # brew install --cask pgadmin4
-- # brew install postgresql  (version: PostgreSQL@14)
-- # brew services start postgresql
-- ####################################################
-- Role: admin
-- DROP ROLE IF EXISTS admin;
-- CREATE ROLE admin WITH LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE REPLICATION ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:FRd+bOnm+iKG8lhJCv4fsw==$qwIDoBcBSU6xBNZNWvKW8IC5zQehD1DIH74OQ/g2Q+U=:alCpVnY1bfriBlR9eXGE2pnZbwPlAdrnj+SMSStbCfQ=';

-- -- Database: sjs
-- -- DROP DATABASE IF EXISTS sjs;
-- CREATE DATABASE sjs WITH OWNER = admin ENCODING = 'UTF8' LC_COLLATE = 'C' LC_CTYPE = 'C' TABLESPACE = pg_default CONNECTION
-- LIMIT = -1 IS_TEMPLATE = False;

--####################################################
DROP TABLE account;

DROP TABLE chatlog;

DROP TABLE helplog;

-- DROP TABLE games;

DROP TABLE information;

-- DROP TABLE event_detail;

-- DROP TABLE event_header;

DROP TABLE polling;

DROP TABLE event;

DROP TABLE activity;

CREATE TABLE account (
    id SERIAL PRIMARY KEY,
    email VARCHAR,
    pwd VARCHAR,
    username VARCHAR
);

CREATE TABLE chatlog (
    id SERIAL PRIMARY KEY,
    senderName VARCHAR,
    senderId VARCHAR,
    message VARCHAR,
    label VARCHAR,
    labelFlag integer, -- Each 10 times, send a DC PM message to user
    timestamp TIMESTAMP
);

CREATE TABLE helplog (
    id SERIAL PRIMARY KEY,
    userName VARCHAR,
    userId VARCHAR,
    needHelp boolean, -- Yes/Not, default null
    timestamp TIMESTAMP
);

CREATE TABLE botlog (
    id SERIAL PRIMARY KEY,
    message VARCHAR,
    timestamp TIMESTAMP
);

CREATE TABLE information (
    name VARCHAR PRIMARY KEY,
    phoneNumber VARCHAR,
    whatsapp VARCHAR,
    website VARCHAR,
    instagram VARCHAR,
    discord VARCHAR,
    servicehours VARCHAR
);

CREATE TABLE Activity (
    ATYId SERIAL PRIMARY KEY,
    ATYName VARCHAR,
    ATYCreateDate TIMESTAMP,
    ATYUpdateDate TIMESTAMP
);

CREATE TABLE Event (
    EVTId SERIAL PRIMARY KEY,
	ATYId SERIAL,
    EVTTitle VARCHAR,
    EVTLimitMem int,
    EVTDesc VARCHAR,
    EVTDate TIMESTAMP,
    EVTdeadline TIMESTAMP,
    EVTCreateDate TIMESTAMP,
    EVTUpdateDate TIMESTAMP,
	CONSTRAINT fk_Event FOREIGN KEY (ATYId) REFERENCES Activity(ATYId)
);

CREATE TABLE Polling (
    POLLId SERIAL PRIMARY KEY,
    EVTId SERIAL,
    POLLDCId VARCHAR,
    POLLDCUsername VARCHAR,
    POLLStatus varchar, -- Applying, Accepted, Rejected
    POLLCreateDate TIMESTAMP,
    POLLUpdateDate TIMESTAMP,
	CONSTRAINT fk_Polling FOREIGN KEY (EVTId) REFERENCES Event(EVTId)
);

INSERT INTO
    account(email, pwd, username)
VALUES
    (
        '1234@gmail.com',
        MD5('1234'),
        'Ken'
    );


INSERT INTO
    information
VALUES
    (
        '聖雅各福群會6PM網上青年支援隊',
        '26093228',
        '59333711',
        'https://www.cyberyouth.sjs.org.hk/',
        'https://www.instagram.com/6pm.hk/',
        'https://discord.gg/6pm',
        'https://cdn.discordapp.com/attachments/709787197385080852/933897809076314132/5ee1ae88efa3e739.png'
    );