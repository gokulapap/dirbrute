import requests 
from termcolor import colored

url = input("Enter domain name: ")
path = input("Enter path of payloads: ")

file = open(path, "r")

for i in range(15):
	a = file.readline()
	
	r = requests.get(url+a)
	s = r.status_code

	if s == 200:
		color = 'green'
	elif s == 404:
		color = 'red'
	else:
		color = 'yellow'

	print(colored("\n=======================================",color))
	print(colored("Path: "+url+a,color))
	print(colored("status_code: "+str(s),color))
	print(colored("=======================================",color))

file.close()