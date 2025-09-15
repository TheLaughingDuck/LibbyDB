# LibbyDB
LibbyDB is a case project, based on a fictional library. This project was born out the desire to practice SQL querying, as well as Data Warehouse and UI design. The setting of a fictional library was selected because it seemed like an interesting challenge.

## Current Project Stage
This project is currently in the beginning and planning stage. See progress.md for the current progress.

## Background
In this project, we consider a fictional National Library. It has multiple locations spread across various cities, and lots of employees working at invididual libraries as well as on a larger administrative level.

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


