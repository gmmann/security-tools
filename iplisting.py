
import csv
import os
import sys
# import nmap 
import socket

ip_list_file = './iplist'
output_file = './ip_status.txt'


with open(ip_list_file, "r") as ip_list:
    ip_list_file_read = csv.reader(ip_list)
    ip_list.readline()
    for ip_row in ip_list_file_read:
        print (ip_row[0])
