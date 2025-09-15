CREATE TABLE IF NOT EXISTS 'tasks' (id STR PRIMARY KEY, commands STR NOT NULL, priority INT NOT NULL, status STR DEFAULT 'waiting', user STR NOT NULL, response STR DEFAULT NULL);
