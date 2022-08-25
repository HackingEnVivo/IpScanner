from socket import gethostbyname
from colorama import Fore, init
init()
def Miscript():
	print(Fore.GREEN +'Welcome to Ip Scanner by: Hack Underway \U0001F1F5\U0001F1EA')
	target = input('./Enter the Host: ')
	targetIP = gethostbyname(target)
	print('Target IP ===>', targetIP)
	print('+------------------------------------+')
	Miscript()
Miscript()

#pip install emoji
#pip install gethostbyname
#pip install colorama
