# Current progress
Here we detail the current progress and what has been begun and completed.

The technical development occurs under dbms/.

# How to use
This is how you can use this system as of now.

1) Open a terminal window, cd into \LibbyDB, run dbms\wh_server.py
2) Manually run dev_server.py in a different terminal, and observe how a task is stored in the wh_task_queue.sqlite file, and then executed on the warehouse.sqlite file by wh_server.py

## **The Operational System** 
- [x] Employee CLI
- [ ] Employee GUI
- [ ] Buffer data warehouse file
- [ ] Loaner GUI

## **The Data Warehouse**
- [x] Warehouse admin server (exists: wh_server.py)
- [x] Data warehouse file (exists: warehouse.sqlite)

## **The Backup-Server**
- [ ] Backup server
- [ ] Database backup file

## **The Developer Server**
- [x] Developer CLI (exists: dev_server.py)
- [ ] Data warehouse developer version
- [ ] Data warehouse test version


# Roadmap
Top priority is constructing the foundational database file, with the necessary tables and columns.

We could build to quickly have something working. Then we would start on the developer CLI and Employee CLI/GUI. We would let them issue commands directly to the datawarehouse/database. 

We could also build to have something robust that will be able to handle many concurrent requests from developers as well as library employees. This will take longer time before we have a working example. Doing this, I would like to define specific custom operations.

We can also try to achieve a balance between the two, where there is an admin server that controls access to the data warehouse, but as a start, we just make it process SQL tasks, without anything more complicated. I will do this.
