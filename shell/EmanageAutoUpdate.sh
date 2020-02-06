#!/bin/bash -l

date="`date '+%Y-%m-%d'`"
cd /var/bin/python/e-manage_batch/src/main/batch/

python3.7 EmanageAutoUpdate.py -date $date
