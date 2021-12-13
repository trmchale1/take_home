# take_home

## Dockerfile / Task 1

When running the command `docker build --build-arg mode=dev . -t demo/server`, the file will successfully run.

The Dockerfile will download and install `curl`, `wget`, `pip`, the `requirements.txt` file, postgres-13, and Google Cloud SDK

-Python is currently `3.6.9` -> ran into challenges getting the right version

-It attempts to set the environment varaible mode to dev via the build argument

-At the bottom of the file it issues the command `sleep infinity`

-The `COPY . /app` is in the Dockerfile

While it certainly builds without error, I haven't been able to confirm that the last three points were completed correctly.

## docker-compose / Task 2

The `docker-compose.yml` is also running, it declares two services db and web. 

It declares a `.env` file which holds the environment variables used to sign into the database.

-Have not been able to set mode to dev in this file or `LOG LEVEL` to `debug`

-The command `uvicorn main:app --reload` is run at startup

## create-database-and-tables.sh / Task 3

This file runs correctly as well and does create a `store` table on the `demo` database, the column `id` is auto-incremented and `name` is set as `varchar(40)`

This has not yet been set up to run on the webserver

## FastAPI Webserver / Task 4

Leveraged the following tutorial to help me with this [FastAPI tutorial](https://www.tutlinks.com/fastapi-with-postgresql-crud-async/)

The webserver is running, you can tell by running `sudo nmap -n -PN -sT -sU -p- localhost` at the command line, `port 80` is open for the webserver, `port 5432` is open for Postgres. 

However, when using the command below, the database has not updated:

`` curl -X PUT "http://localhost:8000/notes/2/" \
 -H "accept: application/json" \
 -H "Content-Type: application/json" \
 -d "{\"text\":\"test_store\"}" ``
 
 It looks like there is an issue with the webserver, or its connection to the postgres database.
