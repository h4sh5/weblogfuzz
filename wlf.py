#!/usr/bin/env python3
import requests
import sys
import time
import random

url = sys.argv[1]
randualines = open('chrome.csv','r').read().split('\n')[1:]
randuas = [x.split('"')[1] for x in randualines[1:210]]
# print(randuas[1:5])

def randip():
	a,b,c,d = random.randrange(0,255),random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
	ip = f"{a}.{b}.{c}.{d}"
	return ip

def randua():
	return random.choice(randuas)

# print(randip())

for i in range(2000):
	headers = {"X-Forwarded-For":randip(), "User-Agent":randua()}
	r = requests.get(url, headers=headers)
	time.sleep(random.randrange(0,200)/10000)

