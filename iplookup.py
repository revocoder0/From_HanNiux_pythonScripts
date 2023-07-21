from ipwhois import IPWhois

from pprint import pprint

ip=input("Enter IP Addres : ")
obj = IPWhois(ip)

results = obj.lookup_whois()
pprint(results)