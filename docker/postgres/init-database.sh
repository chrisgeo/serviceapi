#!/bin/bash
gosu postgres pg_ctl -w start
gosu postgres psql -d template1 -c "CREATE EXTENSION IF NOT EXISTS hstore;"
gosu postgres pg_ctl -w stop

echo "******CREATING $DATABASE DATABASE******"
gosu postgres postgres --single <<- EOSQL
   CREATE DATABASE $DATABASE;
   CREATE USER $DATABASE_USER;
   GRANT ALL PRIVILEGES ON DATABASE $DATABASE to $DATABASE_USER;
EOSQL
echo ""
echo "******$DATABASE DATABASE CREATED******"
