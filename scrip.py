import whois

name = input("Enter domain : ")

domain = whois.whois(name)

print(domain)
