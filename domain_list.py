sites_list = open("bug_bounty-sites.txt", "r")
sites = sites_list.readlines()
domainList = open("bug_bounty-domainList.txt", "w")

for site in sites:
    split_site = site.split('/')
    if len(split_site) > 1:
        if "www." in split_site[2]:
            print(split_site[2])
            split_site[2] = split_site[2].replace("www.", "")
        domainList.write(split_site[2] + "\n")
