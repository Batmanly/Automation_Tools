import time

import shodan

shodan_api_key = "SHODAN_API_KEY"
api = shodan.Shodan(shodan_api_key)
out_file = open('promethus_list.txt', 'w')
words = open("bug_bounty-wordList.txt", "r")

for word in words:
    query = f'http.title:"Prometheus Time series" ssl:"{word}"'
    time.sleep(0.01)
    try:
        results = api.search(query)
        print(f"Result Found: {results['total']}")

        for result in results["matches"]:

            port = result['port']
            print(f"IP: {result['ip_str'] + ':' + str(port)}")
            if port in [80, 443]:
                if port == 80:
                    scheme = "http://"
                else:
                    scheme = "https://"

                out = scheme + result['ip_str']
            else:
                out = "http://" + result['ip_str'] + ':' + str(port)
            out_file.write(out + '\n')
            print("")
    except shodan.APIError as e:
        print(f"Error: {e}")
