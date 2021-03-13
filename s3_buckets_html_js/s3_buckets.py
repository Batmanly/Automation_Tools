import re
from urllib.parse import unquote

import requests

import domain_check

domains = open("bug-bounty-domains-2.txt", "r")
for domain in domains.readlines():
    subdomains = open(domain.rstrip("\n") + "_subdomains.txt", "r")
    for subdomain in subdomains.readlines():
        buckets = []
        urls = domain_check.isdomainlive(subdomain.rstrip("\n"))
        if urls:
            for url in urls:
                print("checking - " + url)
                try:
                    html = requests.get(url=url, timeout=10, verify=False).content
                    try:
                        html = unquote(str(html))
                    except Exception as e:
                        print(e)
                    regjs = r"(?<=src=['\"])[a-zA-Z0-9_\.\-\:\/]+\.js"
                    regs3 = r"[\w\-\.]+\.s3\.?(?:[\w\-\.]+)?\.amazonaws\.com|(?< !\.)s3\.?(?:[\w\-\.]+)?\.amazonaws\.com\\?\ / [\w\-\.]+"
                    js = re.findall(regjs, html)
                    s3 = re.findall(regs3, html)
                    buckets = buckets + s3
                    if len(js) > 0:
                        for i in js:
                            if i.startswith('//'):
                                jsurl = i.replace('//', 'http://')
                            elif i.startswith('http'):
                                jsurl = i
                            else:
                                jsurl = url + '/' + i
                            try:
                                jsfile = requests.get(jsurl, timeout=10).content
                                s3 = re.findall(regs3, jsfile)
                            except Exception as y:
                                pass
                            if s3:
                                buckets = buckets + s3
                except Exception as x:
                    pass
                for bucket in buckets:
                    print(bucket)
