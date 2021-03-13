import requests as rt
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urls = open("grafana_list.txt", "r")
data = {"user": "admin", "password": "admin"}
endpoint = "/login"
for url in urls.readlines():
    print("Testing =" + url)
    try:
        req = rt.post(url=url.rstrip("\n") + endpoint, json=data, verify=False)
        if req.status_code == 200:
            print("login Success")
    except:
        pass
