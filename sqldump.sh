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

curl -u jenk:4ef8589e4926010533377fa27429dc55 --data "token=2M3gX7QsIhqfaFH8XFEGJN55nCd6tV3y" --data "SITENAME=${s}" --data "HOST=${d}" -X POST https://build.www.umass.edu/job/sqldump/buildWithParameters