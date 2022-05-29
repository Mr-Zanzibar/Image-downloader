import requests
web = input("Paste your website link: ")
r = requests.get(web)

print(r.content)
with open("output.jpg", "wb") as f:
  f.write(r.content)
