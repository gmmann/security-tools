
import requests
import csv
import os
url_list_file = './urllist'
output_file = './url_status.txt'
os.remove(output_file)
print(output_file + "has been Removed!")

with open(url_list_file, "r") as url_list:
    url_list_file_read = csv.reader(url_list)
    for url_row in url_list_file_read:
        url = 'http://' + url_row[0]
        # print(url)
        r = requests.get(url, allow_redirects=False)
        # print(r.url)
        # print(r.history)
        # print(r.status_code)
        status_string = str(r.status_code)
        write_output_file = open(output_file,'a+')
        if r.status_code == 200:
            write_output_file.writelines ('Site          : ' + url + ' \n' )
            write_output_file.writelines('Response Code : ' + status_string + ' \n' )
            write_output_file.writelines('Result        : This responds to HTTP and is BAD!! \n' )     
        elif r.status_code == 302 :    
            write_output_file.writelines('Site          : ' + url + ' \n' )
            write_output_file.writelines('Response Code : ' + status_string + ' \n' )
            write_output_file.writelines('Result        : This is ok and redirects \n' )     
            # print('This is ok and redirects')
        else:
            write_output_file.writelines('Site          : ' + url + ' \n' )
            write_output_file.writelines('Response Code : ' + status_string + ' \n' )
            write_output_file.writelines('Result        : This is likely ok and redirects probably \n' )     

