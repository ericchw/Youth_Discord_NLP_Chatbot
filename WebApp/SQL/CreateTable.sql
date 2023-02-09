--DROP TABLE IF EXISTS Account;
--DROP TABLE IF EXISTS Event_Header;
--DROP TABLE IF EXISTS Event_Detail;
--DROP TABLE IF EXISTS chatlog;
--DROP TABLE IF EXISTS games;
--DROP TABLE IF EXISTS information;

CREATE TABLE IF NOT EXISTS information
(
    name character varying COLLATE pg_catalog."default",
    phonenumber character varying COLLATE pg_catalog."default",
    whatsapp character varying COLLATE pg_catalog."default",
    countrycode character(3) COLLATE pg_catalog."default",
    website character varying COLLATE pg_catalog."default",
    instagram character varying COLLATE pg_catalog."default",
    discord character varying COLLATE pg_catalog."default",
    servicehours character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS information
    OWNER to postgres;
	
-------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS games
(
    id SERIAL PRIMARY KEY,
    name character varying COLLATE pg_catalog."default",
    name_zh character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS games
    OWNER to postgres;

-------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS chatlog
(
    id SERIAL PRIMARY KEY,
    userid character varying COLLATE pg_catalog."default",
    message character varying COLLATE pg_catalog."default",
    label character varying COLLATE pg_catalog."default",
    timestamptz timestamp with time zone
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS chatlog
    OWNER to postgres;
	
-------------------------------------------------------------------------------------
CREATE TABLE Account(
	aid int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	email varchar,
	pwd varchar,
	username varchar
);

-------------------------------------------------------------------------------------

CREATE TABLE Event_Header(
	eHdrId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	eHdrTitle varchar,
	eStatus varchar,
	eHdrDesc varchar,
	eHdrDate timestamp,
	eHdrCreateDate timestamp
);

-------------------------------------------------------------------------------------

CREATE TABLE Event_Detail(
	eDtlId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    eGameId SERIAL,
	eDtlHdrId int,
    CONSTRAINT fk_EventDetail_GameId FOREIGN KEY (eGameId) REFERENCES Games(id),
    CONSTRAINT fk_EventDetail_HdrId FOREIGN KEY (eDtlHdrId) REFERENCES Event_Header(eHdrId)
);

-------------------------------------------------------------------------------------

select * from account;

select * from games;

select * from Event_Header;

select * from Event_Detail;

SELECT * FROM Event_Detail left join Games 
on Event_Detail.eGameId = Games.id
where eDtlHdrId = 2


SELECT * FROM Event_Header left join Event_Detail
ON Event_Header.eHdrId = Event_Detail.eDtlHdrId where eHdrId = '1'

SELECT * FROM Event_Header left join Event_Detail
ON Event_Header.eHdrId = Event_Detail.eDtlHdrId where eHdrId = '2'

