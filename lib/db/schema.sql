CREATE TABLE IF NOT EXISTS teams (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL UNIQUE,
country TEXT 
);

CREATE TABLE IF NOT EXISTS drivers (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
nationality TEXT 
);

CREATE TABLE IF NOT EXISTS races (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
location TEXT,
date DATABASE
);

--Race results table
CREATE TABLE IF NOT EXISTS results (
id INTEGER PRIMARY KEY,
driver_id INTEGER,
team_id INTEGER,
race_id INTEGER,
position INTEGER,
points REAL,
FOREIGN KEY (driver_id) REFERENCES drivers(id),
FOREIGN KEY (team_id) REFERENCES teams(id),
FOREIGN KEY (race_id) REFERENCES races(id)
);
 