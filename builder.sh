#!/bin/bash
while getopts ":d:s:" o; do
    case "${o}" in
        s)
            s=${OPTARG}
            ;;
        d)
            d=${OPTARG}
            ;;
        f)
            f=${OPTARG}
            ;;
    esac
done

curl -u jenk:4ef8589e4926010533377fa27429dc55 --data "token=0IKD35R4ixyb50ShSTcvsFrJqUXOh8nS" --data "SITENAME=${s}" --data "DESTINATION=${d}" --data "-X POST https://build.www.umass.edu/job/builder/buildWithParameters
