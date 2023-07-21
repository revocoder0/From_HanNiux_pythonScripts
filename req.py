import requests

# Prompt the user to enter the domain name
url = input("Enter Domain name: ")

# Make the HTTP GET request
response = requests.get(url)

# Rest of your code to process the response
# ...
