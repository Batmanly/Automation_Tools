import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def isodomainlive(domain):
    https = "https://" + domain
    http = "http://"+domain
    urls = []
    try:
        requests.get(https + "/robots.txt",timeout=5,verify=False)
        urls.append(https)
    except:
        pass
    try:
        requests.get(http + "/robots.txt",timeout=5,verify=False)
        urls.append(http)
    except:
        pass
    if urls:
        return urls
    else:
        return False