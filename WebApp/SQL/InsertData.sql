INSERT INTO account(email, pwd, username) VALUES ('1234@gmail.com', '1234', 'Ken');

INSERT INTO Event_Header(eHdrTitle, eStatus, eHdrDesc, eHdrDate, eHdrCreateDate) VALUES 
('Hiking everyday', 'Finished', 'Let''s hiking', CURRENT_DATE, CURRENT_TIMESTAMP);

INSERT INTO Event_Header(eHdrTitle, eStatus, eHdrDesc, eHdrDate, eHdrCreateDate) VALUES 
('Playing everyday', 'Start', 'Let''s play the game', CURRENT_DATE, CURRENT_TIMESTAMP);

--Game--
-------------------------------------------------------------------------------

INSERT INTO Games(name, name_zh) VALUES ('League of Legends', '英雄聯盟');
INSERT INTO Games(name, name_zh) VALUES ('Apex Leagues', 'Apex 英雄');
INSERT INTO Games(name, name_zh) VALUES ('Fall Guys', '糖豆人');
INSERT INTO Games(name, name_zh) VALUES ('PUBG: Battlegrounds', '絕地求生');
INSERT INTO Games(name, name_zh) VALUES ('PUBG MOBILE', '絕地求生M');
INSERT INTO Games(name, name_zh) VALUES ('Brawlhalla', '英靈神殿大亂鬥');
INSERT INTO Games(name, name_zh) VALUES ('Talesrunner', '跑Online');
INSERT INTO Games(name, name_zh) VALUES ('Among Us', '太空狼人殺');
INSERT INTO Games(name, name_zh) VALUES ('Rummikub', '魔力橋');
INSERT INTO Games(name, name_zh) VALUES ('Board Game Arena', '桌遊競技場');
INSERT INTO Games(name, name_zh) VALUES ('Arena of Valor', '傳說對決');
INSERT INTO Games(name, name_zh) VALUES ('Honor of Kings', '王者榮耀');
INSERT INTO Games(name, name_zh) VALUES ('Other', '其他');

INSERT INTO Event_Detail (egameid, edtlhdrid) values ('1', '2');
INSERT INTO Event_Detail (egameid, edtlhdrid) values ('2', '2');

select * from games

select * from Event_Header