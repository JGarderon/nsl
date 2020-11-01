#!/bin/bash

RACINE="/home/julien/Projets/nothus-serverless"

PORT="5984"

DID=`docker run \
	--rm \
	-e COUCHDB_USER=admin \
	-e COUCHDB_PASSWORD=password \
	-v "$RACINE/couchdb-datas:/opt/couchdb/data" \
	-d \
	-p "$PORT:5984" \
	couchdb`


echo "conteneur 'db' : $DID via http://localhost:$PORT" 


