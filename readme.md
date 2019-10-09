The check_redirs files is intended to 
1. look at the urlist file as input, for a for in loop per entry or urls/fqdns
2. check if port 80 is open and continue
3. do a GEt on the http based url and find out status, while not following redirects
4. depending on the code provided, output to either of 2 reports
    a generic report on all url/fqdns
    a report on the fqdn/urls that respond with a 200 NOT redirecting to https and should be looked at by an app/system team.

    


