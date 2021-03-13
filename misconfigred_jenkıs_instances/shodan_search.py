import shodan

SHODAN_API_KEY = "SHODAN_API_KEY"
# Jenkins Without Authentication "X-Jenkins"
# http.title:"Dashboard"
# Login with SSO(Single Sign On) like
# github,bitbucket etc.
# html:"securityRealm"
# All jenkins instance "X-Jenkins"
api = shodan.Shodan(SHODAN_API_KEY)
words = open("bug_bounty-wordList.txt", "r")
django_debug_list = open("jenkins-list.txt", "w")
for word in words.readlines():
    query = "X-Jenkins" + 'html:"securityRealm"' + word.strip('\n')
    try:
        result = api.search(query)
        print(f'Result found : {result["total"]}')
        for result in result['matches']:
            print(word)
            print(f'IP: {result["ip_str"]}')
            port = result['port']
            if port in [80, 443]:
                if port == 443:
                    ip = "https://" + result['ip_str']
                else:
                    ip = "http://" + result['ip_str']
            else:
                ip = "http://" + result['ip_str'] + "" + str(port)
            django_debug_list.write(ip + "\n")
            print("")
    except Exception as e:
        print(e)
