#!bin/bash
set PGPASSWORD=$POSTGRES_PASSWORD
psql -h localhost -p 5432 -d $POSTGRES_DB -U $POSTGRES_USER << EOF
	CREATE DATABASE demo;
	CREATE TABLE stores(
		id SERIAL PRIMARY KEY,
		name varchar(40) NOT NULL
	);
EOF
