import tldextract
domainList = open("bug_bounty-domainList.txt","r")
word_list = open("bug_bounty-wordList.txt","w")
for domain in domainList.readlines():
    tld = tldextract.extract(domain)
    word_list.write(tld.domain + "\n")