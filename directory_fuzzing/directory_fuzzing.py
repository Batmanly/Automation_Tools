import wfuzz

import domain_check

wordlist = "https://raw.githubusercontent.com/maurosoria/dirsearch/master/db/dicc.txt"
domains = open("bug-bounty-domains-2.txt", "r")
payloads = wfuzz.get_payloads(wordlist)
for domain in domains.readlines():
    subdomains = open(domain.rstrip("\n") + "_subdomains.txt", "r")
    for subdomains in subdomains.readlines():
        urls = domain_check.isodomainlive(subdomains.rstrip("\n"))
        if urls:
            for url in urls:
                print("Fuzzing =" + url)
                try:
                    fuzzer = payloads.fuzz(url=url + "/FUZZ", sc=[200, 301])
                    for result in fuzzer:
                        print(result)
                except:
                    pass
