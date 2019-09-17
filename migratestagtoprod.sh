#!/bin/bash
## -d is the host target -s is the sitename
## given $d and $s, prepare the FS on the target host
while getopts ":d:" o; do
    case "${o}" in
        d)
            d=${OPTARG}
            ;;
    esac
done

STAGDIR=/mnt/qs_ssd/www/stag/$d/
PRODDIR=/mnt/qs_ssd/d7/prod/www/$d

mkdir $PRODDIR
chown jenk:apache $PRODDIR
chmod 775 $PRODDIR
chmod ug+s $PRODDIR

rsync -avzhP --exclude-from=sites_exclude.txt $STAGDIR $PRODDIR
sed -i 's/stag.umwebdb.umass.edu/umwebdb.umass.edu/g' $PRODDIR/sites/default/settings.php
sed -i 's/3307/3308/g' $PRODDIR/sites/default/settings.php

ssh d7prod "cd /var/www/$d; drush sqlc < ${d}_drpl.sql; exit"


# ssh d7prod "sudo -i; cp -a /etc/httpd/conf.d/sites-available/uww.conf /etc/httpd/conf.d/sites-available/${d}.conf;exit"
# ssh d7prod "sudo -i; sed -i 's/uww/${d}/g' /etc/httpd/conf.d/sites-available/${d}.conf;exit"
# ssh d7prod "sudo -i; sed -i 's/uww/${d}/g' /etc/httpd/conf.d/sites-available/${d}.conf; ensite ${d}; exit"

