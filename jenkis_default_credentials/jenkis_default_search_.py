import requests as rt
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urls = open("jenkins_list.txt","r")
data = {"j_username":"admin","j_password":"password"}
endpoint="/j_acegi_security_check"
for url in urls.readlines():
    url = url.rstrip("\n")
    print("Testing -"+url)
    try:
        req = rt.post(url=url+endpoint,data=data,verify=False)
        if req.headers.get('location') and not 'loginError' in req.headers["location"]:
            print("login Success" + url)
    except:
        pass