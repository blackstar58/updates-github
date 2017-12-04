#!/usr/bin/python

import sys

count  = 0
ip_old = None
acct_id = None
cmp_id = None
date = None
time = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 6:
        print("Break Out")
        # Something has gone wrong. Skip this line.
        continue

    this_day,this_time,this_acctid,this_cmpid,this_ip,this_total = data_mapped
    print(this_day,this_time,this_acctid,this_cmpid,this_ip,this_total)

    if ip_old and ip_old != this_ip and acct_id != this_acctid and cmp_id != this_cmpid and date != this_day and time != this_time:
        print ip_old, "\t",date,"\t",this_time ,"\t", count
        ip_old = this_ip;
        count = 0
        acct_id = this_acctid
        cmp_id = this_cmpid
        date = this_day
        time = this_time
    ip_old = this_ip
    count += 1

if ip_old != None:
     print ip_old, "\t",date,"\t",time,"\t", count
