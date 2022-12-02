import os
import sys
import time
from termcolor import colored
import socket


def booking():
	x = ''
	print(colored('Every Time You Run This Code, Give File A New Name', 'red'))
	file = input('Name The File You Are Saving: ')
	while x != 'quit':
		url = input('What Is The URL: ')
#		file = input('Give File A Name: ')
		IP_address = socket.gethostbyname(url)
		print(IP_address)
		format = file + '.txt'
		layout = url + '\n' + IP_address + '\n \n'
		layout2 = IP_address + '\n'

		with open(format, 'a') as f:
			f.write(layout)
		with open('IPs.txt', 'a') as f2:
			f2.write(layout2)
#		move = 'mv ' + format + ' SITES'
#		os.system(move)

		x = input('[cont]inue  OR  [quit]: ')

	move = 'mv ' + format + ' SITES'
	os.system(move)

booking()
