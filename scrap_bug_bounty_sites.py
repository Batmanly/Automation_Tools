import requests
from bs4 import BeautifulSoup as sp

url = "https://www.vulnerability-lab.com/list-of-bug-bounty-programs.php"  # our url for parsing

webpage = requests.get(url=url)  # we make get requests and assign it webpage
soup = sp(webpage.content, 'html.parser')  # we create soup object for parse webpage content
tables = soup.find_all('table')  # take tables from soup object with find_all methods
a_tags = tables[4].find_all('a')  # take a tags in the table
with open("bug_bounty-sites.txt", "w") as sites_list:  # open a file for write url list

    for a in a_tags:
        if "mailto" in a:
            pass
        elif "http" not in a.get("href"):
            sites_list.write("http://" + a.get("href") + "\n")
        else:
            sites_list.write(a.get('href') + "\n")  # write url list after open file
