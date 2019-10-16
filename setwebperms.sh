#!/bin/bash
if [ $# -ne 2 ]
then
  echo "Improper number of arguments."
  echo "Set application permissions <DEV|STAG|PROD> <SITENAME>"
  exit
fi

WEBROOT="/mnt/qs_ssd/www/"
WEBPATH="${WEBROOT}${1}/${2}"

chown -RL jenk:apache $WEBPATH
find $WEBPATH -type d -exec chmod 775 {} \;
find $WEBPATH -type d -exec chmod g+s {} \;
find $WEBPATH -type f -exec chmod 664 {} \;
chmod 644 "${WEBPATH}/sites/default/settings.php"