#!/bin/bash
## -d is the host target -s is the sitename
## Give -d "stag", "dev" or "prod"
## given $d and $s, prepare the FS on the target host
while getopts ":d:s:" o; do
    case "${o}" in
        s)
            s=${OPTARG}
            ;;
        d)
            d=${OPTARG}
            ;;
    esac
done

DIR=/mnt/qs_ssd/www/$d/$s
mkdir $DIR
chown jenk:apache $DIR; chmod 775 $DIR; chmod ug+s $DIR
