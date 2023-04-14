DROP TABLE IF EXISTS account;
DROP TABLE IF EXISTS polling;
DROP TABLE IF EXISTS event;
DROP TABLE IF EXISTS activity;
DROP TABLE IF EXISTS chatlog;
DROP TABLE IF EXISTS helplog;
DROP TABLE IF EXISTS botlog;
DROP TABLE IF EXISTS information;
        
CREATE TABLE IF NOT EXISTS account (
    id SERIAL PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    pwd VARCHAR NOT NULL,
    username VARCHAR UNIQUE NOT NULL
);

INSERT INTO
    account(email, pwd, username)
VALUES
    (   
        '1234@gmail.com',
        MD5('1234'),
        'Ken'
    )
ON CONFLICT DO NOTHING;

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
    EVTdeadline TIMESTAMP,
    EVTCreateDate TIMESTAMP,
    EVTUpdateDate TIMESTAMP,
    CONSTRAINT fk_Event FOREIGN KEY (ATYId) REFERENCES Activity(ATYId)
);

CREATE TABLE IF NOT EXISTS Polling (
    POLLId SERIAL PRIMARY KEY,
    EVTId SERIAL,
    POLLDCId VARCHAR,
    POLLDCUsername VARCHAR,
    POLLStatus varchar, -- Applying, Accepted, Rejected
    POLLCreateDate TIMESTAMP,
    POLLUpdateDate TIMESTAMP,
    CONSTRAINT fk_Polling FOREIGN KEY (EVTId) REFERENCES Event(EVTId)
);

CREATE TABLE IF NOT EXISTS chatlog (
    id SERIAL PRIMARY KEY,
    senderName VARCHAR,
    senderId VARCHAR,
    message VARCHAR,
    label VARCHAR,
    labelFlag integer, -- Each 10 times, send a DC PM message to user
    timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS helplog (
    id SERIAL PRIMARY KEY,
    userName VARCHAR,
    userId VARCHAR,
    needHelp boolean, -- Yes/Not, default null
    timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS botlog (
    id SERIAL PRIMARY KEY,
    message VARCHAR,
    timestamp TIMESTAMP
);


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
    )
ON CONFLICT DO NOTHING;

-----------------------------------------------

-- DROP TABLE games IF EXISTS;

-- CREATE TABLE IF NOT EXISTS games (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR,
--     name_zh VARCHAR
-- );

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