
#!/bin/bash

NAME="testHAProxy"
BASEDIR_CONFIG="haproxy"
PORT_ACCES="9090"
PORT_STAT="8404"

docker run \
	-it \
	--rm \
	--name "$NAME" \
	-p "127.0.0.1:$PORT_ACCES:9090/tcp" \
	-p "127.0.0.1:$PORT_STAT:8404/tcp" \
	-v "$PWD/$BASEDIR_CONFIG:/usr/local/etc/haproxy/" \
	haproxy 




