# LibbyDB
LibbyDB is a case project, based on a fictional library. This project was born out the authors' desire to practice SQL querying, as well as Data Warehouse and UI design. The setting of a fictional library was selected because it seemed like an interesting challenge to the authors.

## Fictional library Setting
In this project, we consider a fictional library, called "Shelfville Library". It has two locations in the city of Shelfville. There are three librarian employees working each location, and a "Library manager", Page Gutenberg, working from an office in Shelfville City Hall. The library holds 1000 books, distributed across the two locations: "South Shelfville library" and "North Shelfville library". Currently, books are kept track of in three excel documents: one global, and one for each of the locations. They each contain a record for each *title*, with a column indicating how many books of that title are available. The main one is updated by Page Gutenberg, and the others are manually updated locally.

Recently, the city decided to drastically expand the budget of the library over the coming 10 years, due to an expected population boom in Shelfville. Following this, Library manager Page Gutenberg outlined the following goals:

* Drastically expand the total library volume, from 1.000 to 20.000 books. This will be accomplished by acquiring approximately 200 new books monthly.
* Acquire various kinds of media beyond books, such as CD's, comics, newspapers.
* Open two more locations.
* Modernize the transfer between locations.
* Hire up to 20 additional librarians to meet new tasks, such as media sourcer, stocker, etc.

## Broad Project Requirements
Based on the library setting, we will design an overarching system with the following major components:

* **The Operational System** consists of 
    1) A gui that allows operational users (library clerks, managers) to add new instances, such as media, employees, loans, etc, and edit existing instances. These instances are stored in a buffer in order to avoid interrupting the central data storage continually, and to avoid the operational users having to wait because of latency.

    2) A buffer database file, used to store new instances before they can be processed by the Data Warehouse DBMS. This file should have broadly the same structure as the Data Warehouse datbase file.

    3) A library user gui that allows users to loan and return media.

* **The Data Warehouse** *"Bibliotheca intra Bibliothecam"* consists of
    1) A DBMS, a constantly running administrative process that handles requests and responds to events like database file corruption (backups). This process makes the data warehouse available to the data analysts.

    2) A database file, used to store the data.

* **The Backup-Server** consists of
    1) A DBMS, a constantly running process that has two main responsibilities. One is to accept new versions of the Data Warehouse database file and store for backup. The other is to provide this backup back to the Data Warehouse DBMS when requested.
    
    2) A most recent database file backup copy.

* **The Developer Server** consists of
    1) A CLI that can be used by developers during development. It should be able to re-generate the two database versions mentioned below on command.

    2) A developer version of the Data Warehouse database file. This is just a small version with few instances, maybe even with masked values.

    3) A test version of the Data Warehouse database, that is equally or almost as large. It can be used for testing out new features in a production-like setting.

## UX
User interaction with this whole system will be based on four entrypoints.

* **Operational System Users** A cli or ideally gui that is part of The operational system, that can be used to enter or edit records. All new records through this port of entry are stored in a separate database file, so that they can gradually be sent to the data warehouse when it has downtime. They should all be considered low priority from the DBMS.

* **Library Users** A library user gui that allows users to loan and return media. Should be considered low priority from the DBMS.

* **Data Warehouse Administrators** A cli that is part of the data warehouse. It can accept commands that instruct the DBMS to perform major changes of the data warehouse. All these commands should be stored in a database so that they may be evaluated when possible, but they should be given medium priority.

* **Business Analyst Users** A gui that allows business analysts to easily and quickly extract information from the data warehouse. Commands from this gui should be read-only.



<!-- 
OLD DESCRIPTIONS BELOW





## Fictional Project Requirements
In order to facilitate development, the following project requirements were formulated at the beginning of the project, as if formulated by the (fictional) client.

* The database must be able to store user information, such as name, contact information and possibly an infraction count, such as 'the number of missed return dates'.

* The database must be able to store media informaton for the collection of the library. Media may be books, films, comics, cd's etc. Each media entry should contain information like name, description, publication date, date when obtained (by the library), date when the media left the collection (if applicable), an indicator of whether the media is currently loaned.

* The databse should hold employee information such as name, salary, title, who the employee reports too, what library location they work at (if applicable).

* In case the library expands across multiple locations, the datbase must be able to store information on which location each media is stored at, as well as where in the library the media is located.

* The DBMS must have friendly UI that employees can use to log new entries in the database. The UI should also be able to query the database for entries, such as overdue media, users etc.

## Project Features
The database currently satisfies most of the features to some extent. Below is an Entity Relationship (ER) diagram that represents the database entities and their relationships.

<img src="db_design/ER_diagram.png" alt="ER diagram" width="900"/>

* LibbyDB is executable, and can be run in the following way, opening either the CLI or GUI. Default mode is "cli". The GUI can also be opened in the CLI.

`python -m libbydb`

`python -m libbydb -mode gui`

* LibbyDB can also be run with the following command:

`YOUR/PATH/HERE/LibbyDB/main.py` -->