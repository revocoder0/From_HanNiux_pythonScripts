import requests


bright_red = "\033[0;91m"
domain=input("Enter Domain name : ")
file = open("/usr/share/wordlists/dirb/small.txt")
content = file.read()
subdomains=content.splitlines()
for subdomain in subdomains:
    url=f"http://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print(bright_red + "[+] Discovered subdomain: ", url)