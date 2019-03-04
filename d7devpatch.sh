#!/bin/bash
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

#echo "s = ${s}"
#echo "d = ${d}"

# assume there are some lazy developers - pull all sites
# foreach /var/www cd then git pull
ssh jenk@d7dev "cd /var/www/cryptozoo; git pull" 

# patch the sites
# foreach /var/www cd then patch with drush
ssh jenk@d7dev "drush @cryptozoo-dev up --security-only -y"

# commit and push patch changes
#foreach /var/www cd then git commit then git push
ssh jenk@d7dev "cd /var/www/cryptozoo; git commit -am 'patch commit'; git push origin master"
