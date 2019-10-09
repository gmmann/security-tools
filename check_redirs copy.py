
import requests
import csv
import os
import sys
import socket
url_list_file = './urllist'
output_file = './url_status.txt'
output_file_bad = './url_responds_to_http.txt'
port_test = '80'

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        # http_open = 'True'
        # # print(http_open)
        return True
   except:
        # http_open = 'False'
        return False
        # print(http_open)



def cleanup_old_file():
    if os.path.exists(output_file):
        os.remove(output_file)
        print(output_file + "has been Removed!")
    else:
        print('output file did not exist, continuing')
    if os.path.exists(output_file_bad):
        os.remove(output_file_bad)
        print(output_file_bad + "has been Removed!")
    else:
        print('Http responding report output file did not exist, continuing')
cleanup_old_file()




def response_code_output():
    write_output_file.writelines('Site Name        : ' + url + ' \n' )
    write_output_file.writelines('Site Address     : ' + url_ip + ' \n' )
    write_output_file.writelines('Response Code    : ' + status_string + ' \n' )

def response_code_output_bad():
    write_bad_output_file.writelines('Site Name        : ' + url + ' \n' )
    write_bad_output_file.writelines('Site Address     : ' + url_ip + ' \n' )
    write_bad_output_file.writelines('Response Code    : ' + status_string + ' \n' )

# def __get_ip_of_hostname__():
#     try:
#            url_ip = socket.gethostbyname(url_row[0])
#        except socket.gaierror
#            pass
#        except:
#            print ("Unexpected error:", sys.exc_info()[0])
#            #return ip


with open(url_list_file, "r") as url_list:
    url_list_file_read = csv.reader(url_list)
    url_list.readline()
    for url_row in url_list_file_read:
        # url_ip = os.system("nslookup " + str(url_list_file_read))
        # print(url_row[0])
        # __get_ip_of_hostname__
        url_ip = socket.gethostbyname(url_row[0])
        if not(url_ip):
            print(url + 'cannot be resolved, moving on....')
        port_is_open = isOpen(url_ip, port_test)
        if port_is_open:
            # print(url_ip)
            # print(port_is_open)
            # print(http_open)
            url = 'http://' + url_row[0]
            # print(url)
            r = requests.get(url, allow_redirects=False)
            # print(r.url)
            # print(r.history)
            # print(r.status_code)
            status_string = str(r.status_code)
            status_output = r.history
            write_output_file = open(output_file,'a+')
            write_bad_output_file = open(output_file_bad,'a+')
            if r.status_code == 200:
                response_code_output()
                # write_output_file.writelines ('Site          : ' + url + ' \n' )
                # write_output_file.writelines('Response Code : ' + status_string + ' \n' )
                write_output_file.writelines('Result         : This responds to HTTP and is BAD!! \n' )
                write_output_file.writelines('\n' )
                response_code_output_bad()
                write_bad_output_file.writelines('Result         : This responds to HTTP and is BAD!! \n' )
                write_bad_output_file.writelines('\n' )

            elif r.status_code in (300, 301, 302, 303, 304, 305, 307, 308) :
                response_code_output()
                # write_output_file.writelines('Site          : ' + url + ' \n' )
                # write_output_file.writelines('Response Code : ' + status_string + ' \n' )
                write_output_file.writelines('Result           : This is ok and redirects \n' )
                # write_output_file.writelines('\n' )
                # print('This is ok and redirects')
                response_with_redirs = requests.get(url, allow_redirects=True)
                response_with_redirs.history
                # print(response_with_redirs.history)
                for resp_redir in response_with_redirs.history:
                    redir_url = response_with_redirs.url
                write_output_file.writelines('Redirect URL is  : ' + redir_url +  '\n' )
            else:
                response_code_output()
                # write_output_file.writelines('Site          : ' + url + ' \n' )
                # write_output_file.writelines('Response Code : ' + status_string + ' \n' )
                write_output_file.writelines('Result         : This is likely ok and redirects probably \n' )
                write_output_file.writelines('\n' )
        write_output_file.writelines('Report Complete \n')
        write_output_file.close