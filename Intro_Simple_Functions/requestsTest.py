import requests
import turtle

r = requests.get('https://api.github.com/user')

for element in r.json():
	turtle.forward(len(element*10))
	turtle.right(len(element)*10)
