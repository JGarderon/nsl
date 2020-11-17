
#!/bin/bash

SCRIPT="default.py"
VERSION="3.9-slim"
NAME=""
BASEDIR="myapp"
DEBUG="no"
PEER="127.0.0.1:9999"
HOSTNAME="$(uname -n)"
SCRIPTPATH="/usr/src"

help() { echo "
---------------------------------------------------------------------------
  Create a container for Python's script (simple FAAS) 
---------------------------------------------------------------------------
"

printf "%3s : %10s      # %s\n" "-s" "\$SCRIPT" "name of script (path)" 
printf "%3s : %10s      # %s\n" "-v" "\$VERSION" "version of Python" 
printf "%3s : %10s      # %s\n" "-n" "\$NAME" "unique name of container (* must set)" 
printf "%3s : %10s      # %s\n" "-b" "\$BASEDIR" "name of basedir" 
printf "%3s : %10s      # %s\n" "-p" "\$PEER" "IP:Port to the listener" 
printf "%3s : %10s      # %s\n" "-d" "\$DEBUG" "debug (on stdout)" 

echo "
---------------------------------------------------------------------------
" 
}

while getopts "hs:v:n:b:d" opt; do 
  case $opt in
    s) SCRIPT="$OPTARG"
    ;;
    v) VERSION="$OPTARG"
    ;;
    n) NAME="$OPTARG"
    ;;
    b) BASEDIR="$OPTARG"
    ;;
    b) PEER="$OPTARG"
    ;;
    h) help ; exit 0
    ;;
    d) DEBUG="yes"
	;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

debug() { 
	if [ "$DEBUG" = "yes" ] 
	then 
		printf "\e[1;36;100m ~ %s ~ \e[0m\n" "$1" 
	fi 
}

if [ "$NAME" = "" ] 
then 

	debug "A unique name for the container must be set" 

	exit 1

else 
	
	debug "Run 'Python:$VERSION $SCRIPT' with name '$NAME'"

	debug "PWD = $PWD"

	docker run \
		-it \
		--rm \
		--name "$NAME" \
		-m "4m" \
		-v "$PWD:/usr/src/$BASEDIR" \
		-w "$SCRIPTPATH/$BASEDIR" \
		-e "HOSTNAME=$HOSTNAME" \
		-e "HOME=$SCRIPTPATH" \
		-e "FAAS=NOTHUSSERVERLESS" \
		-e "PEER=$PEER" \
		-e "GPG_KEY" \
		-e "PYTHON_GET_PIP_URL" \
		-e "PYTHON_GET_PIP_SHA256" \
		-e "PYTHON_PIP_VERSION" \
		python:$VERSION \
		python -OO -X utf8 -I $SCRIPT
		#-d \

	case  "$?" in 
		0) debug "Script terminé, aucun problème" 
		;;
		137) debug "Docker a rencontré une erreur (mémoire consommée trop importante)" 
		;;
	esac 

	exit 0

fi





