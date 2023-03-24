-- Test bot:
-- hi
-- Hello
-- 極度憤怒
-- 聯絡
-- 我的狗剛剛去世
-- ####################################################
-- # brew install --cask pgadmin4
-- # brew install postgresql  (version: PostgreSQL@14)
-- # brew services start postgresql
-- ####################################################
-- Role: admin
-- DROP ROLE IF EXISTS admin;
-- CREATE ROLE admin WITH LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE REPLICATION ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:FRd+bOnm+iKG8lhJCv4fsw==$qwIDoBcBSU6xBNZNWvKW8IC5zQehD1DIH74OQ/g2Q+U=:alCpVnY1bfriBlR9eXGE2pnZbwPlAdrnj+SMSStbCfQ=';

-- Database: sjs
-- DROP DATABASE IF EXISTS sjs;
-- CREATE DATABASE sjs WITH OWNER = admin ENCODING = 'UTF8' LC_COLLATE = 'C' LC_CTYPE = 'C' TABLESPACE = pg_default CONNECTION
-- LIMIT = -1 IS_TEMPLATE = False;

--####################################################
-- DROP TABLE account IF EXISTS;

-- DROP TABLE chatlog IF EXISTS;

-- DROP TABLE helplog IF EXISTS;

-- DROP TABLE games IF EXISTS;

-- DROP TABLE information IF EXISTS;

-- DROP TABLE event_detail;

-- DROP TABLE event_header;

-- DROP TABLE activity;

CREATE TABLE IF NOT EXISTS account (
    id SERIAL PRIMARY KEY,
    email VARCHAR,
    pwd VARCHAR,
    username VARCHAR
);

CREATE TABLE IF NOT EXISTS chatlog (
    id SERIAL PRIMARY KEY,
    senderName VARCHAR,
    senderId VARCHAR,
    message VARCHAR,
    label VARCHAR,
    timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS helplog (
    id SERIAL PRIMARY KEY,
    userName VARCHAR,
    userId VARCHAR,
    timestamp TIMESTAMP
);

-- CREATE TABLE IF NOT EXISTS games (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR,
--     name_zh VARCHAR
-- );

CREATE TABLE IF NOT EXISTS information (
    name VARCHAR PRIMARY KEY,
    phoneNumber VARCHAR,
    whatsapp VARCHAR,
    website VARCHAR,
    instagram VARCHAR,
    discord VARCHAR,
    servicehours VARCHAR
);

INSERT INTO
    account(email, pwd, username)
VALUES
    (
        '1234@gmail.com',
        MD5('1234'),
        'Ken'
    );

-- select * from account

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

-- INSERT INTO games VALUES
-- 	(1, 'Other', '其他'),
-- 	(2, 'League of Legends', '英雄聯盟'),
-- 	(3, 'Apex Leagues', 'Apex 英雄'),
-- 	(4, 'Fall Guys', '糖豆人'),
-- 	(5, 'PUBG: Battlegrounds', '絕地求生'),
-- 	(6, 'PUBG MOBILE', '絕地求生M'),
-- 	(7, 'Brawlhalla', '英靈神殿大亂鬥'),
-- 	(8, 'Talesrunner', '跑Online'),
-- 	(9, 'Among Us', '太空狼人殺'),
-- 	(10, 'Rummikub', '魔力橋'),
-- 	(11, 'Board Game Arena', '桌遊競技場'),
-- 	(12, 'Arena of Valor', '傳說對決'),
-- 	(13, 'Honor of Kings', '王者榮耀')
-- ;

CREATE TABLE IF NOT EXISTS Activity (
    ATYId SERIAL PRIMARY KEY,
    ATYName VARCHAR,
    ATYCreateDate TIMESTAMP,
    ATYUpdateDate TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Event(
    EVTId SERIAL PRIMARY KEY,
	ATYId SERIAL,
    EVTTitle VARCHAR,
    EVTLimitMem int,
    EVTDesc VARCHAR,
    EVTDate TIMESTAMP,
    EVTCreateDate TIMESTAMP,
    EVTUpdateDate TIMESTAMP,
	CONSTRAINT fk_Event FOREIGN KEY (ATYId) REFERENCES Activity(ATYId)
);

-- CREATE TABLE IF NOT EXISTS Event_Detail(
--     eDtlId SERIAL PRIMARY KEY,
--     eDtlHdrId INTEGER,
--     eDtlGameId INTEGER,
--     CONSTRAINT fk_EventDetail FOREIGN KEY (eDtlHdrId) REFERENCES Event_Header(eHdrId)
-- );

CREATE TABLE IF NOT EXISTS Polling(
    POLLId SERIAL PRIMARY KEY,
    EVTId SERIAL,
    POLLDCId VARCHAR,
    POLLDCUsername VARCHAR,
    POLLCreateDate TIMESTAMP,
    POLLUpdateDate TIMESTAMP,
	CONSTRAINT fk_Polling FOREIGN KEY (EVTId) REFERENCES Event(EVTId)
);

-- select * from account