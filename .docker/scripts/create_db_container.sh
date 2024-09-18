#!/bin/bash
# Script executed after variables substitution:
# .docker run --name chatbot -e POSTGRES_USER=admin -e POSTGRES_DB=chatbot -e POSTGRES_PASSWORD=vO9_opN2bONgWApvVzNS -v chatbot_db_data:/var/lib/postgresql/data -p 5432:5432 -d postgres:16.3

CONTAINER_NAME=$1
PG_USER=$2
PG_DB=$3
PG_PWD=$4
PG_VOLUME=$5
PORTS=$6
IMAGE=$7

docker run --name $CONTAINER_NAME -e POSTGRES_USER=$PG_USER -e POSTGRES_DB=$PG_DB -e POSTGRES_PASSWORD=$PG_PWD -v $PG_VOLUME -p $PORTS -d $IMAGE
