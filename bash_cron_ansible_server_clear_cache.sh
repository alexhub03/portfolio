# Cat /root/al/cache/clear_cache_mem_servername_.sh
# Bash script to clear vm cache and make a log

#!/bin/bash
ansible --private-key=/root/.ssh/id_rsa_satprod -i /root/al/cache/servername.txt all -m shell -a "sync;echo 1 > /proc/sys/vm/drop_caches;date" > /root/al/cache/log/$(date+"%Y-%m-%d-%H-%M-%S").txt

# Alternative path for backup inv: /home/shell/inventory/servername
# Crontab setting: 3 hours crontab: 0 */3 * * * 

# Clear cache example path - /root/all/cache/log/

fpath=/root/al/cache/log/*
find $fpath -type f -mtrime +20 -exec ls -ltrh {} \; > /root/al/cache/fodler.out
find $fpath -type f -mtime +20 -exec rm -rf {} \;
count=$(cat /root/al/cache/folder.out | wc -l)