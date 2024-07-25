import requests

with open("school.txt", "r") as f:
	    word = (f.read().split())

url = "http://150.95.91.122:2003/frame/0010001/2024-07-25/"

for path in word:
	respose = requests.get(url+path)
	if not respose.ok:
		print(url+path, "off")
	else:
		print(url+path, "on")
		with open("webon.txt", "a") as f:
			f.write(url+path + "\n")
