# Constructing the database
Run the following commands to construct the underlying database table structure.

```
CREATE TABLE `media` (
  `id` integer PRIMARY KEY,
  `name` text DEFAULT 'null',
  `owned_since` text DEFAULT 'null',
  `owned_until` text DEFAULT 'null',
  `description` text DEFAULT 'null',
  `type` text DEFAULT 'null',
  `loaned` boolean DEFAULT 'FALSE'
);

CREATE TABLE `employees` (
  `id` integer PRIMARY KEY,
  `name` text DEFAULT 'null',
  `title` text DEFAULT 'null',
  `reports_to` integer 'null',
  `salary` numeric DEFAULT '',
  `salary_currency` text DEFAULT 'SEK',
  `employed_since` text DEFAULT 'null',
  `employed_until` text DEFAULT 'null'
);

CREATE TABLE `users` (
  `id` integer PRIMARY KEY,
  `name` text DEFAULT 'null',
  `user_since` text DEFAULT 'null',
  `user_until` text DEFAULT 'null',
  `email` text DEFAULT 'null',
  `warnings` integer DEFAULT 0
);

CREATE TABLE `loans` (
  `id` integer PRIMARY KEY,
  `media_id` integer DEFAULT 'null',
  `user_id` integer DEFAULT 'null',
  `loan_date` text DEFAULT 'null',
  `return_date` text DEFAULT 'null',
  `due_date` text DEFAULT 'null',
  `resolved` boolean DEFAULT 'FALSE'
);
```