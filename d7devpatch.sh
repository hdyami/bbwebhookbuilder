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

# https://unix.stackexchange.com/questions/1459/remote-for-loop-over-ssh
ssh jenk@d7dev "for i in $(find /var/www/ -maxdepth 1 -type d | xargs -t -I{} basename {}-dev); do echo '@$i'; done"

# assume there are some lazy developers - pull all sites
# foreach /var/www cd then git pull
#ssh jenk@d7dev "cd /var/www/cryptozoo; git pull" 

# patch the sites
# foreach /var/www cd then patch with drush
#ssh jenk@d7dev "drush @cryptozoo-dev up --security-only -y"

# commit and push patch changes
#foreach /var/www cd then git commit then git push
#ssh jenk@d7dev "cd /var/www/cryptozoo; git commit -am 'patch commit'; git push origin master"
