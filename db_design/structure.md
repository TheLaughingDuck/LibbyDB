# Database structure
LibbyDB, the database management system, was designed to be generic and useable by practically any library. The database schema is represented here below as an ER diagram, which illustrates the different tables in the database, and their internal relationships. After that follows an explanation of the variables.

![alt text](ER_diagram.png)

## media
The media table lists various forms of media, such as books, films, etc. It consists of the following variables:

* **id**: The primary key, unique to each piece of media.
* **name**: The name, or title, of the media, for example "There and back again".
* **owned_since**: The date when the media was obtained by the library, in a text string, format "YYYY-MM-DD".
* **owned_until**: The date when the library was considered no longer in posession of the media, for example if sold to another library, or lost by a user.
* **description**: A short textual description of the media.
* **type**: The media type as a string, one of "book", "film", "cd".
* **loaned**: Boolean indicating whether the media is currently loaned by a user.

## authors
...

## employees
...

## users
...

## loans
...

## warrants
...

# Practical details
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

CREATE TABLE `authors` (
  `id` integer PRIMARY KEY,
  `name` text DEFAULT 'null',
  `dob` text DEFAULT 'null',
  `dod` text DEFAULT 'null',
  `warnings` integer DEFAULT 0
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

CREATE TABLE `warrants` (
  `id` integer PRIMARY KEY,
  `media_id` integer DEFAULT 'null',
  `user_id` integer DEFAULT 'null'
  `employee_id` integer DEFAULT 'null',
  `resolved` boolean DEFAULT 'FALSE'
);
```