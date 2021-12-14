#!bin/bash
psql -h localhost -p 5432 -d demo -U demouser << EOF
	CREATE TABLE store(
		id SERIAL PRIMARY KEY,
		name varchar(40) NOT NULL
	);
EOF
