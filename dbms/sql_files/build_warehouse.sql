CREATE TABLE IF NOT EXISTS 'media' (
  'id' TEXT PRIMARY KEY,
  'name' TEXT DEFAULT 'null',
  'owned_since' TEXT DEFAULT 'null',
  'owned_until' TEXT DEFAULT 'null',
  'description' TEXT DEFAULT 'null',
  'author_id' INTEGER DEFAULT 'null',
  'type' TEXT DEFAULT 'null',
  'loaned' BOOLEAN DEFAULT 'FALSE'
);

CREATE TABLE IF NOT EXISTS 'authors' (
  'id' TEXT PRIMARY KEY,
  'name' TEXT DEFAULT 'null',
  'dob' TEXT DEFAULT 'null',
  'dod' TEXT DEFAULT 'null'
);

CREATE TABLE IF NOT EXISTS 'employees' (
  'id' TEXT PRIMARY KEY,
  'name' TEXT DEFAULT 'null',
  'title' TEXT DEFAULT 'null',
  'reports_to' INTEGER 'null',
  'salary' numeric DEFAULT '',
  'salary_currency' TEXT DEFAULT 'SEK',
  'employed_since' TEXT DEFAULT 'null',
  'employed_until' TEXT DEFAULT 'null'
);

CREATE TABLE IF NOT EXISTS 'users' (
  'id' TEXT PRIMARY KEY,
  'name' TEXT DEFAULT 'null',
  'user_since' TEXT DEFAULT 'null',
  'user_until' TEXT DEFAULT 'null',
  'email' TEXT DEFAULT 'null',
  'warnings' INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS 'loans' (
  'id' TEXT PRIMARY KEY,
  'media_id' INTEGER DEFAULT 'null',
  'user_id' INTEGER DEFAULT 'null',
  'loan_date' TEXT DEFAULT 'null',
  'return_date' TEXT DEFAULT 'null',
  'due_date' TEXT DEFAULT 'null',
  'employee_id' INTEGER DEFAULT 'null',
  'resolved' BOOLEAN DEFAULT 'FALSE'
);



