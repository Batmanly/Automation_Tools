domains = open("bug_bounty-domainList.txt","r")
domains2 = open("bug-bounty-domains-2.txt","w")
for domain in domains.readlines():
    domains2.write(domain.lstrip('www.'))