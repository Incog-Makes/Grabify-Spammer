import requests
import time
from stem import Signal
from stem.control import Controller
#simple variable to make while loop
i = 2
#request counter
NUM = 0
#handling the request for a new connection node via control port, referenced partially from another site but lost it :/
def new_ip():
    with Controller.from_port(port = 9051) as control:
        control.authenticate(password="password") #password being the password you chose, so make sure to replace that, UNHASHED!!
        control.signal(Signal.NEWNYM)
        control.close()
#grabs tor localhost proxy
def tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port but double check
    session.proxies = {'http':  'socks5://127.0.0.1:9150',
                       'https': 'socks5://127.0.0.1:9150'}
    return session
	
#headers and url to change, changing header isn't needed
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
url = 'http/s url here'
#calls tor proxy to open session 
session = tor_session()
while i == 2:
	#GET request with parameters passed through
	x = session.get(url,headers=headers)
	NUM = NUM+1
	print(str(NUM) + " requests sent!")
	#calling function to change node ip
	new_ip()

	#forced wait to ensure a new ip (isnt essential)
	time.sleep(0.2)
	#making a new session 
	session = tor_session()
	#rinse and repeat
	x = session.get(url,headers=headers)
	NUM = NUM+1
	print(str(NUM) + " requests sent!")

