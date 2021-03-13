import requests
import wfuzz
wordlist = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/DiscoverContent/spring-boot.txt').text.split("\n")
springs = open("spring_boot_server.txt","r")
payloads = wfuzz.get_payloads(wordlist)
for spring in springs.readlines():
    print("Fuzzing - " + spring)
    try:
        fuzzer = payloads.fuzz(url=spring.strip("\n")+"/FUZZ",sc=[200])
        for result in fuzzer:
            print(result)
    except:
        pass