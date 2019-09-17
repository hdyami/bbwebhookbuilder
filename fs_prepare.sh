#!/bin/bash
## -d is the host target -s is the sitename
## given $d and $s, prepare the FS on the target host
while getopts ":s:" o; do
    case "${o}" in
        s)
            s=${OPTARG}
            ;;
        d)
            d=${OPTARG}
            ;;
    esac
done

DIR=/var/www/$s

ssh $d "sudo -i mkdir $DIR"
ssh $d "sudo -i chown jenk:apache $DIR; sudo -i chmod 775 $DIR; sudo -i chmod ug+s $DIR"
