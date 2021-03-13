liste = list()
with open("prometheus_instances_without_authentication/bug_bounty-wordList.txt", "r") as file:
    for word in file.readlines():
        if word not in liste:
            liste.append(word)

with open("bug_bounty_clean.txt", "w") as file:
    for word in liste:
        file.write(word)
