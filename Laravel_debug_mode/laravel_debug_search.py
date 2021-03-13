import re

import requests

django_debug_list = open("laravel-debug-list.txt", "r")
regex = r"(?:laravel):\/\/"
for ip in django_debug_list.readlines():
    try:
        response = requests.post(url=ip.rstrip("\n") + "/admin", data={}, verify=False)
        if re.search(regex, response.content.decode()):
            print("laravel URI found")
            print("ip: " + ip.rstrip("\n") + "/admin")
    except Exception as e:
        print(e)
