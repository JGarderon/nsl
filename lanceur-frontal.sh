#!/bin/bash

RACINE="/home/julien/Projets/nothus-serverless"

NOM="nothus-frontal"

rm "$RACINE/nginx-logs/access.log" 
rm "$RACINE/nginx-logs/error.log" 

DID=`docker run \
	-d \
	-v "$RACINE/nginx-conf/:/etc/nginx/conf.d" \
	-v "$RACINE/nginx-scripts/:/app" \
	-v "$RACINE/nginx-static/:/var/www" \
	-v "$RACINE/nginx-logs/:/usr/local/openresty/nginx/logs/" \
	-p 50000:80 \
	--name "$NOM" \
	openresty/openresty` 

echo "conteneur 'frontal' : $DID via http://localhost:50000" 

curl http://127.0.0.1:50000/lua

docker stop nothus-frontal 

docker container rm nothus-frontal

# docker stop "$DID"


