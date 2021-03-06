-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE players ( name TEXT,
					   id SERIAL primary key);

CREATE TABLE matches ( winner INTEGER references players(id),
					   loser INTEGER references players(id),
					   id SERIAL primary key);

